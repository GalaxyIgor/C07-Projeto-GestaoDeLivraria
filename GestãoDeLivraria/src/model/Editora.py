class Editora:
    def __init__(self, idEditora=None, nomeEditora=None, nacionalidadeEditora=None):
        self.idEditora = idEditora
        self.nomeEditora = nomeEditora
        self.nacionalidadeEditora = nacionalidadeEditora

    # Método de representação para facilitar a exibição
    def __str__(self):
        return f"ID: {self.idEditora}, Nome: {self.nomeEditora}, Nacionalidade: {self.nacionalidadeEditora}"

    # --- Getters e Setters ---
    def getIdAutor(self):
        return self.idEditora

    def setNomeAutor(self, nomeEditora):
        self.nomeEditora = nomeEditora
