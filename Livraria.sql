CREATE DATABASE IF NOT EXISTS livraria;
USE livraria;

CREATE TABLE Autor(
	idAutor INT NOT NULL,
    nomeAutor VARCHAR(120),
    nacionalidadeAutor VARCHAR(60),
    
    PRIMARY KEY (idAutor)
);

CREATE TABLE EstoqueLivros(
	idEstoqueLivros INT NOT NULL,
    quantidade INT NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    UltimaMovimentacao VARCHAR(45) NOT NULL,
    
    PRIMARY KEY (EstoqueLivros)
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
    
    PRIMARY KEY (idDetalhesDoLivro, Livro_Editora_idEditora,Livro_idLivro)
    
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
    
    PRIMARY KEY (idLivro, Autor_idAutor,EstoqueLivros_idEstoqueLivros)
    
);

CREATE TABLE Editora(
	idEditora INT NOT NULL,
    nomeEditora VARCHAR(100) NOT NULL,
    cnpjEditora VARCHAR(20) NOT NULL UNIQUE,
    LocalEditora VARCHAR(45) NOT NULL,
    
    PRIMARY KEY (idEditora, Autor_idAutor,EstoqueLivros_idEstoqueLivros)
    
);

CREATE TABLE Editora(
	idEditora INT NOT NULL,
    nomeEditora VARCHAR(100) NOT NULL,
    cnpjEditora VARCHAR(20) NOT NULL UNIQUE,
    LocalEditora VARCHAR(45) NOT NULL,
    
    PRIMARY KEY (idEditora)
    
);


CREATE TABLE Pedido_has_Livro(
	Pedido_idPedido INT NOT NULL,
    Livro_idLivro VARCHAR(100) NOT NULL,
    Livro_Editora_idEditora VARCHAR(20) NOT NULL UNIQUE,
    quantidade VARCHAR(45) NOT NULL,
    
    PRIMARY KEY (Pedido_idPedido, Livro_idLivro,Livro_Editora_idEditora)
    
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
    
    PRIMARY KEY (Cliente_idCliente, Pedido_idPedido)
    
);
CREATE TABLE Cliente(
	idCliente INT NOT NULL,
    nomeCliente VARCHAR(120) NOT NULL,
    emailCliente VARCHAR(120) NOT NULL UNIQUE,
    telefoneCliente VARCHAR(45) NOT NULL UNIQUE,
    
    PRIMARY KEY (idCliente)
    
);