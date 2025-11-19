class Livro:
    def __init__(self, idLivro=None, nomeLivro=None, nacionalidadeLivro=None):
        self.idLivro = idLivro
        self.nomeLivro = nomeLivro
        self.nacionalidadeLivro = nacionalidadeLivro

    # Método de representação para facilitar a exibição
    def __str__(self):
        return f"ID: {self.idLivro}, Nome: {self.nomeLivro}, Nacionalidade: {self.nacionalidadeLivro}"

    # --- Getters e Setters ---
    def getIdAutor(self):
        return self.idLivro

    def setNomeAutor(self, nomeLivro):
        self.nomeLivro = nomeLivro
