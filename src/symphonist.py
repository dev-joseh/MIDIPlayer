class Symphonist():
    def __init__(self, text, bpm, instrument) -> None:
        self.__text = text
        self.__bpm = bpm
        self.__instrument = instrument

        print(self.__text, self.__bpm, self.__instrument)