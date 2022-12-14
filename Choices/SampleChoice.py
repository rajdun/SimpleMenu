from Choices.BaseChoice import BaseChoice
from Choices.SampleSubchoice import SampleSubchoice


class SampleChoice(BaseChoice):
    def execute(self, args) -> str:
        pass

    def register_subchoices(self) -> None:
        self.sub_choices.append(SampleSubchoice())

    def __str__(self):
        return "Testowa opcja z podopcjami"
