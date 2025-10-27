CREATE DATABASE IF NOT EXISTS livraria;
USE livraria;

CREATE TABLE Autor(
	idAutor INT NOT NULL,
    nomeAutor VARCHAR(120),
    nacionalidadeAutor VARCHAR(60),
    
    PRIMARY KEY (idAutor)
);

CREATE TABLE Editora(
	idEditora INT NOT NULL,
    nomeEditora VARCHAR(100) NOT NULL,
    cnpjEditora VARCHAR(20) NOT NULL UNIQUE,
    LocalEditora VARCHAR(45) NOT NULL,
    
    PRIMARY KEY (idEditora)
    
);

CREATE TABLE EstoqueLivros(
	idEstoqueLivros INT NOT NULL,
    quantidade INT NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    UltimaMovimentacao VARCHAR(45) NOT NULL,
    
    PRIMARY KEY (idEstoqueLivros)
);

CREATE TABLE Livro(
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

CREATE TABLE DetalhesDoLivro(
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

CREATE TABLE Cliente(
	idCliente INT NOT NULL,
    nomeCliente VARCHAR(120) NOT NULL,
    emailCliente VARCHAR(120) NOT NULL UNIQUE,
    telefoneCliente VARCHAR(45) NOT NULL UNIQUE,
    
    PRIMARY KEY (idCliente)
    
);

CREATE TABLE Pedido(
	idPedido INT NOT NULL,
    dataPedido DATE NOT NULL,
    valorTotal DECIMAL(10,2) NOT NULL,
    
    PRIMARY KEY (idPedido)
    
);

CREATE TABLE Cliente_has_Pedido(
	Cliente_idCliente INT NOT NULL,
    Pedido_idPedido INT NOT NULL,
    
    PRIMARY KEY (Cliente_idCliente, Pedido_idPedido),
    FOREIGN KEY (Cliente_idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (Pedido_idPedido) REFERENCES Pedido(idPedido)
);

CREATE TABLE Pedido_has_Livro(
	Pedido_idPedido INT NOT NULL,
    Livro_idLivro INT NOT NULL,
    Livro_Editora_idEditora INT NOT NULL,
    quantidade INT NOT NULL,
    
    PRIMARY KEY (Pedido_idPedido, Livro_idLivro, Livro_Editora_idEditora),
    FOREIGN KEY (Pedido_idPedido) REFERENCES Pedido(idPedido),
    FOREIGN KEY (Livro_idLivro) REFERENCES Livro(idLivro),
    FOREIGN KEY (Livro_Editora_idEditora) REFERENCES Editora(idEditora)
);

INSERT INTO Autor (idAutor, nomeAutor, nacionalidadeAutor) VALUES
(1, 'Machado de Assis', 'Brasileiro'),
(2, 'George Orwell', 'Britânico'),
(3, 'J.K. Rowling', 'Britânica'),
(4, 'Clarice Lispector', 'Brasileira');

INSERT INTO Editora (idEditora, nomeEditora, cnpjEditora, localEditora) VALUES
(1, 'Companhia Livro', '00.000.000/0000-00', 'São Paulo'),
(2, 'Editora Rio', '11.111.111/1111-11', 'Rio de Janeiro'),
(3, 'Editora Minas', '33.333.333/3333-33', 'Belo Horizonte');

INSERT INTO EstoqueLivros (idEstoqueLivros, endereco, quantidade, UltimaMovimentacao) VALUES
(1, 'Rua Exemplo1, 100 - São Paulo', 200, '2025-10-01 10:00:00'),
(2, 'Rua Exemplo2, 45 - Rio de Janeiro', 150, '2025-10-05 09:30:00');

INSERT INTO Livro (idLivro, tituloLivro, DataPublicacaoLivro, estoqueLivro, PaginaLivro, Editora_idEditora, EstoqueLivros_idEstoqueLivros, Autor_idAutor) VALUES
(1, 'Dom Casmurro', '1899-01-01 00:00:00', 50, 256, 1, 1, 1),
(2, '1984', '1949-06-08 00:00:00', 80, 328, 2, 1, 2),
(3, 'Harry Potter e a Pedra Filosofal', '1997-06-26 00:00:00', 120, 320, 3, 2, 3),
(4, 'A Hora da Estrela', '1977-10-01 00:00:00', 40, 96, 1, 2, 4);

INSERT INTO DetalhesDoLivro (idDetalhesDoLivro, numPaginasDetalhes, idioma, sinopseDetalhes, Volume, Peso, Livro_idLivro, Livro_Editora_idEditora) VALUES
(1, 256, 'Português', 'A história de Bentinho e Capitu, marcada por ciúmes e dúvida.', 1.2, 0.5, 1, 1),
(2, 328, 'Inglês', 'Uma distopia sobre um regime totalitário e vigilância constante.', 1.3, 0.6, 2, 2),
(3, 320, 'Português', 'A jornada de um jovem bruxo em sua primeira aventura em Hogwarts.', 1.5, 0.8, 3, 3),
(4, 96, 'Português', 'Uma narrativa introspectiva sobre a vida de uma nordestina no Rio.', 0.8, 0.3, 4, 1);

INSERT INTO Cliente (idCliente, nomeCliente, emailCliente, telefoneCliente) VALUES
(1, 'Igor', 'igorexemplo@email.com', '00000000000'),
(2, 'Nicholas', 'nicholasexemplo@email.com', '11111111111'),
(3, 'Ana', 'anaexemplo@email.com', '22222222222');

INSERT INTO Pedido (idPedido, data, valor_total, id_cliente) VALUES
(1, '2025-10-10 15:30:00', 89.90, 1),
(2, '2025-10-11 16:00:00', 120.50, 2),
(3, '2025-10-12 09:45:00', 59.90, 3);

INSERT INTO Cliente_has_Pedido (Cliente_idCliente, Pedido_idPedido) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO Pedido_has_Livro (Pedido_idPedido, Livro_idLivro, Livro_Editora_idEditora, quantidade) VALUES
(1, 1, 1, 1),  -- Igor comprou Dom Casmurro
(1, 2, 2, 1),  -- Igor comprou 1984
(2, 3, 3, 2),  -- Nicholas comprou 2 Harry Potter
(3, 4, 1, 1);  -- Ana comprou A Hora da Estrela