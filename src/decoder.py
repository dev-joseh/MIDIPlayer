import random
from midiutil import MIDIFile

# Mapping
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
vogais = ["I", "i", "O", "o", "U", "u"]
default_volume = 64

class Decoder:
    def __init__(self, midi_file, instrument=0, bpm=120):
        self.__midi_file = midi_file 
        self.__track = 0  
        self.__instrument = instrument  
        self.__bpm = bpm  
        self.__time = 0.0  # Initial time
        self.__octave = 5  # Default octave
        self.__volume = default_volume 
        self.__current_note = None  

    def play_note(self, note):
        final_note = (self.__octave * 12) + notes.index(note)
        self.__current_note = note
        self.__midi_file.addNote(self.__track, 0, final_note, self.__time, 1, self.__volume)
        self.__time += 1  

    def play_telefone(self):
        self.__midi_file.addNote(self.__track, 0, 125, self.__time, 1, self.__volume)
        self.__time += 1

    def change_octave(self, direction):
        if direction == "+":
            self.__octave += 1
        elif direction == "-":
            self.__octave -= 1

    def change_volume(self, direction):
        if direction == "+":
            self.__volume = min(self.__volume * 2, 127)
        elif direction == "-":
            self.__volume = default_volume

    def random_note(self):
        random_note = random.choice(notes)
        self.play_note(random_note)

    def decode(self, text):
        next_char = 0
        while next_char < len(text):
            if text[next_char:next_char + 4] == "BPM+":
                self.__bpm = min(self.__bpm + 80, 300)
                self.__midi_file.addTempo(self.__track, self.__time, self.__bpm)
                next_char += 4

            elif text[next_char] in "abcdefgABCDEFG":
                self.play_note(text[next_char].upper())
                next_char += 1

            elif text[next_char] == " ":
                self.__time += 1
                next_char += 1

            elif text[next_char] in "+-":
                self.change_volume(text[next_char])
                next_char += 1

            elif text[next_char:next_char+2] == "R+" or text[next_char:next_char+2] == "R-":
                self.change_octave(text[next_char+1])
                next_char += 2

            elif text[next_char] in vogais:
                if self.__current_note:
                    self.play_note(self.__current_note)
                else:
                    self.play_telefone()

                next_char += 1
            elif text[next_char] == "?":
                self.random_note()
                next_char += 1

            elif text[next_char] == "\n":
                self.__instrument = random.randint(0, 127)
                self.__midi_file.addProgramChange(self.__track, 0, self.__time, self.__instrument)
                next_char += 1

            elif text[next_char] == ";":
                self.__bpm = random.randint(60, 180)
                self.__midi_file.addTempo(self.__track, self.__time, self.__bpm)
                next_char += 1
            else:
                next_char += 1

        return self.__midi_file
