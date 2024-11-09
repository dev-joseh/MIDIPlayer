
class MidiController:
    """
    - Interface entre a lógica MIDI e a GUI.
    - Coordena as funções de reprodução do player MIDI com a atualização da interface
    """
    def __init__(self, midi_player, state_manager):
        self.midi_player = midi_player  # Instância do player MIDI
        self.state_manager = state_manager  # Instância do StateManager para controle de estado

    def play(self):
        """Inicia a reprodução do MIDI."""
        if self.state_manager.is_stopped() or self.state_manager.is_paused():
            self.midi_player.start()  # Função que inicia o player
            self.state_manager.set_state("playing")

    def pause(self):
        """Pausa a reprodução do MIDI."""
        if self.state_manager.is_playing():
            self.midi_player.pause()  # Função que pausa o player
            self.state_manager.set_state("paused")

    def stop(self):
        """Para a reprodução do MIDI."""
        if not self.state_manager.is_stopped():
            self.midi_player.stop()  # Função que para o player
            self.state_manager.set_state("stopped")
