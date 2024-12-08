import random
import pygame
import pygame.midi
from midiutil import MIDIFile
from decoder import Decoder
import time
import mido

harpa = ["I", "i", "O", "o", "U", "u"]
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

class Player:
    def __init__(self, text, bpm, instrument):
        self.__text = text
        self.__bpm = int(bpm)
        self.__instrument = int(instrument)
        self.__volume = 50
        self.__octave = 0
        self.__track = 0
        
    def get___bpm(self):
        return self.__bpm

    def set___bpm(self, __bpm):
        self.__bpm = __bpm

    def get_instrument(self):
        return self.__instrument

    def set_instrument(self, instrument):
        self.__instrument = instrument

    def get_volume(self):
        return self.__volume

    def get_octave(self):
        return self.__octave
    
    def compose(self):

        pygame.midi.init()
        output_id = pygame.midi.get_default_output_id()
        saida_midi = pygame.midi.Output(output_id)

        decoder = Decoder()

        midi_filename = "output.mid"

        decoder.decode(self.__text, saida_midi, midi_filename)

        pygame.midi.quit() 
        pygame.midi.init()

        midi_file = mido.MidiFile(midi_filename)
        output = pygame.midi.Output(output_id)
        for msg in midi_file.play():
            if msg.type == 'note_on':
                output.note_on(msg.note, msg.velocity)
            elif msg.type == 'note_off':
                output.note_off(msg.note, msg.velocity)

        output.close()
        pygame.midi.quit()
