import unittest
from unittest.mock import patch, MagicMock
from ui.interface import Interface

class TestInterface(unittest.TestCase):
    def setUp(self):
        self.interface = Interface()

    def test_get_instrument(self):
        self.interface.instrument_input = "10"
        self.assertEqual(self.interface.get_instrument(), "10")

    def test_set_instrument(self):
        self.interface.set_instrument("5")
        self.assertEqual(self.interface.instrument_input, "5")

    def test_get_bpm(self):
        self.interface.bpm_input = "150"
        self.assertEqual(self.interface.get_bpm(), "150")

    def test_set_bpm(self):
        self.interface.set_bpm("200")
        self.assertEqual(self.interface.bpm_input, "200")

    def test_get_text(self):
        self.interface.text_input = "Sample Text"
        self.assertEqual(self.interface.get_text(), "Sample Text")

    def test_set_text(self):
        self.interface.set_text("New Text")
        self.assertEqual(self.interface.text_input, "New Text")

    def test_sanitize_file_text_with_valid_text(self):
        text = "Valid text"
        sanitized_text = self.interface._Interface__sanitize_file_text(text)
        self.assertEqual(sanitized_text, text)

    def test_sanitize_file_text_with_empty_text(self):
        self.interface.text_input = "Default Text"
        sanitized_text = self.interface._Interface__sanitize_file_text("")
        self.assertEqual(sanitized_text, "Default Text")

    @patch('ui.interface.Reader')
    def test_on_file_selected(self, MockReader):
        # Aplique um mock para Reader com o comportamento esperado
        mock_instance = MockReader.return_value
        mock_instance.read_file.return_value = "fake text"

        # Simule a seleção de arquivo
        selection = ['fake_file.txt']
        self.interface.on_file_selected(selection)

        # Verifique se o texto foi atribuído corretamente
        self.assertEqual(self.interface.text_input, "fake text")
        MockReader.assert_called_once_with('fake_file.txt')
        mock_instance.read_file.assert_called_once()

    @patch('ui.interface.Reader')  # Alterar para o caminho completo de importação
    def test_on_file_selected(self, MockReader):
        mock_instance = MockReader.return_value
        mock_instance.read_file.return_value = "fake text"

        selection = ['fake_file.txt']
        self.interface.on_file_selected(selection)

        self.assertEqual(self.interface.text_input, "fake text")
        MockReader.assert_called_once_with('fake_file.txt')
        mock_instance.read_file.assert_called_once()


if __name__ == "__main__":
    unittest.main()
