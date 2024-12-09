import unittest
from unittest.mock import patch, MagicMock
from player import Player
from midiutil import MIDIFile

class TestPlayer(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para cada teste
        self.text = "C D E F G A B"
        self.bpm = 120
        self.instrument = 0
        self.player = Player(self.text, self.bpm, self.instrument)

    def test_initialization(self):
        # Verifica se os valores iniciais são atribuídos corretamente
        self.assertEqual(self.player.get___bpm(), self.bpm)
        self.assertEqual(self.player.get_instrument(), self.instrument)
        self.assertEqual(self.player.get_volume(), 50)
        self.assertEqual(self.player.get_octave(), 0)

    def test_set_get_bpm(self):
        # Testa os métodos de acesso e modificação do BPM
        new_bpm = 90
        self.player.set___bpm(new_bpm)
        self.assertEqual(self.player.get___bpm(), new_bpm)

    def test_set_get_instrument(self):
        # Testa os métodos de acesso e modificação do instrumento
        new_instrument = 10
        self.player.set_instrument(new_instrument)
        self.assertEqual(self.player.get_instrument(), new_instrument)

    @patch('pygame.init')
    @patch('pygame.mixer.music.load')
    @patch('pygame.mixer.music.play')
    @patch('builtins.open', new_callable=MagicMock)
    @patch('midiutil.MIDIFile')
    def test_compose(self, MockMIDIFile, mock_open, mock_play, mock_load, mock_pygame_init):
        # Mocka dependências para testar o método `compose`
        mock_midi_instance = MagicMock()
        MockMIDIFile.return_value = mock_midi_instance

        decoder_mock = MagicMock()
        with patch('player.Decoder', return_value=decoder_mock):
            decoder_mock.decode.return_value = mock_midi_instance

            self.player.compose()

            # Verifica se os métodos relevantes foram chamados
            decoder_mock.decode.assert_called_with(self.text)
            mock_open.assert_called_once_with("output.mid", "wb")
            mock_midi_instance.writeFile.assert_called_once()
            mock_load.assert_called_once_with("output.mid")
            mock_play.assert_called_once()

if __name__ == '__main__':
    unittest.main()
