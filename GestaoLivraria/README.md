# Sistema de Livraria

## Participantes Do Projeto

Igor Nascimento Belisario - GES - 603

Nicholas Lima do Nascimento - GES - 697


## Escopo do Projeto

O objetivo deste projeto é desenvolver um sistema para gerenciamento de uma livraria.

O sistema permitirá o cadastro de livros, autores, clientes e pedidos, além do controle das compras realizadas.



## Entidades e Relacionamentos

O sistema terá as seguintes entidades principais:



1. **Livro**

- A entidade livro tem **um autor**  

- Atributos: 

        1. id_livro(pk)
        2. títuloLivro(VARCHAR)
        3. DataPublicacaoLivro(DATETIME)
        4. estoqueLivro(INT)
        5. PaginaLivro(INT)
        6. editora_idEditora(FK INT)
        7. EstoqueLivros_idEstoqueLivros(FK - INT)
        8. Autor_idAutor(FK - INT)


2. **Autor**

- Um autor pode escrever **um ou vários livros**  - 1:N.

- Atributos: 

        1. idAutor(pk)
        2. nomeAutor(VARCHAR)
        3. nacionalidadeAutor(VARCHAR)




3. **Editora**

- Uma editora pode publicar **vários livros**, mas um livro pertence a apenas **uma editora**.

- Atributos: 

        1. idEditora(pk)
        2. nomeEditora(VARCHAR)
        3. cnpjEditora(VARCHAR)
        4. localEditora(VARCHAR)
       


4. **Cliente**

- Um cliente pode realizar **vários pedidos**.

- Atributos:

        1. id_cliente(pk)
        2. nomeCliente (VARCHAR)
        3. emailCliente (VARCHAR)
        4. telefoneCliente (VARCHAR)


5. **Pedido**

- Um pedido pertence a **um único cliente**, mas pode conter **vários livros**.

- Atributos: 

        1. id_pedido(pk)
        2. data(DATETIME)
        3. valor_total(FLOAT)
        4. id_cliente(FK - INT)
    

7. **EstoqueLivros**

- O estoque armazena os livros pertencente a biblioteca onde **tem pelo menos um livro** - 1:N

-  Atributos: 

        1. idEstoqueLivros(INT)
        2. endereco(VARCHAR)
        3. quantidade(INT)
        4. UltimaMovimentacao(DATETIME)
     

8. **DetalhesDoLivro** 

- Entidade que contem mais caracteristicas do livro onde **tem apenas um livro** - 1:1

- Atributos:

        1. idDetalhesDoLivro(INT)
        2. numPaginasDetalhes(INT)
        3. idioma(VARCHAR)
        4. sinopseDetalhes(TEXT)
        5. Volume(FLOAT)
        6. Peso(FLOAT)
        7. Livro_idLivro(FK - INT)
        8. Livro_Editora_idEditora(FK - INT)


8. **Cliente_has_Pedido**(tabela associativa para relacionamento N:M)

- Atributos:

        1. Cliente_idCliente(FK -INT)
        2. Pedido_idPedido(FK - INT)



9. **Pedido_has_Livro**(tabela associativa para relacionamento N:M)

- Representa os livros comprados em cada pedido.

- Atributos: 

        1. Pedido_idPedido(FK - INT)
        2. Livro_idLivro(FK - INT)
        3. Livro_Editora_idEditora(FK - INT)
        4. quantidade(FK - INT)


## Relacionamentos

- **Autor ↔ Livro** → 1:N (um autor pode escrever vários livros e um livro pode ter apenas um ator).

- **DetalhesLivros ↔ Livro** → 1:1 (cada livro tem um relacionamento com uma entidade onde tem mais características do livro).

- **Editora ↔ Livro** → 1:N (uma editora publica vários livros, mas cada livro tem apenas uma editora).

- **Cliente ↔ Pedido** → 1:N (um cliente pode fazer vários pedidos, mas um pedido pertence a apenas um cliente).

- **Pedido ↔ Livro** → N:M (um pedido pode ter vários livros e um livro pode estar em vários pedidos).

- **Pedido ↔ Cliente** → 1:N (cada pedido pertence a apenas um cliente).

- **EstoqueLivros ↔ Livro** → 1:N (Estoque pode ter varios livros).


