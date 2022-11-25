from Choices.BaseChoice import BaseChoice


class ExitChoice(BaseChoice):
    def execute(self) -> str:
        raise KeyboardInterrupt()

    def __str__(self):
        return "Zamknij"
