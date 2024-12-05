class Reader:
    def __init__(self, file):
        self.__file = file

    def __file_is_txt(self):
        return self.__file.endswith('.txt')

    def read_file(self):
        if (not self.__file_is_txt()):
            print('Error opening file!')
            return ''

        fl = open(self.__file, 'r')

        text = fl.read()

        return text