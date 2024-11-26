import pygame.midi #importada mesmo sem ser usada para ter o SDL correto
from kivy.app import App
from template.interface import Interface

class Beethoven():
    def main(self):
        interface = Interface()
        interface.run()

if __name__ == "__main__":
    bee = Beethoven()
    bee.main()
