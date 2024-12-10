from kivy.app import App
from file_reader import Reader
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from player import Player

class Interface(BoxLayout, App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_input = '2CDEFF F CDCDD D CGFEE E CDEFF F2,CDEFF F CDCDD D CGFEE E CDEFF F,CDEFF F CDCDD D CGFEE E CDEFF F,'
        self.instrument_input = '1'
        self.bpm_input = '120'
        self.reader = None

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
        player = Player(text=self.text_input, bpm=self.bpm_input, instrument=self.instrument_input)
        player.compose()

    