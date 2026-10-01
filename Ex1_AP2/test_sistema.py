import unittest
from unittest.mock import Mock
from sistema import Pedido, ServicoProcessamento


class TesteProcessamento(unittest.TestCase):
    def test_processamento_com_sucesso(self):
        repo_mock = Mock()
        pedido_fake = Pedido(101, 150.0)
        repo_mock.buscar_por_id.return_value = pedido_fake

        comprovante_dummy = "comprovante_ficticio.pdf"

        servico = ServicoProcessamento(repo_mock)
        resultado = servico.processar_pagamento(101, comprovante_dummy)

        print("\nResultado do Teste 1:", resultado)
        self.assertEqual(resultado, "Pagamento do pedido 101 no valor de R$150.0 processado")

    def test_pedido_nao_encontrado(self):
        repo_mock = Mock()
        repo_mock.buscar_por_id.return_value = None

        comprovante_dummy = None

        servico = ServicoProcessamento(repo_mock)
        resultado = servico.processar_pagamento(999, comprovante_dummy)

        print("Resultado do Teste 2:", resultado)
        self.assertEqual(resultado, "Pedido não encontrado")


if __name__ == "__main__":
    unittest.main()