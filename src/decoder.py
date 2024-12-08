import random
import mido
import pygame.midi
import time

# Notas e mapeamentos 
## REVER ##
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
vogais = ["I", "i", "O", "o", "U", "u"]

class Decoder:
    def __init__(self):
        self.__nota_atual = 'A'
        self.__volume = 64  # Volume padrão
        self.__octave = 5  # Octava padrão
        self.__instrument = 0  # Instrumento padrão (Piano)
        self.__tempo = 120  # BPM padrão
        self.__midi_file = None  # Arquivo MIDI
        self.__track = None  # Track para adicionar os eventos MIDI
        self.__last_note_time = 0  # Variável para controlar o tempo de execução das notas

    def play_note(self, note):
        final_note = (self.__octave * 12) + notes.index(note)
        self.__nota_atual = note
        self.__track.append(mido.Message('note_on', note=final_note, velocity=self.__volume, time=0))
        self.__track.append(mido.Message('note_off', note=final_note, velocity=self.__volume, time=500))  # Duração fixa para a nota

    def play_telefone(self):
        # Toca o som do telefone (nota MIDI 125)
        self.__track.append(mido.Message('note_on', note=125, velocity=100, time=self.__current_time))
        self.__track.append(mido.Message('note_off', note=125, velocity=100, time=self.__current_time + 500))  # Define a duração da nota

    def change_octave(self, direction):
        if direction == "+":
            self.__octave += 1
        elif direction == "-":
            self.__octave -= 1

    def change_volume(self, direction):
        if direction == "+":
            self.__volume *= 2
        elif direction == "-":
            self.__volume = 64  # Volume padrão

    def random_note(self):
        random_note = random.choice(notes)
        self.play_note(random_note)

    def decode(self, text, output, midi_filename):
        self.__midi_file = mido.MidiFile()  # Novo arquivo MIDI
        self.__track = mido.MidiTrack()  # Nova track dentro do arquivo MIDI
        self.__midi_file.tracks.append(self.__track)

        # Configurar o tempo (BPM)
        tempo = mido.bpm2tempo(self.__tempo)
        self.__track.append(mido.MetaMessage('set_tempo', tempo=tempo))

        # Calculando o intervalo entre as notas baseado no BPM
        interval = 60 / self.__tempo  # Tempo entre notas, em segundos (de acordo com o BPM)

        i = 0  # Variável para iterar pelos caracteres
        while i < len(text):
            if text[i:i+4] == "BPM+":
                # Quando encontrar "BPM+", aumenta o BPM
                self.__tempo = min(self.__tempo + 80, 300)  # Limita o BPM máximo a 300
                tempo = mido.bpm2tempo(self.__tempo)
                self.__track.append(mido.MetaMessage('set_tempo', tempo=tempo))
                interval = 60 / self.__tempo  # Atualiza o intervalo entre notas
                i += 4  # Pula os 4 caracteres "BPM+"
            elif text[i] in "abcdefgABCDEFG":
                # Toca a nota correspondente e adiciona ao arquivo MIDI
                self.play_note(text[i].upper())
                #time.sleep(interval)  # Espera para tocar a próxima nota
                i += 1  # Passa para o próximo caractere
            elif text[i] == " ":
                # Silêncio, adiciona pausa no MIDI
                self.__track.append(mido.Message('note_off', note=0, velocity=0, time=int(interval * 1000)))
                i += 1  # Passa para o próximo caractere
            elif text[i] == "+" or text[i] == "-":
                # Modifica o volume
                self.change_volume(text[i])
                i += 1
            elif text[i:i+2] == "R+" or text[i:i+2] == "R-":
                # Modifica a oitava
                self.change_octave(text[i+1])
                i += 2
            elif text[i] in vogais:
                if text[i-1] in "abcdefgABCDEF":
                    # Se o caractere anterior era uma nota (A a G), repete a nota
                    self.play_note(self.__nota_atual)
                else:
                    # Caso contrário, toca o som do telefone (nota 125)
                    self.play_telefone()
                i += 1
            elif text[i] == "?":
                # Tocar uma nota aleatória
                self.random_note()
                #time.sleep(interval)
                i += 1
            elif text[i] == "\n":
                # Trocar instrumento
                self.__instrument = random.randint(0, 128)
                i += 1
            elif text[i] == ";":
                # Atribui valor aleatório à BPM
                self.__tempo = random.randint(60, 180)
                interval = 60 / self.__tempo  # Atualiza o intervalo entre notas
                i += 1
            elif text[i].isnumeric():
                # Mudar instrumento (ajustado conforme descrito)
                self.__instrument = int(text[i])
                i += 1
            else:
                # Ignora caracteres desconhecidos
                i += 1

        # Salva o arquivo MIDI
        self.__midi_file.save(midi_filename)
