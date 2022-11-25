from Choices.BaseChoice import BaseChoice


class SampleSubchoice(BaseChoice):
    is_subcommand = True
    def execute(self) -> str:
        return "Testowe"

    def __str__(self):
        return "Pod opcja"
