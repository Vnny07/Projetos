from Banco import Banco

class Usuarios(object):
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha="", estado=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha
        self.estado = estado

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into usuarios (nome, telefone, email, usuario, senha, estado) values (?, ?, ?, ?, ?, ?)",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha, self.estado))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update usuarios set nome = ?, telefone = ?, email = ?, usuario = ?, senha = ?, estado = ? where idusuario = ?",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha, self.estado, self.idusuario))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from usuarios where idusuario = ?", (self.idusuario,))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from usuarios where idusuario = ?", (idusuario,))
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
                self.estado = linha[6]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"

    def listUsers(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select idusuario, nome, estado from usuarios")
            users = c.fetchall()
            c.close()
            return users
        except:
            return "Ocorreu um erro ao listar os usuários"