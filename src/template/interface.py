from kivy.app import App
# from ..composer import Composer
# from ..reader import Reader

class Interface(App):
    __is_loading = False
    __instrument_input = 0
    __bpm_input = 0
    __text_input = ''
    __file_input = ''

    def __get_loading(self):
        return self.__is_loading

    def __set_loading(self, loading):
        self.__disable_button() if loading else self.__enable_button()

        self.__is_loading = loading

    def __disable_button(self):
        self.root.ids.main_button.disabled = True

    def __enable_button(self):
        self.root.ids.main_button.disabled = False

    def __get_instrument(self):
        instrument = self.root.ids.instrument.text

        if not instrument.isnumeric():
            print("Error reading instrument!")
            return

        self.__instrument_input = int(instrument)

    def __get_bpm(self):
        bpm = self.root.ids.bpm.text

        if not bpm.isnumeric():
            print("Error reading BPM!")
            return

        self.__bpm_input = int(bpm)

    def __get_text(self):
        self.__text_input = self.root.ids.text.text

    def __get_file(self):
        self.__file_input = self.root.ids.file.selection[0] if len(self.root.ids.file.selection) == 1 else ''

    # def generate(self):
    #     self.__get_instrument()
    #     self.__get_bpm()
    #     self.__get_text()
    #     self.__get_file()

    #     self.__set_loading(True)

    #     file_text = ''

    #     if (self.__file_input != ''):
    #         reader = Reader(self.__file_input)
    #         file_text = reader.read_file()

    #     generate_input = self.__text_input + file_text

    #     composer = Composer(generate_input, self.__bpm_input, self.__instrument_input)

    #     composer.compose()

    #     self.__set_loading(False)
