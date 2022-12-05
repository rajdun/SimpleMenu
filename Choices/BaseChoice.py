from Choices.Executable import Executable
class BaseChoice(Executable):
    is_subchoice = False
    def __init__(self):
        self.indent = 0
        self.sub_choices = []
        self.indent = int()

        self.register_subchoices()
        for sub_choice in self.sub_choices:
            sub_choice.indent = self.indent+1

    def draw_subchoices(self) -> str:
        if len(self.sub_choices) == 0:
            return ""

        space = " " * (self.indent+1)
        sub_choice = ""

        for i, choice in enumerate(self.sub_choices):
            sub_choice += f"{space}{i+1}. {choice.__str__()}\n"

        return sub_choice

    def register_subchoices(self) -> None:
        pass
