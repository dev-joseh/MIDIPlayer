import pygame
import pygame.midi
import mido
from midiutil import MIDIFile
from midi_decoder import Decoder
# from midi_decoder_gica import Decoder

# Se caractere anterior era NOTA (A a G), repete nota; Caso contrário, fazer som de “Telefone tocando” (125)
telephone = ["I", "i", "O", "o", "U", "u"]
notes = ["C", "D", "E", "F", "G", "A", "B"]

class Player:
    def __init__(self, text, bpm, instrument):
        self.__text = text
        self.__bpm = int(bpm)
        self.__instrument = int(instrument)

        self.__volume = 50
        self.__octave = 5
        self.__track = 0
        self.__channel = 0
        self.__time = 0
        self.__duration = 1
        self.__player = Decoder()

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
        return self.__increase_octave
    
    def __double_volume(self):
        self.__volume *= 2

        if self.__volume > 127:
            self.__reset_volume()

    def __reset_volume(self):
        self.__volume = 50

    def __increase_octave(self):
        self.__octave += 1

    def __note_exists(self, note):
        return note in notes

    def compose(self):
        midi_file = MIDIFile(1)
        escala = 12
        midi_file.addTempo(self.__track, self.__time, self.__bpm)
        midi_file.addProgramChange(self.__track, self.__channel, self.__time, self.__instrument)

        for note in self.__text:
            volume_atual = self.__volume
            final_note = 0

            # Troca o instrumento sem tocar nada e continua o loop
            if note == "!" or note in telephone or note == "\n" or note == ";" or note == "," or note.isnumeric():
                self.__instrument = self.__player.play_instrument(note, self.__instrument)
                midi_file.addProgramChange(self.__track, self.__channel, self.__time, self.__instrument)
                self.__time += 1

            if self.__note_exists(note):
                final_note = self.__player.play_note(note, self.__instrument, self.__octave, volume_atual, escala)
            else:
                # Senão, repete a ultima nota
                final_note = self.__player.repeat_note(self.__instrument, self.__octave, volume_atual, escala)
            
            midi_file.addNote(self.__track, self.__channel, final_note, self.__time, self.__duration, volume_atual)
            self.__time += 1

        output_file = "output/output.mid"

        with open(output_file, "wb") as output_file:
            midi_file.writeFile(output_file)

        pygame.init()
        pygame.mixer.music.load("output/output.mid")
        pygame.mixer.music.play()