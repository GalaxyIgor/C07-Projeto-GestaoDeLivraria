class Autor:
    def __init__(self, idAutor=None, nomeAutor=None, nacionalidadeAutor=None):
        self.idAutor = idAutor
        self.nomeAutor = nomeAutor
        self.nacionalidadeAutor = nacionalidadeAutor

    # Método de representação para facilitar a exibição
    def __str__(self):
        return f"ID: {self.idAutor}, Nome: {self.nomeAutor}, Nacionalidade: {self.nacionalidadeAutor}"

    # --- Getters e Setters ---
    def getIdAutor(self):
        return self.idAutor

    def setNomeAutor(self, nomeAutor):
        self.nomeAutor = nomeAutor
