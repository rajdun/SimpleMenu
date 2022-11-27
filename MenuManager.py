import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class MenuManager:
    choice_list = []
    last_message = str()
    current_choice = None
    is_running = True

    def add_choice(self, choice) -> None:
        self.choice_list.append(choice())

    def draw_menu(self) -> None:
        if self.current_choice is not None:
            print("0. Powrót")

        for i, choice in enumerate(self.choice_list):
            print(f"{i + 1}. {str(choice)}")
            if choice == self.current_choice:
                self.current_choice.draw_subchoices()
        print()
        if self.last_message != "":
            print(self.last_message)

    def get_choice(self, input_value: str) -> str:
        try:
            choice = int(input_value)
        except ValueError:
            return "Wartość misu być liczbą."

        if choice == 0:
            self.current_choice = None
            return self.current_choice

        if choice < 0:
            return "Wybór nie może być niższy niż 0."

        if self.current_choice is None:
            return self.get_choice_from_list(choice, self.choice_list)
        else:
            return self.get_choice_from_list(choice, self.current_choice.sub_choices)

    def get_choice_from_list(self, input_choice: int, choice_list) -> str:
        if input_choice > len(choice_list):
            return "Wybór nie może być spoza zakresu."

        next_choice = choice_list[input_choice-1]
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
        while self.is_running:
            clear_console()
            self.draw_menu()
            input_value = input(">")
            self.last_message = self.get_choice(input_value)
            if self.last_message == "" and self.current_choice is not None:
                self.execute_choice()
