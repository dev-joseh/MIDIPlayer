# Importa as principais classes e funções para fácil acesso ao pacote
from .midi_loader import MidiLoader
from .midi_decoder import MidiPlayer
from .midi_events import MidiEvents

# Exponha apenas o que é necessário para outros módulos
__all__ = ["MidiLoader", "MidiPlayer", "MidiEvents"]
