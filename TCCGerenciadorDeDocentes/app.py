from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, make_response
from supabase_config import supabase
import bcrypt
import uuid
from functools import wraps
from datetime import datetime
import qrcode
import socket
from flask import send_file
from io import BytesIO
from weasyprint import HTML
import html
import base64
import os
from flask import current_app

app = Flask(__name__)
app.secret_key = 'your-secret-key'

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return '127.0.0.1'

local_ip = get_local_ip()
url = f"http://{local_ip}:5000"
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("static/qrcode.png")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, faça login primeiro.', 'error')
            response = make_response(redirect(url_for('index')))
            response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
            return response
        return f(*args, **kwargs)
    return decorated_function

def check_user_type(user_id):
    result = supabase.from_('usuarios').select('tipo_usuario').eq('id', user_id).execute()
    return result.data[0]['tipo_usuario'] if result.data else None

def get_user_name(user_id):
    result = supabase.from_('usuarios').select('nome').eq('id', user_id).execute()
    return result.data[0]['nome'] if result.data else 'Usuário'

@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    result = supabase.from_('usuarios').select('*').eq('email', email).execute()

    if result.data and bcrypt.checkpw(senha.encode('utf-8'), result.data[0]['senha'].encode('utf-8')):
        session['user_id'] = str(result.data[0]['id'])
        session['tipo_usuario'] = result.data[0]['tipo_usuario']
        response = make_response(redirect(url_for('dashboard')))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
    else:
        flash('E-mail ou senha inválidos.', 'error')
        response = make_response(redirect(url_for('index')))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        tipo_usuario = request.form['tipo_usuario']

        if not all([nome, email, senha, tipo_usuario]):
            flash('Todos os campos são obrigatórios.', 'error')
            return redirect(url_for('cadastro'))

        if tipo_usuario not in ['admin', 'coordenador']:
            flash('Tipo de usuário inválido.', 'error')
            return redirect(url_for('cadastro'))

        result = supabase.from_('usuarios').select('id').eq('email', email).execute()
        if result.data:
            flash('E-mail já cadastrado.', 'error')
            return redirect(url_for('cadastro'))

        hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        supabase.from_('usuarios').insert({
            'nome': nome,
            'email': email,
            'senha': hashed_senha,
            'tipo_usuario': tipo_usuario
        }).execute()

        flash('Cadastro realizado com sucesso! Faça login.', 'success')
        response = make_response(redirect(url_for('index')))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

    response = make_response(render_template('cadastro.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/dashboard')
@login_required
def dashboard():
    tipo_usuario = check_user_type(session['user_id'])
    response = make_response(render_template('dashboard.html', tipo_usuario=tipo_usuario))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/editar_conta')
@login_required
def editar_conta():
    usuario_nome = get_user_name(session['user_id'])
    response = make_response(render_template('editar.html', usuario_nome=usuario_nome))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/alterar_email', methods=['POST'])
@login_required
def alterar_email():
    email_atual = request.form['email_atual']
    email_novo = request.form['email_novo']
    user_id = session['user_id']

    result = supabase.from_('usuarios').select('email').eq('id', user_id).execute()
    if not result.data or result.data[0]['email'] != email_atual:
        flash('E-mail atual incorreto.', 'error')
        return redirect(url_for('editar_conta'))

    email_check = supabase.from_('usuarios').select('id').eq('email', email_novo).execute()
    if email_check.data:
        flash('O novo e-mail já está em uso.', 'error')
        return redirect(url_for('editar_conta'))

    supabase.from_('usuarios').update({'email': email_novo}).eq('id', user_id).execute()
    flash('E-mail alterado com sucesso.', 'success')
    response = make_response(redirect(url_for('editar_conta')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/alterar_senha', methods=['POST'])
@login_required
def alterar_senha():
    senha_atual = request.form['senha_atual']
    senha_nova = request.form['senha_nova']
    user_id = session['user_id']

    result = supabase.from_('usuarios').select('senha').eq('id', user_id).execute()
    if not result.data or not bcrypt.checkpw(senha_atual.encode('utf-8'), result.data[0]['senha'].encode('utf-8')):
        flash('Senha atual incorreta.', 'error')
        return redirect(url_for('editar_conta'))

    hashed_senha = bcrypt.hashpw(senha_nova.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    supabase.from_('usuarios').update({'senha': hashed_senha}).eq('id', user_id).execute()
    flash('Senha alterada com sucesso.', 'success')
    response = make_response(redirect(url_for('editar_conta')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/excluir_conta', methods=['POST'])
@login_required
def excluir_conta():
    senha_atual = request.form['senha_atual']
    confirmar_senha = request.form['confirmar_senha']
    user_id = session['user_id']

    if senha_atual != confirmar_senha:
        flash('As senhas não coincidem.', 'error')
        return redirect(url_for('editar_conta'))

    result = supabase.from_('usuarios').select('senha').eq('id', user_id).execute()
    if not result.data or not bcrypt.checkpw(senha_atual.encode('utf-8'), result.data[0]['senha'].encode('utf-8')):
        flash('Senha atual incorreta.', 'error')
        return redirect(url_for('editar_conta'))

    supabase.from_('usuarios').delete().eq('id', user_id).execute()
    session.clear()
    flash('Conta excluída com sucesso.', 'success')
    response = make_response(redirect(url_for('index')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/logout')
def logout():
    session.clear()
    flash('Logout realizado com sucesso.', 'success')
    response = make_response(redirect(url_for('index')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/cadastrar_docente', methods=['POST'])
@login_required
def cadastrar_docente():
    if check_user_type(session['user_id']) != 'admin':
        flash('Acesso não autorizado.', 'error')
        return redirect(url_for('dashboard'))

    data = request.form
    supabase.from_('docentes').insert({
        'nome': data['nome'],
        'email': data['email'],
        'telefone': data['telefone'],
        'cpf': data['cpf'],
        'status': data['status'],
        'carga_horaria_max': int(data['carga_horaria_max'])
    }).execute()

    flash('Docente cadastrado com sucesso.', 'success')
    response = make_response(redirect(url_for('dashboard')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/cadastrar_contrato', methods=['POST'])
@login_required
def cadastrar_contrato():
    if check_user_type(session['user_id']) != 'admin':
        flash('Acesso não autorizado.', 'error')
        return redirect(url_for('dashboard'))

    data = request.form
    supabase.from_('contratos').insert({
        'docente_id': data['docente_id'],
        'data_inicio': data['data_inicio'],
        'data_fim': data['data_fim'],
        'tipo_contrato': data['tipo_contrato'],
        'valor_hora': float(data['valor_hora'])
    }).execute()

    flash('Contrato cadastrado com sucesso.', 'success')
    response = make_response(redirect(url_for('dashboard')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/cadastrar_turma', methods=['POST'])
@login_required
def cadastrar_turma():
    if check_user_type(session['user_id']) != 'admin':
        flash('Acesso não autorizado.', 'error')
        return redirect(url_for('dashboard'))

    data = request.form
    supabase.from_('turmas').insert({
        'nome': data['nome'],
        'periodo': data['periodo']
    }).execute()

    flash('Turma cadastrada com sucesso.', 'success')
    response = make_response(redirect(url_for('dashboard')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/cadastrar_disciplina', methods=['POST'])
@login_required
def cadastrar_disciplina():
    if check_user_type(session['user_id']) != 'admin':
        flash('Acesso não autorizado.', 'error')
        return redirect(url_for('dashboard'))

    data = request.form
    supabase.from_('disciplinas').insert({
        'nome': data['nome']
    }).execute()

    flash('Disciplina cadastrada com sucesso.', 'success')
    response = make_response(redirect(url_for('dashboard')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/alocar_docente', methods=['POST'])
@login_required
def alocar_docente():
    if check_user_type(session['user_id']) != 'coordenador':
        flash('Acesso não autorizado.', 'error')
        return redirect(url_for('dashboard'))

    data = request.form
    docente_id = data['docente_id']
    horas_atribuidas = int(data['horas_atribuidas'])

    if horas_atribuidas <= 0:
        flash('As horas atribuídas devem ser maiores que zero.', 'error')
        return redirect(url_for('dashboard'))

    docente = supabase.from_('docentes').select('carga_horaria_max').eq('id', docente_id).execute()
    if not docente.data:
        flash('Docente inválido.', 'error')
        return redirect(url_for('dashboard'))

    carga_horaria_max = docente.data[0]['carga_horaria_max']

    alocacoes = supabase.from_('alocacoes').select('horas_atribuidas').eq('docente_id', docente_id).execute()
    horas_atuais = sum(alocacao['horas_atribuidas'] for alocacao in alocacoes.data)

    if horas_atuais + horas_atribuidas > carga_horaria_max:
        flash(f'A alocação excede a carga horária máxima do docente ({carga_horaria_max} horas). Horas atuais: {horas_atuais}.', 'error')
        return redirect(url_for('dashboard'))

    supabase.from_('alocacoes').insert({
        'docente_id': docente_id,
        'disciplina_id': data['disciplina_id'],
        'turma_id': data['turma_id'],
        'horas_atribuidas': horas_atribuidas
    }).execute()

    flash('Docente alocado com sucesso.', 'success')
    response = make_response(redirect(url_for('dashboard')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/transferir_docente', methods=['POST'])
@login_required
def transferir_docente():
    if check_user_type(session['user_id']) != 'coordenador':
        flash('Acesso não autorizado.', 'error')
        return redirect(url_for('dashboard'))

    data = request.form
    docente_id = data.get('docente_id')
    turma_origem = data.get('turma_origem')
    turma_destino = data.get('turma_destino')

    if not all([docente_id, turma_origem, turma_destino]):
        flash('Todos os campos são obrigatórios.', 'error')
        return redirect(url_for('dashboard'))

    docente = supabase.from_('docentes').select('id').eq('id', docente_id).execute()
    if not docente.data:
        flash('Docente inválido.', 'error')
        return redirect(url_for('dashboard'))

    turma_origem_check = supabase.from_('turmas').select('id').eq('id', turma_origem).execute()
    turma_destino_check = supabase.from_('turmas').select('id').eq('id', turma_destino).execute()
    if not turma_origem_check.data or not turma_destino_check.data:
        flash('Uma ou ambas as turmas são inválidas.', 'error')
        return redirect(url_for('dashboard'))

    if turma_origem == turma_destino:
        flash('A turma de origem deve ser diferente da turma de destino.', 'error')
        return redirect(url_for('dashboard'))

    try:
        supabase.from_('transferencias').insert({
            'docente_id': docente_id,
            'turma_origem': turma_origem,
            'turma_destino': turma_destino,
            'data_transferencia': datetime.now().date().isoformat()
        }).execute()

        flash('Transferência realizada com sucesso.', 'success')
    except Exception as e:
        flash(f'Erro ao realizar a transferência: {str(e)}', 'error')

    response = make_response(redirect(url_for('dashboard')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/registros/<tipo>')
@login_required
def registros(tipo):
    if tipo not in ['docentes', 'contratos', 'turmas', 'disciplinas', 'alocacoes', 'transferencias']:
        flash('Tipo de registro inválido.', 'error')
        return redirect(url_for('dashboard'))

    if tipo == 'contratos':
        data = supabase.rpc('get_contratos_with_docente').execute().data
    elif tipo == 'alocacoes':
        data = supabase.rpc('get_alocacoes_with_relations').execute().data
    elif tipo == 'transferencias':
        data = supabase.rpc('get_transferencias_with_relations').execute().data
    else:
        data = supabase.from_(tipo).select('*').execute().data

    response = make_response(render_template('registros.html', tipo=tipo, registros=data))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/editar_registro/<tipo>/<id>', methods=['POST'])
@login_required
def editar_registro(tipo, id):
    valid_types = ['docentes', 'contratos', 'turmas', 'disciplinas', 'alocacoes', 'transferencias']
    if tipo not in valid_types:
        flash('Tipo de registro inválido.', 'error')
        return redirect(url_for('registros', tipo=tipo))

    existing = supabase.from_(tipo).select('id').eq('id', id).execute()
    if not existing.data:
        flash('Registro não encontrado.', 'error')
        return redirect(url_for('registros', tipo=tipo))

    data = request.form.to_dict()

    data = {k: v for k, v in data.items() if v is not None and (v != '' or k in ['email', 'telefone', 'cpf', 'status', 'data_fim'])}

    try:
        if tipo == 'docentes':
            if 'nome' not in data or not data['nome']:
                flash('O nome é obrigatório.', 'error')
                return redirect(url_for('registros', tipo=tipo))
            if 'carga_horaria_max' in data:
                try:
                    data['carga_horaria_max'] = int(data['carga_horaria_max'])
                    if data['carga_horaria_max'] < 0:
                        flash('A carga horária máxima não pode ser negativa.', 'error')
                        return redirect(url_for('registros', tipo=tipo))
                except ValueError:
                    flash('Carga horária máxima deve ser um número válido.', 'error')
                    return redirect(url_for('registros', tipo=tipo))
            if 'cpf' in data and data['cpf']:
                cpf_check = supabase.from_('docentes').select('id').eq('cpf', data['cpf']).neq('id', id).execute()
                if cpf_check.data:
                    flash('CPF já cadastrado para outro docente.', 'error')
                    return redirect(url_for('registros', tipo=tipo))

        elif tipo == 'contratos':
            if 'docente_id' in data:
                docente = supabase.from_('docentes').select('id').eq('id', data['docente_id']).execute()
                if not docente.data:
                    flash('Docente inválido.', 'error')
                    return redirect(url_for('registros', tipo=tipo))
            if 'data_inicio' not in data or not data['data_inicio']:
                flash('A data de início é obrigatória.', 'error')
                return redirect(url_for('registros', tipo=tipo))
            if 'tipo_contrato' not in data or not data['tipo_contrato']:
                flash('O tipo de contrato é obrigatório.', 'error')
                return redirect(url_for('registros', tipo=tipo))
            if 'valor_hora' in data:
                try:
                    data['valor_hora'] = float(data['valor_hora'])
                    if data['valor_hora'] < 0:
                        flash('O valor por hora não pode ser negativo.', 'error')
                        return redirect(url_for('registros', tipo=tipo))
                except ValueError:
                    flash('Valor por hora deve ser um número válido.', 'error')
                    return redirect(url_for('registros', tipo=tipo))

        elif tipo == 'turmas':
            if 'nome' not in data or not data['nome']:
                flash('O nome é obrigatório.', 'error')
                return redirect(url_for('registros', tipo=tipo))
            if 'periodo' not in data or not data['periodo']:
                flash('O período é obrigatório.', 'error')
                return redirect(url_for('registros', tipo=tipo))

        elif tipo == 'disciplinas':
            if 'nome' not in data or not data['nome']:
                flash('O nome é obrigatório.', 'error')
                return redirect(url_for('registros', tipo=tipo))
            nome_check = supabase.from_('disciplinas').select('id').eq('nome', data['nome']).neq('id', id).execute()
            if nome_check.data:
                flash('Nome da disciplina já cadastrado.', 'error')
                return redirect(url_for('registros', tipo=tipo))

        elif tipo == 'alocacoes':
            if 'docente_id' in data:
                docente = supabase.from_('docentes').select('id').eq('id', data['docente_id']).execute()
                if not docente.data:
                    flash('Docente inválido.', 'error')
                    return redirect(url_for('registros', tipo=tipo))
            if 'disciplina_id' in data:
                disciplina = supabase.from_('disciplinas').select('id').eq('id', data['disciplina_id']).execute()
                if not disciplina.data:
                    flash('Disciplina inválida.', 'error')
                    return redirect(url_for('registros', tipo=tipo))
            if 'turma_id' in data:
                turma = supabase.from_('turmas').select('id').eq('id', data['turma_id']).execute()
                if not turma.data:
                    flash('Turma inválida.', 'error')
                    return redirect(url_for('registros', tipo=tipo))
            if 'horas_atribuidas' in data:
                try:
                    data['horas_atribuidas'] = int(data['horas_atribuidas'])
                    if data['horas_atribuidas'] < 0:
                        flash('As horas atribuídas não podem ser negativas.', 'error')
                        return redirect(url_for('registros', tipo=tipo))
                except ValueError:
                    flash('Horas atribuídas deve ser um número válido.', 'error')
                    return redirect(url_for('registros', tipo=tipo))

        elif tipo == 'transferencias':
            if 'docente_id' in data:
                docente = supabase.from_('docentes').select('id').eq('id', data['docente_id']).execute()
                if not docente.data:
                    flash('Docente inválido.', 'error')
                    return redirect(url_for('registros', tipo=tipo))
            if 'turma_origem' in data:
                turma_origem = supabase.from_('turmas').select('id').eq('id', data['turma_origem']).execute()
                if not turma_origem.data:
                    flash('Turma de origem inválida.', 'error')
                    return redirect(url_for('registros', tipo=tipo))
            if 'turma_destino' in data:
                turma_destino = supabase.from_('turmas').select('id').eq('id', data['turma_destino']).execute()
                if not turma_destino.data:
                    flash('Turma de destino inválida.', 'error')
                    return redirect(url_for('registros', tipo=tipo))
            if 'turma_origem' in data and 'turma_destino' in data and data['turma_origem'] == data['turma_destino']:
                flash('A turma de origem deve ser diferente da turma de destino.', 'error')
                return redirect(url_for('registros', tipo=tipo))
            if 'data_transferencia' in data:
                del data['data_transferencia']

        supabase.from_(tipo).update(data).eq('id', id).execute()
        flash('Registro editado com sucesso.', 'success')

    except Exception as e:
        flash(f'Erro ao editar o registro: {str(e)}', 'error')
        print(f'Erro no endpoint editar_registro: {str(e)}')  # Log para depuração

    response = make_response(redirect(url_for('registros', tipo=tipo)))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/excluir_registro/<tipo>/<id>')
@login_required
def excluir_registro(tipo, id):
    if tipo not in ['docentes', 'contratos', 'turmas', 'disciplinas', 'alocacoes', 'transferencias']:
        flash('Tipo de registro inválido.', 'error')
        return redirect(url_for('dashboard'))

    supabase.from_(tipo).delete().eq('id', id).execute()

    flash('Registro excluído com sucesso.', 'success')
    response = make_response(redirect(url_for('registros', tipo=tipo)))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/get_docentes')
@login_required
def get_docentes():
    docentes = supabase.from_('docentes').select('id, nome').execute().data
    response = make_response(jsonify(docentes))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/get_turmas')
@login_required
def get_turmas():
    turmas = supabase.from_('turmas').select('id, nome').execute().data
    response = make_response(jsonify(turmas))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/get_disciplinas')
@login_required
def get_disciplinas():
    disciplinas = supabase.from_('disciplinas').select('id, nome').execute().data
    response = make_response(jsonify(disciplinas))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/gerar_relatorio/<docente_id>')
@login_required
def gerar_relatorio(docente_id):
    if check_user_type(session['user_id']) != 'coordenador':
        flash('Acesso não autorizado.', 'error')
        return redirect(url_for('dashboard'))

    docente = supabase.from_('docentes').select('nome, email, telefone, cpf, status, carga_horaria_max').eq('id', docente_id).execute()
    if not docente.data:
        flash('Docente inválido.', 'error')
        return redirect(url_for('dashboard'))
    docente = docente.data[0]

    contratos = supabase.from_('contratos').select('tipo_contrato, data_inicio, data_fim, valor_hora').eq('docente_id', docente_id).order('data_inicio', desc=True).execute()
    contrato = contratos.data[0] if contratos.data else None

    alocacoes = supabase.rpc('get_alocacoes_with_relations').execute().data
    alocacoes_docente = [a for a in alocacoes if a['docente_id'] == docente_id]

    transferencias = supabase.rpc('get_transferencias_with_relations').execute().data
    transferencias_docente = [t for t in transferencias if t['docente_id'] == docente_id]

    try:
        image_path = os.path.join(app.static_folder, 'icone.png')
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        image_data_uri = f"data:image/png;base64,{base64_image}"
    except Exception as e:
        print(f"Erro ao carregar imagem: {str(e)}")
        flash(f'Erro ao carregar a imagem para o relatório: {str(e)}', 'error')
        image_data_uri = ""

    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{
                margin: 2.5cm; /* Margens consistentes em todas as páginas */
            }}
            body {{
                font-family: Arial, sans-serif;
                margin: 0; /* Remove margens do body, já que @page lida com isso */
                font-size: 12pt;
            }}
            h1 {{
                text-align: center;
                font-size: 24pt;
                margin-bottom: 0.5cm;
            }}
            h2 {{
                font-size: 18pt;
                margin-top: 1cm;
                margin-bottom: 0.5cm;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 1cm;
            }}
            th, td {{
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
                font-weight: bold;
            }}
            .no-data {{
                font-style: italic;
                color: #555;
            }}
            .center {{
                text-align: center;
            }}
            .logo {{
                display: block;
                margin: 0 auto 20px auto;
                width: 350px; /* Mantido o tamanho maior da logo */
                height: auto;
            }}
        </style>
    </head>
    <body>
        {"<img src=\"" + image_data_uri + "\" alt=\"Logo SENAI\" class=\"logo\">" if image_data_uri else "<p>Imagem não disponível</p>"}
        <h1>Relatório</h1>
        <p class="center"><strong>Data de Geração:</strong> {datetime.now().strftime('%d/%m/%Y')}</p>

        <h2>Dados do Docente</h2>
        <table>
            <tr><th>Docente</th><th>Registros</th></tr>
            <tr><td>Nome</td><td>{html.escape(docente['nome'])}</td></tr>
            <tr><td>E-mail</td><td>{html.escape(docente['email'] or 'N/A')}</td></tr>
            <tr><td>Telefone</td><td>{html.escape(docente['telefone'] or 'N/A')}</td></tr>
            <tr><td>CPF</td><td>{html.escape(docente['cpf'] or 'N/A')}</td></tr>
            <tr><td>Status</td><td>{html.escape(docente['status'])}</td></tr>
            <tr><td>Carga Horária Máxima</td><td>{docente['carga_horaria_max']} horas</td></tr>
        </table>

        <h2>Contrato Atual</h2>
        {'<table><tr><th>Contrato</th><th>Registros</th></tr>'
         f'<tr><td>Tipo de Contrato</td><td>{html.escape(contrato["tipo_contrato"])}</td></tr>'
         f'<tr><td>Data de Início</td><td>{contrato["data_inicio"]}</td></tr>'
         f'<tr><td>Data de Fim</td><td>{contrato["data_fim"] or "N/A"}</td></tr>'
         f'<tr><td>Valor por Hora</td><td>R$ {contrato["valor_hora"]:.2f}</td></tr>'
         '</table>' if contrato else '<p class="no-data">Nenhum contrato encontrado.</p>'}

        <h2>Turmas Alocadas</h2>
        {'<table><tr><th>Turma</th><th>Disciplina</th><th>Horas Atribuídas</th></tr>' +
         ''.join([f'<tr><td>{html.escape(a["turma_nome"])}</td><td>{html.escape(a["disciplina_nome"])}</td><td>{a["horas_atribuidas"]} horas</td></tr>'
                  for a in alocacoes_docente]) + '</table>' if alocacoes_docente else '<p class="no-data">Nenhuma alocação encontrada.</p>'}

        <h2>Transferências</h2>
        {'<table><tr><th>Turma Origem</th><th>Turma Destino</th><th>Data</th></tr>' +
         ''.join([f'<tr><td>{html.escape(t["turma_origem_nome"])}</td><td>{html.escape(t["turma_destino_nome"])}</td><td>{t["data_transferencia"]}</td></tr>'
                  for t in transferencias_docente]) + '</table>' if transferencias_docente else '<p class="no-data">Nenhuma transferência encontrada.</p>'}

    </body>
    </html>
    """

    try:
        pdf_buffer = BytesIO()
        HTML(string=html_content).write_pdf(pdf_buffer)
        pdf_buffer.seek(0)

        response = send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=f'relatorio_docente_{docente_id}.pdf',
            mimetype='application/pdf'
        )
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
    except Exception as e:
        print(f"Erro ao gerar PDF com WeasyPrint: {str(e)}")
        flash(f'Erro ao gerar o relatório em PDF: {str(e)}', 'error')
        return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')