# Sistema de Livraria



## Escopo do Projeto

O objetivo deste projeto é desenvolver um sistema para gerenciamento de uma livraria.

O sistema permitirá o cadastro de livros, autores, clientes e pedidos, além do controle das compras realizadas.



## Entidades e Relacionamentos

O sistema terá as seguintes entidades principais:



1. **Livro**

- Atributos: id_livro(pk), títuloLivro, DataPublicacaoLivro, estoqueLivro, PaginaLivro, Editora_idEditora, EstoqueLivros_idEstoqueLivros, Autor_idAutor

- Um livro pode ter **um autor**.



2. **Autor**

- Atributos: idAutor(pk), nomeAutor, nacionalidadeAutor

- Um autor pode escrever **um ou vários livros**.



3. **Editora**

- Atributos: idEditora(pk), nomeEditora, cnpjEditora, localEditora

- Uma editora pode publicar **vários livros**, mas um livro pertence a apenas **uma editora**.



4. **Cliente**

- Atributos: id_cliente(pk), nomeCliente, emailCliente, telefoneCliente

- Um cliente pode realizar **vários pedidos**.



5. **Pedido**

- Atributos: id_pedido(pk), data, valor_total, id_cliente

- Um pedido pertence a **um único cliente**, mas pode conter **vários livros**.



7. **EstoqueLivros**

-  Atributos: idEstoqueLivros, endereco, quantidade, UltimaMovimentacao

-




8. **Cliente_has_Pedido**(tabela associativa para relacionamento N:M)

- Atributos: Cliente_idCliente, Pedido_idPedido

- 



9. **Pedido_has_Livro**(tabela associativa para relacionamento N:M)

- Atributos: Pedido_idPedido, Livro_idLivro, Livro_Editora_idEditora, quantidade

- Representa os livros comprados em cada pedido.
---



## Relacionamentos

- **Autor ↔ Livro** → N:M (um autor pode escrever vários livros e um livro pode ter vários autores).

- **Editora ↔ Livro** → 1:N (uma editora publica vários livros, mas cada livro tem apenas uma editora).

- **Cliente ↔ Pedido** → 1:N (um cliente pode fazer vários pedidos, mas um pedido pertence a apenas um cliente).

- **Pedido ↔ Livro** → N:M (um pedido pode ter vários livros e um livro pode estar em vários pedidos, resolvido pela entidade `ItemPedido`).

- **Pedido ↔ Cliente** → 1:N (cada pedido pertence a apenas um cliente).



---



## Requisitos atendidos

- Pelo menos **5 entidades diferentes** (Livro, Autor, Editora, Cliente, Pedido).

- Relacionamentos com todos os tipos:

- **1:1** → Cliente ↔ descrição

- **1:N** → Editora ↔ Livro, Cliente ↔ Pedido

- **N:M** → Autor ↔ Livro, Pedido ↔ Livro
