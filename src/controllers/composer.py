import random
import pygame
from midiutil import MIDIFile
from controllers.player import Player
import time

harpa = ["I", "i", "O", "o", "U", "u"]
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

class Composer:
    def __init__(self, text, __bpm, instrument):
        self.__text = text
        self.__bpm = __bpm
        self.__instrument = instrument
        self.__volume = 50
        self.__octave = 0
        self.__track = 0
        self.__channel = 0
        self.__time = 0
        self.__duration = 1
        self.__player = Player()

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

    def __note_exists(self, note):
        return note in notes

    def compose(self):
        pygame.midi.init()
        output = pygame.midi.Output(0)
        escala = 12

        midi_file = MIDIFile(1)

        midi_file.addTempo(self.__track, self.__time, self.__bpm)

        # Set the program change event to the selected instrument
        output.set_instrument(self.__instrument)
        midi_file.addProgramChange(self.__track, self.__channel, self.__time, self.__instrument)

        for note in self.__text:
            volume_atual = self.__volume
            final_note = 0

            # Dobra o volume e continua o loop
            if note == " ":
                self.__double_volume()
                continue
            
            # Aumenta a oitava e continua o loop
            if note == "?" or note == ".":
                self.__increase_octave()
                continue

            # Troca o instrumento sem tocar nada e continua o loop
            if note == "!" or note in harpa or note == "\n" or note == ";" or note == "," or note.isnumeric():
                self.__instrument = self.__player.play_instrument(note, self.__instrument, output)

                output.set_instrument(self.__instrument)
                midi_file.addProgramChange(self.__track, self.__channel, self.__time, self.__instrument)

                time.sleep(60 / self.__bpm)
                self.__time += 1

                continue

            # Se a nota atual existir, toca ela
            if self.__note_exists(note):
                final_note = self.__player.play_note(note, self.__instrument, self.__octave, volume_atual, escala, output)
            # Senão, repete a ultima nota
            else:
                final_note = self.__player.repeat_note(self.__instrument, self.__octave, volume_atual, escala, output)
            
            time.sleep(60 / self.__bpm)
            output.note_off(final_note, 0)

            if final_note == 10:
                volume_atual = 0
            midi_file.addNote(self.__track, self.__channel, final_note, self.__time, self.__duration, volume_atual)

            self.__time += 1

        output_file = "output/output.mid"

        with open(output_file, "wb") as output_file:
            midi_file.writeFile(output_file)

        output.note_off(final_note, 0)

        del output
        pygame.midi.quit()

        pygame.init()
        pygame.mixer.music.load("output/output.mid")
        pygame.mixer.music.play()

    def __double_volume(self):
        self.__volume *= 2

        if self.__volume > 127:
            self.__reset_volume()

    def __reset_volume(self):
        self.__volume = 50

    def __increase_octave(self):
        self.__octave += 1
