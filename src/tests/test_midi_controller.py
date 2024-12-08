# Testa a mudança de volume, oitava e velocidade
import unittest
from unittest.mock import Mock
from src.controllers.midi_controller import MidiController

class TestMidiController(unittest.TestCase):
    def setUp(self):
        self.midi_player_mock = Mock()
        self.state_manager_mock = Mock()

        self.controller = MidiController(
            midi_player=self.midi_player_mock, 
            state_manager=self.state_manager_mock
        )

    def test_play_starts_player_and_sets_playing_state(self):
        self.state_manager_mock.is_stopped.return_value = True
        self.state_manager_mock.is_paused.return_value = False
        self.controller.play()

        # Verifica se o método start foi chamado no midi_player
        self.midi_player_mock.start.assert_called_once()

        # Verifica se o estado foi alterado para 'playing'
        self.state_manager_mock.set_state.assert_called_once_with("playing")

    def test_pause_pauses_player_and_sets_paused_state(self):
        self.state_manager_mock.is_playing.return_value = True
        self.controller.pause()
        self.midi_player_mock.pause.assert_called_once()

        # Verifica se o estado foi alterado para 'paused'
        self.state_manager_mock.set_state.assert_called_once_with("paused")

    def test_stop_stops_player_and_sets_stopped_state(self):
        self.state_manager_mock.is_stopped.return_value = False
        self.controller.stop()
        self.midi_player_mock.stop.assert_called_once()

        # Verifica se o estado foi alterado para 'stopped'
        self.state_manager_mock.set_state.assert_called_once_with("stopped")

    def test_play_does_not_start_player_if_already_playing(self):
        self.state_manager_mock.is_stopped.return_value = False
        self.state_manager_mock.is_paused.return_value = False
        self.controller.play()

        # Verifica que o método start não foi chamado no midi_player
        self.midi_player_mock.start.assert_not_called()

        # Verifica que o estado não foi alterado
        self.state_manager_mock.set_state.assert_not_called()

if __name__ == '__main__':
    unittest.main()