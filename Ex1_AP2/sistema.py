class Pedido:
    def __init__(self, id_pedido, valor_total):
        self.id_pedido = id_pedido
        self.valor_total = valor_total


class RepositorioPedidos:
    def buscar_por_id(self, id_pedido):
        pass


class ServicoProcessamento:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def processar_pagamento(self, id_pedido, comprovante_dummy):
        pedido = self.repositorio.buscar_por_id(id_pedido)
        if pedido is None:
            return "Pedido não encontrado"
        if pedido.valor_total > 0:
            return f"Pagamento do pedido {pedido.id_pedido} no valor de R${pedido.valor_total} processado"
        return "Valor inválido"