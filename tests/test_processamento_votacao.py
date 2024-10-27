import unittest
from colab_votacao import Votacao


class TestProcessamentoVotacao(unittest.TestCase):
    """Testes para o processamento de votos em uma votação."""

    def setUp(self):
        """Configura os candidatos para os testes."""
        self.candidatos = {"Candidato A": 0, "Candidato B": 0}
        self.votacao = Votacao(self.candidatos)

    def test_processar_voto_valido(self):
        """Verifica se um voto válido é processado corretamente."""
        self.votacao.processar_voto("Candidato A")
        self.assertEqual(self.candidatos["Candidato A"], 1)

    def test_processar_voto_invalido(self):
        """Verifica o comportamento ao votar em um candidato inválido."""
        self.votacao.processar_voto("Candidato C")
        self.assertEqual(self.candidatos["Candidato A"], 0)
        self.assertEqual(self.candidatos["Candidato B"], 0)

    def test_exibir_resultados(self):
        """Verifica se os resultados são exibidos corretamente."""
        self.votacao.processar_voto("Candidato A")
        self.votacao.processar_voto("Candidato B")
        self.votacao.exibir_resultados()


if __name__ == "__main__":
    unittest.main()