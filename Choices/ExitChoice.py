from Choices.BaseChoice import BaseChoice


class ExitChoice(BaseChoice):
    def execute(self, args) -> str:
        raise KeyboardInterrupt()

    def __str__(self):
        return "Zamknij"
