from Banco import Banco

class Cidades:
    def __init__(self, idcidade=0, nome="", estado=""):
        self.idcidade = idcidade
        self.nome = nome
        self.estado = estado

    def insertCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            INSERT INTO cidades (nome, estado)
            VALUES (?, ?)
            """, (self.nome, self.estado))
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {e}"

    def updateCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            UPDATE cidades
            SET nome = ?, estado = ?
            WHERE idcidade = ?
            """, (self.nome, self.estado, self.idcidade))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração da cidade: {e}"

    def deleteCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM cidades WHERE idcidade = ?", (self.idcidade,))
            banco.conexao.commit()
            c.close()
            return "Cidade excluída com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão da cidade: {e}"

    def selectCidade(self, idcidade):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM cidades WHERE idcidade = ?", (idcidade,))
            row = c.fetchone()
            if row:
                self.idcidade, self.nome, self.estado = row
            c.close()
            return "Busca feita com sucesso!" if row else "Cidade não encontrada."
        except Exception as e:
            return f"Ocorreu um erro na busca da cidade: {e}"