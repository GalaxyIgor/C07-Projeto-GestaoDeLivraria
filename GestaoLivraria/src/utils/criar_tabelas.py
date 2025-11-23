
from conection import Conexao
from mysql.connector import Error

def criar_tabelas():
    sql_script = """
    CREATE TABLE IF NOT EXISTS Autor (
        idAutor INT AUTO_INCREMENT PRIMARY KEY,
        nomeAutor VARCHAR(120) NOT NULL,
        nacionalidadeAutor VARCHAR(60)
    );

    CREATE TABLE IF NOT EXISTS Editora (
        idEditora INT NOT NULL,
        nomeEditora VARCHAR(100) NOT NULL,
        cnpjEditora VARCHAR(20) NOT NULL UNIQUE,
        LocalEditora VARCHAR(45) NOT NULL,
        PRIMARY KEY (idEditora)
        
    );

    CREATE TABLE IF NOT EXISTS Cliente (
        idCliente INT AUTO_INCREMENT PRIMARY KEY,
        nomeCliente VARCHAR(120) NOT NULL,
        emailCliente VARCHAR(120) UNIQUE NOT NULL,
        telefoneCliente VARCHAR(20)
    );

    CREATE TABLE IF NOT EXISTS Livro (
        idLivro INT NOT NULL,
        títuloLivro VARCHAR(150) NOT NULL,
        DataPublicacaoLivro DATE NOT NULL,
        precoLivro DECIMAL(10,2) NOT NULL,
        estoqueLivro INT NOT NULL,
        PaginasLivro INT NOT NULL,
        Editora_idEditora INT NOT NULL,
        Autor_idAutor INT NOT NULL,
        EstoqueLivros_idEstoqueLivros INT NOT NULL,
        
        PRIMARY KEY (idLivro),
        FOREIGN KEY (Editora_idEditora) REFERENCES Editora(idEditora),
        FOREIGN KEY (Autor_idAutor) REFERENCES Autor(idAutor),
        FOREIGN KEY (EstoqueLivros_idEstoqueLivros) REFERENCES EstoqueLivros(idEstoqueLivros)

    );

    CREATE TABLE IF NOT EXISTS Pedido (
        idPedido INT AUTO_INCREMENT PRIMARY KEY,
        dataPedido DATETIME DEFAULT CURRENT_TIMESTAMP,
        valorPedido DECIMAL(10,2) NOT NULL,
        idCliente INT NOT NULL,
        FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
    );
    
    
    CREATE TABLE IF NOT EXISTS EstoqueLivros(
        idEstoqueLivros INT NOT NULL,
        quantidade INT NOT NULL,
        endereco VARCHAR(100) NOT NULL,
        UltimaMovimentacao DATETIME NOT NULL,
        PRIMARY KEY (idEstoqueLivros)
    );
    
    CREATE TABLE IF NOT EXISTS DetalhesDoLivro(
        idDetalhesDoLivro INT NOT NULL,
        Livro_Editora_idEditora INT NOT NULL,
        Livro_idLivro INT NOT NULL,
        numPaginasDetalhes INT NOT NULL,
        Idioma VARCHAR(50),
        sinopseDetalhes TEXT(200),
        Peso FLOAT NOT NULL,
        Volume FLOAT NOT NULL,
        
        PRIMARY KEY (idDetalhesDoLivro),
        FOREIGN KEY (Livro_idLivro) REFERENCES Livro(idLivro),
        FOREIGN KEY (Livro_Editora_idEditora) REFERENCES Editora(idEditora)
    );
    
    CREATE TABLE  IF NOT EXISTS Cliente_has_Pedido(
        Cliente_idCliente INT NOT NULL,
        Pedido_idPedido INT NOT NULL,
        
        PRIMARY KEY (Cliente_idCliente, Pedido_idPedido),
        FOREIGN KEY (Cliente_idCliente) REFERENCES Cliente(idCliente),
        FOREIGN KEY (Pedido_idPedido) REFERENCES Pedido(idPedido)
    );

    CREATE TABLE IF NOT EXISTS Pedido_has_Livro(
        Pedido_idPedido INT NOT NULL,
        Livro_idLivro INT NOT NULL,
        Livro_Editora_idEditora INT NOT NULL,
        quantidade INT NOT NULL,
        
        PRIMARY KEY (Pedido_idPedido, Livro_idLivro, Livro_Editora_idEditora),
        FOREIGN KEY (Pedido_idPedido) REFERENCES Pedido(idPedido),
        FOREIGN KEY (Livro_idLivro) REFERENCES Livro(idLivro),
        FOREIGN KEY (Livro_Editora_idEditora) REFERENCES Editora(idEditora)
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
