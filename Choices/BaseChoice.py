class BaseChoice:
    sub_choices = []
    is_subcommand = False
    indent = int()

    def __init__(self, indent=0):
        self.indent = indent+1
        self.register_subchoices()

    def execute(self) -> str:
        pass

    def draw_subchoices(self) -> None:
        space = " "*self.indent

        for i in range(len(self.sub_choices)):
            print(f"{space}{i+1}.{self.sub_choices[i].__str__()}")

    def register_subchoices(self) -> None:
        self.sub_choices = []
