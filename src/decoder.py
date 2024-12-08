import random
from midiutil import MIDIFile

# Notas e mapeamentos
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
vogais = ["I", "i", "O", "o", "U", "u"]

class Decoder:
    def __init__(self, midi_file, instrument=0, bpm=120):
        """Inicializa a classe com um arquivo MIDI existente."""
        self.__midi_file = midi_file  # O MIDIFile existente
        self.__track = 0  # Track única (pode ser ajustado conforme necessário)
        self.__instrument = instrument  # Instrumento padrão
        self.__tempo = bpm  # BPM padrão
        self.__time = 0.0  # Tempo inicial em batidas
        self.__octave = 5  # Oitava padrão
        self.__volume = 64  # Volume padrão
        self.__nota_atual = None  # Nota atual (para repetir)

    def play_note(self, note):
        """Toca uma nota específica."""
        final_note = (self.__octave * 12) + notes.index(note)
        self.__nota_atual = note
        self.__midi_file.addNote(self.__track, 0, final_note, self.__time, 1, self.__volume)
        self.__time += 1  # Avança o tempo em 1 batida

    def play_telefone(self):
        """Toca o som do telefone (nota MIDI 125)."""
        self.__midi_file.addNote(self.__track, 0, 125, self.__time, 1, self.__volume)
        self.__time += 1

    def change_octave(self, direction):
        """Muda a oitava."""
        if direction == "+":
            self.__octave += 1
        elif direction == "-":
            self.__octave -= 1

    def change_volume(self, direction):
        """Muda o volume."""
        if direction == "+":
            self.__volume = min(self.__volume * 2, 127)
        elif direction == "-":
            self.__volume = 64

    def random_note(self):
        """Toca uma nota aleatória."""
        random_note = random.choice(notes)
        self.play_note(random_note)

    def decode(self, text):
        """Decodifica o texto e adiciona as notas ao arquivo MIDI existente."""
        i = 0
        while i < len(text):
            if text[i:i+4] == "BPM+":
                self.__tempo = min(self.__tempo + 80, 300)
                self.__midi_file.addTempo(self.__track, self.__time, self.__tempo)
                i += 4
            elif text[i] in "abcdefgABCDEFG":
                self.play_note(text[i].upper())
                i += 1
            elif text[i] == " ":
                # Adiciona uma pausa (simula silêncio com incremento de tempo)
                self.__time += 1
                i += 1
            elif text[i] in "+-":
                self.change_volume(text[i])
                i += 1
            elif text[i:i+2] == "R+" or text[i:i+2] == "R-":
                self.change_octave(text[i+1])
                i += 2
            elif text[i] in vogais:
                if self.__nota_atual:
                    self.play_note(self.__nota_atual)
                else:
                    self.play_telefone()
                i += 1
            elif text[i] == "?":
                self.random_note()
                i += 1
            elif text[i] == "\n":
                # Trocar instrumento aleatoriamente
                self.__instrument = random.randint(0, 127)
                self.__midi_file.addProgramChange(self.__track, 0, self.__time, self.__instrument)
                i += 1
            elif text[i] == ";":
                # Define BPM aleatório
                self.__tempo = random.randint(60, 180)
                self.__midi_file.addTempo(self.__track, self.__time, self.__tempo)
                i += 1
            else:
                # Ignora caracteres desconhecidos
                i += 1

        # Retorna o novo MIDIFile com as notas adicionadas
        return self.__midi_file
