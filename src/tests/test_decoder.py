import unittest
from unittest.mock import MagicMock
from midiutil import MIDIFile
from decoder import Decoder

class TestDecoder(unittest.TestCase):
    def setUp(self):
        # Configuração inicial: um MIDIFile com 1 trilha
        self.midi_file = MIDIFile(1)
        self.decoder = Decoder(self.midi_file)

    def test_play_note(self):
        self.midi_file.addNote = MagicMock()  # Mock do método addNote
        self.decoder.play_note("C")
        # Verifica se a nota foi adicionada
        self.midi_file.addNote.assert_called_once_with(0, 0, 60, 0.0, 1, 64)

    def test_random_note(self):
        self.midi_file.addNote = MagicMock()  # Mock do método addNote
        self.decoder.random_note()
        self.midi_file.addNote.assert_called_once()  # Verifica que alguma nota foi tocada

    def test_change_octave(self):
        initial_octave = self.decoder._Decoder__octave
        self.decoder.change_octave("+")
        self.assertEqual(self.decoder._Decoder__octave, initial_octave + 1)

        self.decoder.change_octave("-")
        self.assertEqual(self.decoder._Decoder__octave, initial_octave)

    def test_change_volume(self):
        initial_volume = self.decoder._Decoder__volume
        self.decoder.change_volume("+")
        self.assertTrue(self.decoder._Decoder__volume > initial_volume)

        self.decoder.change_volume("-")
        self.assertEqual(self.decoder._Decoder__volume, 64)

    def test_decode_basic_notes(self):
        self.midi_file.addNote = MagicMock()  # Mock do método addNote
        text = "C D E F G"
        self.decoder.decode(text)
        # Verifica se 5 notas foram tocadas
        self.assertEqual(self.midi_file.addNote.call_count, 5)

    def test_decode_bpm(self):
        self.midi_file.addTempo = MagicMock()  # Mock do método addTempo
        self.decoder.decode("BPM+")
        self.midi_file.addTempo.assert_called_once()  # Confirma que o BPM foi ajustado

    def test_decode_volume(self):
        self.decoder.decode("+")
        self.assertGreater(self.decoder._Decoder__volume, 64)
        self.decoder.decode("-")
        self.assertEqual(self.decoder._Decoder__volume, 64)

    def test_decode_octave(self):
        initial_octave = self.decoder._Decoder__octave
        self.decoder.decode("R+")
        self.assertEqual(self.decoder._Decoder__octave, initial_octave + 1)
        self.decoder.decode("R-")
        self.assertEqual(self.decoder._Decoder__octave, initial_octave)

    def test_decode_vogais_with_no_current_note(self):
        self.midi_file.addNote = MagicMock()  # Mock do método addNote
        self.decoder.decode("I")
        self.midi_file.addNote.assert_called_once_with(0, 0, 125, 0.0, 1, 64)  # Toca telefone

    def test_decode_vogais_with_current_note(self):
        self.midi_file.addNote = MagicMock()  # Mock do método addNote
        self.decoder.play_note("C")
        self.decoder.decode("I")
        # Verifica se 2 chamadas ao método addNote foram feitas
        self.assertEqual(self.midi_file.addNote.call_count, 2)

    def test_decode_random_instrument(self):
        self.midi_file.addProgramChange = MagicMock()  # Mock do método addProgramChange
        self.decoder.decode("\n")
        self.midi_file.addProgramChange.assert_called_once()

    def test_decode_random_bpm(self):
        self.midi_file.addTempo = MagicMock()  # Mock do método addTempo
        self.decoder.decode(";")
        self.midi_file.addTempo.assert_called_once()

if __name__ == "__main__":
    unittest.main()
