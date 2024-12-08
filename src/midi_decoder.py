
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
harpas = ["I", "i", "O", "o", "U", "u"]

class Decoder:
    """
    Objeto usado para decodificar uma nota MIDI
    """
    def __init__(self):
        self.__nota_atual = 'A#'

    def __get_instrument(self, note, instrument):
        if note == "!":
            return 113
        elif note in harpas:
            return 6
        elif note == "\n":
            return 14
        elif note == ";":
            return 75
        elif note == ",":
            return 19
        elif note.isnumeric():
            new_instrument = instrument + int (note)
            new_instrument = new_instrument if new_instrument < 127 else 0

            return new_instrument

    def play_instrument(self, note, instrument, output):
        new_instrument = self.__get_instrument(note, instrument)

        self.__nota_atual = "A#"

        return new_instrument

    def repeat_note(self, instrument, octave, volume, escala, output):
        final_note = 10
        if self.__nota_atual != "A#":
            final_note = (octave * escala) + (notes.index(self.__nota_atual))
            self.__nota_atual = "A#"

            output.set_instrument(instrument)
            output.note_on(final_note, volume)

        return final_note

    def play_note(self, note, instrument, octave, volume, escala, output):
        final_note = (octave * escala) + (notes.index(note))
        self.__nota_atual = note
        
        output.set_instrument(instrument)
        output.note_on(final_note, volume)

        return final_note