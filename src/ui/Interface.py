from kivy.app import App
from file_reader import Reader
from symphonist import Symphonist
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from player import Player

class Interface(BoxLayout, App):
    text_input = StringProperty('AAAAAaaaBBB')
    instrument_input = StringProperty('1')
    bpm_input = StringProperty('120')
    reader = None

    # public
    def get_instrument(self):
        return self.instrument_input
    
    # private
    def set_instrument(self, instrument):
        self.instrument_input = instrument

    def get_bpm(self):
        return self.bpm_input
    
    def set_bpm(self, bpm):
        self.bpm_input = bpm

    def get_text(self):
        return self.text_input
    
    def set_text(self, text):
        self.text_input = text

    # checks if text is not null
    def __sanitize_file_text(self, text):
            return text if text else self.text_input

    def on_file_selected(self, selection):
        self.reader = Reader(selection[0])
        self.text_input = self.__sanitize_file_text(self.reader.read_file())

    def generate_symphony(self):
        # symphonist = Symphonist(text=self.text_input, bpm=self.bpm_input, instrument=self.instrument_input)
        player = Player(text=self.text_input, bpm=self.bpm_input, instrument=self.instrument_input)
        player.compose()

    