from Choices.BaseChoice import BaseChoice
from Choices.Argumentable import Argumentable


class SampleSubchoice(BaseChoice, Argumentable):
    is_subcommand = True
    arg = "--sample"
    alias = "-s"
    help = "Przykladowa komenda"

    def execute(self, args) -> str:
        if len(args) > 0:
            return " ".join(args)
        return "Testowo"

    def __str__(self):
        return "Pod opcja"
