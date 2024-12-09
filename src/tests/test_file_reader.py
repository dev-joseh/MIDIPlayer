import unittest
from unittest.mock import mock_open, patch
from file_reader import Reader

class TestReader(unittest.TestCase):
    def setUp(self):
        # Configuração inicial
        self.valid_file = "example.txt"
        self.invalid_file = "example.pdf"

    def test_read_valid_txt_file(self):
        # Mock para simular leitura de arquivo com sucesso
        mocked_file_content = "This is a test file content."
        with patch("builtins.open", mock_open(read_data=mocked_file_content)):
            reader = Reader(self.valid_file)
            content = reader.read_file()
            self.assertEqual(content, mocked_file_content)

    def test_read_invalid_file_type(self):
        # Testa comportamento ao passar um arquivo não .txt
        reader = Reader(self.invalid_file)
        with patch("builtins.print") as mocked_print:
            content = reader.read_file()
            mocked_print.assert_called_once_with("Only txt files are allowed")
            self.assertEqual(content, "")

    def test_file_not_found(self):
        # Testa comportamento ao tentar ler um arquivo inexistente
        with patch("builtins.open", side_effect=IOError):
            reader = Reader(self.valid_file)
            with patch("builtins.print") as mocked_print:
                content = reader.read_file()
                mocked_print.assert_called_once_with("Could not read file: ", self.valid_file)
                self.assertEqual(content, "")

    def test_empty_file(self):
        # Testa comportamento ao ler um arquivo vazio
        with patch("builtins.open", mock_open(read_data="")):
            reader = Reader(self.valid_file)
            content = reader.read_file()
            self.assertEqual(content, "")

    def test_internal_methods_are_private(self):
        # Verifica se os métodos privados não são acessíveis diretamente
        reader = Reader(self.valid_file)
        with self.assertRaises(AttributeError):
            reader.__file_is_txt()
        with self.assertRaises(AttributeError):
            reader.__get_text()
        with self.assertRaises(AttributeError):
            reader.__set_text("Some text")

if __name__ == "__main__":
    unittest.main()
