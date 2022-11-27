from MenuManager import MenuManager
import os
import Choices
from sys import argv

MODULES_DIRECTORY = "Choices"
MODULES_PATH = os.path.join(os.getcwd(), MODULES_DIRECTORY)

def main():
    manager = MenuManager()

    manager.add_choice(Choices.SampleChoice)
    manager.add_choice(Choices.ExitChoice)

    manager.run()

if __name__ == "__main__":
    if Choices.ARGUMENT is not None:
        print(Choices.ARGUMENT().execute(argv[2:]))

    else:
        main()
