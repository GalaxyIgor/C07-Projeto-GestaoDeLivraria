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
    FOREIGH
);
