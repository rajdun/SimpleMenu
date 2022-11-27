from Choices.Executable import Executable
class BaseChoice(Executable):
    sub_choices = []
    is_subcommand = False
    indent = int()

    def __init__(self, indent=0):
        self.indent = indent+1
        self.register_subchoices()

    def draw_subchoices(self) -> None:
        space = " "*self.indent

        for i, choice in enumerate(self.sub_choices):
            print(f"{space}{i+1}.{choice.__str__()}")

    def register_subchoices(self) -> None:
        self.sub_choices = []
