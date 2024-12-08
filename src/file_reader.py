class Reader:
    __text = ''

    def __init__(self, file):
        self.__file = file

    def __file_is_txt(self):
        return self.__file.endswith('.txt') 

    def __get_text(self):
        return self.__text
    
    def __set_text(self, text):
        self.__text = text

    def read_file(self):
        try:
            if (self.__file_is_txt()):
                with open(self.__file, 'r') as f:
                    self.__set_text(f.read())
            else:
                print("Only txt files are allowed")

        except IOError:
            print("Could not read file: ", self.__file)

        return self.__get_text()