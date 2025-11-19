class Cliente:
    def __init__(self, idCliente=None, nomeCliente=None, nacionalidadeCliente=None):
        self.idCliente = idCliente
        self.nomeCliente = nomeCliente
        self.nacionalidadeCliente = nacionalidadeCliente

    # Método de representação para facilitar a exibição
    def __str__(self):
        return f"ID: {self.idCliente}, Nome: {self.nomeCliente}, Nacionalidade: {self.nacionalidadeCliente}"

    # --- Getters e Setters ---
    def getIdAutor(self):
        return self.idCliente

    def setNomeAutor(self, nomeCliente):
        self.nomeCliente = nomeCliente
