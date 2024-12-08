import random
import pygame
import pygame.midi
from midiutil import MIDIFile
from decoder import Decoder
import time
import mido

class Player:
    def __init__(self, text, bpm, instrument):
        self.__text = text
        self.__bpm = int(bpm)
        self.__instrument = int(instrument)
        self.__volume = 50
        self.__octave = 0
        self.__track = 0
        self.__channel = 0
        self.__time = 0

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
        midi_file = MIDIFile(1)
        midi_file.addTempo(self.__track, self.__time, self.__bpm)
        midi_file.addProgramChange(self.__track, self.__channel, self.__time, self.__instrument)

        decoder = Decoder(midi_file, self.__instrument, self.__bpm)

        midi_filename = "output.mid"

        midi_file = decoder.decode(self.__text)

        with open(midi_filename, "wb") as midi_out:
            midi_file.writeFile(midi_out)

        pygame.init()
        pygame.mixer.music.load(midi_filename)
        pygame.mixer.music.play()
