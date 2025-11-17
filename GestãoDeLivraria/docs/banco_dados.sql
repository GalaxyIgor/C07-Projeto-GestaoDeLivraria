DROP DATABASE IF EXISTS livraria;
SET SQL_SAFE_UPDATES = 0;
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
    UltimaMovimentacao DATETIME NOT NULL,
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
(4, 'Clarice Lispector', 'Brasileira'),
(5, 'Isaac Asimov', 'Russo/Americano');

INSERT INTO Editora (idEditora, nomeEditora, cnpjEditora, localEditora) VALUES
(1, 'Companhia Livro', '00.000.000/0000-00', 'São Paulo'),
(2, 'Editora Rio', '11.111.111/1111-11', 'Rio de Janeiro'),
(3, 'Editora Minas', '33.333.333/3333-33', 'Belo Horizonte'),
(4, 'Editora Fantasia', '44.444.444/4444-44', 'Curitiba');

INSERT INTO EstoqueLivros (idEstoqueLivros, quantidade, endereco, UltimaMovimentacao) VALUES
(1, 200, 'Rua Exemplo1, 100 - São Paulo', '2025-10-01 10:00:00'),
(2, 150, 'Rua Exemplo2, 45 - Rio de Janeiro', '2025-10-05 09:30:00'),
(3, 50, 'Av. Central, 20 - Curitiba', '2025-11-01 11:00:00');

INSERT INTO Livro (idLivro, títuloLivro, DataPublicacaoLivro, precoLivro, estoqueLivro, PaginasLivro, Editora_idEditora, Autor_idAutor, EstoqueLivros_idEstoqueLivros) VALUES
(1, 'Dom Casmurro', '1899-01-01', 39.90, 50, 256, 1, 1, 1),
(2, '1984', '1949-06-08', 49.90, 80, 328, 2, 2, 1),
(3, 'Harry Potter e a Pedra Filosofal', '1997-06-26', 60.00, 120, 320, 3, 3, 2),
(4, 'A Hora da Estrela', '1977-10-01', 29.90, 40, 96, 1, 4, 2),
(5, 'Eu, Robô', '1950-12-02', 55.00, 70, 253, 4, 5, 3);

INSERT INTO DetalhesDoLivro (idDetalhesDoLivro, Livro_Editora_idEditora, Livro_idLivro, numPaginasDetalhes, Idioma, sinopseDetalhes, Peso, Volume) VALUES
(1, 1, 1, 256, 'Português', 'A história de Bentinho e Capitu, marcada por ciúmes e dúvida.', 0.5, 1.2),
(2, 2, 2, 328, 'Inglês', 'Uma distopia sobre um regime totalitário e vigilância constante.', 0.6, 1.3),
(3, 3, 3, 320, 'Português', 'A jornada de um jovem bruxo em sua primeira aventura em Hogwarts.', 0.8, 1.5),
(4, 1, 4, 96, 'Português', 'Uma narrativa introspectiva sobre a vida de uma nordestina no Rio.', 0.3, 0.8),
(5, 4, 5, 253, 'Inglês', 'Coletânea de contos que estabelecem as Três Leis da Robótica.', 0.55, 1.25);

INSERT INTO Cliente (idCliente, nomeCliente, emailCliente, telefoneCliente) VALUES
(1, 'Igor', 'igorexemplo@email.com', '00000000000'),
(2, 'Nicholas', 'nicholasexemplo@email.com', '11111111111'),
(3, 'Ana', 'anaexemplo@email.com', '22222222222'),
(4, 'Pedro', 'pedroexemplo@email.com', '33333333333');

INSERT INTO Pedido (idPedido, dataPedido, valorTotal) VALUES
(1, '2025-10-10', 89.80),
(2, '2025-10-11', 120.00),
(3, '2025-10-12', 29.90),
(4, '2025-11-01', 55.00);

INSERT INTO Cliente_has_Pedido (Cliente_idCliente, Pedido_idPedido) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);

INSERT INTO Pedido_has_Livro (Pedido_idPedido, Livro_idLivro, Livro_Editora_idEditora, quantidade) VALUES
(1, 1, 1, 1),
(1, 2, 2, 1),
(2, 3, 3, 2),
(3, 4, 1, 1),
(4, 5, 4, 1);


-- Adiciona uma coluna para para identificar clientes premium - ALTER TABLE

ALTER TABLE Cliente
ADD COLUMN premiumCliente BOOLEAN DEFAULT FALSE;

-- Se esta FK não existir, remova a linha, mas a intenção é remover a coluna
-- Drop FK - remover colna

ALTER TABLE DetalhesDoLivro
DROP FOREIGN KEY DetalhesDoLivro_ibfk_2;

-- Remove a coluna redundante de Editora na tabela DetalhesDoLivro
ALTER TABLE DetalhesDoLivro
DROP COLUMN Livro_Editora_idEditora;



-- Update no preco do livro com nacionalidade britanica

UPDATE Livro l
    INNER JOIN Autor a ON l.Autor_idAutor = a.idAutor
        SET l.precoLivro = l.precoLivro * 1.10
            WHERE a.nacionalidadeAutor IN ('Britânico', 'Britânica');

-- Livros 2 (1984) e 3 (Harry Potter) modificados

-- SELECT * FROM Livro;

-- Atualiza o status premium do cliente 'Igor'

UPDATE Cliente
SET premiumCliente = TRUE
WHERE nomeCliente = 'Igor';


-- 1. Deleteando o pedido id = 4

DELETE FROM Pedido_has_Livro WHERE Pedido_idPedido = 4;
DELETE FROM Cliente_has_Pedido WHERE Pedido_idPedido = 4;
DELETE FROM Pedido WHERE idPedido = 4;

-- Delete cliente 'Pedro' com id 4, pedido cancelado e cliente removido

DELETE FROM Cliente WHERE idCliente = 4;


-- Criando usuario

CREATE USER IF NOT EXISTS 'joao'@'localhost' IDENTIFIED BY 'Joao@1234';


-- Concede privilégios de leitura, inserção e atualização
GRANT SELECT, INSERT, UPDATE ON livraria.* TO 'joao'@'localhost';

FLUSH PRIVILEGES;

-- VIEW: Exibe um resumo dos pedidos

CREATE OR REPLACE VIEW ResumoPedidos AS
SELECT
    p.idPedido,
    c.nomeCliente,
    l.títuloLivro,
    pl.quantidade,
    p.dataPedido,
    p.valorTotal
FROM Pedido p
INNER JOIN Cliente_has_Pedido cp ON p.idPedido = cp.Pedido_idPedido
INNER JOIN Cliente c ON cp.Cliente_idCliente = c.idCliente
INNER JOIN Pedido_has_Livro pl ON p.idPedido = pl.Pedido_idPedido
INNER JOIN Livro l ON pl.Livro_idLivro = l.idLivro
ORDER BY p.idPedido;

-- UTILIZAÇÃO DA VIEW
SELECT * FROM ResumoPedidos;

-- PROCEDURE: Get livros por ID do autor
DROP PROCEDURE IF EXISTS ObterLivrosPorAutor;

DELIMITER $$
CREATE PROCEDURE ObterLivrosPorAutor(IN autor_id INT)
BEGIN
    SELECT
        l.títuloLivro,
        e.nomeEditora,
        l.DataPublicacaoLivro
    FROM Livro l
    JOIN Editora e ON l.Editora_idEditora = e.idEditora
    WHERE l.Autor_idAutor = autor_id;
END$$
DELIMITER ;

-- UTILIZAÇÃO DA PROCEDURE - autor 1 machado de assis

CALL ObterLivrosPorAutor(1);

-- TRIGGER: Diminui o estoque de livros após a inserção de um item no pedido
DROP TRIGGER IF EXISTS trg_diminuir_estoque;

DELIMITER $$

CREATE TRIGGER `trg_diminuir_estoque`
AFTER INSERT ON `Pedido_has_Livro`
FOR EACH ROW
BEGIN
    UPDATE Livro
    SET estoqueLivro = estoqueLivro - NEW.quantidade
    WHERE idLivro = NEW.Livro_idLivro;
END$$

DELIMITER ;

-- teste trigger

-- Estoque inicial do livro 'Eu, Robô' id = 5
SELECT 'Estoque Inicial Eu, Robô (id=5):' AS Teste;
SELECT idLivro, títuloLivro, estoqueLivro FROM Livro WHERE idLivro = 5;

-- Insere um novo pedido para o livro 5, quantidade 2.
INSERT INTO Pedido (idPedido, dataPedido, valorTotal) VALUES (5, '2025-11-04', 110.00);

-- cliente igor
INSERT INTO Cliente_has_Pedido (Cliente_idCliente, Pedido_idPedido) VALUES (1, 5);

-- A TRIGGER será ativada no INSERT abaixo
INSERT INTO Pedido_has_Livro (Pedido_idPedido, Livro_idLivro, Livro_Editora_idEditora, quantidade)
VALUES (5, 5, 4, 2);

-- Verifica o estoque final - deve ter como incial 2
SELECT 'Estoque Final Eu, Robô (id=5):' AS Teste;
SELECT idLivro, títuloLivro, estoqueLivro FROM Livro WHERE idLivro = 5;


SELECT * FROM Livro;