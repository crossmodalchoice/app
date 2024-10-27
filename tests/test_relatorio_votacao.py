import unittest
from colab_votacao import Votacao


class TestRelatorioVotacao(unittest.TestCase):
    """Testes para a geração de relatórios de votação."""

    def setUp(self):
        """Configura os candidatos para o teste de relatório."""
        self.candidatos = {"Candidato A": 0, "Candidato B": 0}
        self.votacao = Votacao(self.candidatos)

    def test_relatorio_votos(self):
        """Verifica se a contagem de votos é feita corretamente."""
        self.votacao.processar_voto("Candidato A")
        self.votacao.processar_voto("Candidato A")
        self.votacao.processar_voto("Candidato B")
        self.assertEqual(self.candidatos["Candidato A"], 2)
        self.assertEqual(self.candidatos["Candidato B"], 1)

    def test_voto_invalido_nao_altera_contagem(self):
        """Verifica se votos inválidos não alteram a contagem."""
        self.votacao.processar_voto("Candidato C")
        self.assertEqual(self.candidatos["Candidato A"], 0)
        self.assertEqual(self.candidatos["Candidato B"], 0)


if __name__ == "__main__":
    unittest.main()