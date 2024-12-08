import random
import mido

# Mapping
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
vogais = ["I", "i", "O", "o", "U", "u"]

class Decoder:
    def __init__(self):
        self.__nota_atual = 'A'
        self.__volume = 64  # default volume
        self.__octave = 5  # default octave
        self.__instrument = 0  # default instrument (piano)
        self.__tempo = 120  # default BPM
        self.__midi_file = None 
        self.__track = None 

    def play_note(self, note):
        final_note = (self.__octave * 12) + notes.index(note)
        self.__nota_atual = note
        self.__track.append(mido.Message('note_on', note=final_note, velocity=self.__volume, time=0))
        self.__track.append(mido.Message('note_off', note=final_note, velocity=self.__volume, time=500))  

    def play_telefone(self):
        self.__track.append(mido.Message('note_on', note=125, velocity=100, time=self.__current_time))
        self.__track.append(mido.Message('note_off', note=125, velocity=100, time=self.__current_time + 500)) 
    
    def change_octave(self, direction):
        if direction == "+":
            self.__octave += 1
        elif direction == "-":
            self.__octave -= 1

    def change_volume(self, direction):
        if direction == "+":
            self.__volume *= 2
        elif direction == "-":
            self.__volume = 64  

    def random_note(self):
        random_note = random.choice(notes)
        self.play_note(random_note)

    def decode(self, text, output, midi_filename):
        self.__midi_file = mido.MidiFile()  
        self.__track = mido.MidiTrack() 
        self.__midi_file.tracks.append(self.__track)

        tempo = mido.bpm2tempo(self.__tempo)
        self.__track.append(mido.MetaMessage('set_tempo', tempo=tempo))

        interval = 60 / self.__tempo  

        nextCharacter = 0 
        while nextCharacter < len(text):
            if text[nextCharacter:nextCharacter+4] == "BPM+":
                self.__tempo = min(self.__tempo + 80, 300)
                tempo = mido.bpm2tempo(self.__tempo)
                self.__track.append(mido.MetaMessage('set_tempo', tempo=tempo))
                interval = 60 / self.__tempo  
                nextCharacter += 4  
            elif text[nextCharacter] in "abcdefgABCDEFG":
                self.play_note(text[nextCharacter].upper())
                nextCharacter += 1 
            elif text[nextCharacter] == " ":
                self.__track.append(mido.Message('note_off', note=0, velocity=0, time=int(interval * 1000)))
                nextCharacter += 1  
            elif text[nextCharacter] == "+" or text[nextCharacter] == "-":
                self.change_volume(text[nextCharacter])
                nextCharacter += 1
            elif text[nextCharacter:nextCharacter+2] == "R+" or text[nextCharacter:nextCharacter+2] == "R-":
                self.change_octave(text[nextCharacter+1])
                nextCharacter += 2
            elif text[nextCharacter] in vogais:
                if text[nextCharacter-1] in "abcdefgABCDEF":
                    self.play_note(self.__nota_atual)
                else:
                    self.play_telefone()
                nextCharacter += 1
            elif text[nextCharacter] == "?":
                self.random_note()
                nextCharacter += 1
            elif text[nextCharacter] == "\n":
                self.__instrument = random.randint(0, 128)
                nextCharacter += 1
            elif text[nextCharacter] == ";":
                self.__tempo = random.randint(60, 180)
                interval = 60 / self.__tempo
                nextCharacter += 1
            elif text[nextCharacter].isnumeric():
                self.__instrument = int(text[nextCharacter])
                nextCharacter += 1
            else:
                nextCharacter += 1

        self.__midi_file.save(midi_filename)
