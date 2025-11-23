
from src.utils.conection import Conexao
from mysql.connector import Error

def criar_tabelas():
    sql_script = """
    CREATE TABLE IF NOT EXISTS Autor (
        idAutor INT AUTO_INCREMENT PRIMARY KEY,
        nomeAutor VARCHAR(120) NOT NULL,
        nacionalidadeAutor VARCHAR(60)
    );

    CREATE TABLE IF NOT EXISTS Editora (
        idEditora INT AUTO_INCREMENT PRIMARY KEY,
        nomeEditora VARCHAR(120) NOT NULL,
        cidadeEditora VARCHAR(80)
    );

    CREATE TABLE IF NOT EXISTS Cliente (
        idCliente INT AUTO_INCREMENT PRIMARY KEY,
        nomeCliente VARCHAR(120) NOT NULL,
        emailCliente VARCHAR(120) UNIQUE NOT NULL,
        telefoneCliente VARCHAR(20)
    );

    CREATE TABLE IF NOT EXISTS Livro (
        idLivro INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(150) NOT NULL,
        preco DECIMAL(10, 2) NOT NULL,
        anoPublicacao INT,
        idAutor INT,
        idEditora INT,
        FOREIGN KEY (idAutor) REFERENCES Autor(idAutor),
        FOREIGN KEY (idEditora) REFERENCES Editora(idEditora)
    );

    CREATE TABLE IF NOT EXISTS Pedido (
        idPedido INT AUTO_INCREMENT PRIMARY KEY,
        dataPedido DATETIME DEFAULT CURRENT_TIMESTAMP,
        idCliente INT NOT NULL,
        FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
    );

    CREATE TABLE IF NOT EXISTS PedidoItem (
        idPedido INT,
        idLivro INT,
        quantidade INT NOT NULL,
        precoUnitario DECIMAL(10,2) NOT NULL,
        PRIMARY KEY (idPedido, idLivro),
        FOREIGN KEY (idPedido) REFERENCES Pedido(idPedido),
        FOREIGN KEY (idLivro) REFERENCES Livro(idLivro)
    );
    """

    conexao_mysql = Conexao()
    
    try:
        conn = conexao_mysql.conectar()
        cursor = conn.cursor()

        print("\nCriando tabelas...")
        for comando in sql_script.split(";"):
            cmd = comando.strip()
            if cmd:
                cursor.execute(cmd + ";")
        
        conn.commit()
        print("Tabelas criadas com sucesso!")

    except Error as e:
        print(f"Erro ao criar tabelas: {e}")

    finally:
        cursor.close()
        conexao_mysql.fechar()


if __name__ == "__main__":
    criar_tabelas()
