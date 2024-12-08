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
        self.__duration = 1

    def get___bpm(self):
        return self.__bpm

    def set___bpm(self, __bpm):
        self.__bpm = __bpm

    def get_instrument(self):
        return self.__instrument

    def compose(self):

        # Inicializa a saída MIDI
        pygame.midi.init()
        output_id = pygame.midi.get_default_output_id()
        saida_midi = pygame.midi.Output(output_id)
        midi_file = MIDIFile(1)
        escala = 12
        midi_file.addTempo(self.__track, self.__time, self.__bpm)
        midi_file.addProgramChange(self.__track, self.__channel, self.__time, self.__instrument)

        # Teste da classe
        decoder = Decoder(midi_file, self.__instrument, self.__bpm)

        midi_filename = "output.mid"

        # Decodificando e tocando o MIDI
        midi_file = decoder.decode(self.__text)

        with open(midi_filename, "wb") as midi_out:
            midi_file.writeFile(midi_out)

        pygame.midi.quit()
        pygame.init()
        pygame.mixer.music.load(midi_filename)
        pygame.mixer.music.play()
