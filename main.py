from dictionary import *
from controller import Controller
from console import Console
def run():
    dictionary=DoubleDictionary(0,"original.txt")
    controller=Controller(dictionary)
    console=Console(controller)
    console.run()
    
run()
