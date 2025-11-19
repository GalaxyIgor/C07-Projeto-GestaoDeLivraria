class Pedido:
    def __init__(self, idPedido=None, nomePedido=None, nacionalidadePedido=None):
        self.idPedido = idPedido
        self.nomePedido = nomePedido
        self.nacionalidadePedido = nacionalidadePedido

    # Método de representação para facilitar a exibição
    def __str__(self):
        return f"ID: {self.idPedido}, Nome: {self.nomePedido}, Nacionalidade: {self.nacionalidadePedido}"

    # --- Getters e Setters ---
    def getIdAutor(self):
        return self.idPedido

    def setNomeAutor(self, nomePedido):
        self.nomePedido = nomePedido