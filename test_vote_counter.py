import unittest
from unittest.mock import patch, mock_open
from vote_counter import count_votes  # Suponiendo que el código refactorizado está en `vote_counter.py`

class TestVoteCounter(unittest.TestCase):

    @patch("builtins.print")
    def test_count_votes_valid_file(self, mock_print):
        # Archivo CSV con datos válidos
        mock_csv = """city,candidate,votes
        Springfield,Alice,1200
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")
        
        # Salida esperada después de sumar votos
        mock_print.assert_any_call("Alice: 3200 votes")
        mock_print.assert_any_call("Bob: 3250 votes")
        mock_print.assert_any_call("Winner is Bob")
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_count_votes_tie(self, mock_print):
        # Archivo CSV que genera un empate
        mock_csv = """city,candidate,votes
        Springfield,Alice,1500
        Springfield,Bob,1500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        # Salida esperada para el caso de empate
        mock_print.assert_any_call("Alice: 1500 votes")
        mock_print.assert_any_call("Bob: 1500 votes")
        mock_print.assert_any_call("There is a tie.")
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_count_votes_invalid_votes(self, mock_print):
        # Simular archivo CSV con datos inválidos
        mock_csv = """city,candidate,votes
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Springfield,Alice,invalid
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        # Salida esperada después de manejar los datos inválidos
        mock_print.assert_any_call("Bob: 3250 votes")
        mock_print.assert_any_call("Alice: 2000 votes")
        mock_print.assert_any_call("Winner is Bob")
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_no_votes(self, mock_print):
        # Archivo CSV sin votos válidos
        mock_csv = """city,candidate,votes"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        # Salida esperada cuando no hay votos válidos
        mock_print.assert_any_call("No valid votes found.")
        self.assertEqual(mock_print.call_count, 1)

if __name__ == "__main__":
    unittest.main()
