import os
from Choices.BaseChoice import BaseChoice


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class MenuManager:
    def __init__(self):
        self.choice_list = []
        self.last_message = str()
        self.current_choice = None
        self.is_running = True

    def add_choice(self, choice) -> None:
        if not issubclass(choice, BaseChoice):
            raise TypeError()
        self.choice_list.append(choice())

    def draw_menu(self) -> str:
        menu = ""

        if self.current_choice is not None:
            menu += "0. Powrót\n"

        for i, choice in enumerate(self.choice_list):
            menu += f"{i + 1}. {str(choice)}\n"
            if choice == self.current_choice:
                menu += self.current_choice.draw_subchoices()
        if self.last_message != "":
            menu += "\n" + self.last_message

        return menu

    def get_choice(self, input_value: str) -> str:
        try:
            choice = int(input_value)
        except ValueError:
            return "Wartość musi być liczbą."

        if choice == 0:
            self.current_choice = None
            return self.last_message

        if choice < 0:
            return "Wybór nie może być niższy niż 0."

        if self.current_choice is None:
            return self.get_choice_from_list(choice, self.choice_list)
        else:
            return self.get_choice_from_list(choice, self.current_choice.sub_choices)

    def get_choice_from_list(self, input_choice: int, choice_list) -> str:
        if input_choice > len(choice_list):
            return "Wybór nie może być spoza zakresu."

        next_choice = choice_list[input_choice - 1]
        self.current_choice = next_choice
        return ""

    def execute_choice(self) -> None:
        if len(self.current_choice.sub_choices) > 0:
            return

        try:
            self.last_message = self.current_choice.execute([])
        except KeyboardInterrupt:
            self.is_running = False
        self.current_choice = None

    def run(self) -> None:
        if len(self.choice_list) == 0:
            raise ValueError()

        while self.is_running:
            clear_console()
            print(self.draw_menu())
            input_value = input(">")
            self.last_message = self.get_choice(input_value)
            if self.last_message == "" and self.current_choice is not None:
                self.execute_choice()
