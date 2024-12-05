from kivy.app import App
from file_reader import Reader
from kivy.uix.boxlayout import BoxLayout

class File(BoxLayout):
    __text_input = ''

    def on_file_selected(self, selection):
        print(selection)


class Interface(App):
    __text_input = ''
    __file_input = ''
    __bpm_input = 0
    __instrument_input = 0

    # public
    def get_instrument(self):
        return self.__instrument_input
    
    # private
    def __set_instrument(self, instrument):
        self.__instrument_input = instrument

    def __read_instrument(self):
        self.__set_instrument(int(self.root.ids.instrument_input.text))


    def get_bpm(self):
        return self.__bpm_input
    
    def __set_bpm(self, bpm):
        self.__bpm_input = bpm

    def __read_bpm(self):
        self.__set_bpm(int(self.root.ids.bpm_input.text))


    def get_text(self):
        return self.__text_input
    
    def __set_text(self, text):
        self.__text_input = text

    def __read_text(self):
        self.__set_text(self.root.ids.text_input.text)


    def get_file(self):
        self.__file_input = self.root.ids.file.selection[0] if len(self.root.ids.file.selection) == 1 else ''

    def get_text_from_file(self):
        return self.__text_from_file
    
    def on_file_selected(self, selector):
        print(selector)

    def create(self):  
        self.__read_instrument()
        self.__read_bpm()
        self.__read_text()

        text_from_file = ''
        if (self.__file_input != ''):
            reader = Reader(self.__file_input)
            text_from_file = reader.read_file()

        final_text = text_from_file + self.__text_input