from database import conectar
class Venda:
    def __init__(self, produto, quantidade, preco):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
    
    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """
        INSERT INTO venda (produto, quantidade, preco)
        VALUES (?, ?, ?)
        """
        valores = (self.produto, self.quantidade, self.preco)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM VENDA")
        lista_vendas = cursor.fetchall()
        cursor.close()
        conexao.close()
        return lista_vendas