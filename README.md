## About
Simplemenu was made for people who are looking for an easy way to create lightweight scripts which can be run from user friendly menu and command line arguments.

## Usage
SimpleMenu lets you create two types of executable scripts. First one is command line argument based. The second one is easier to read menu choice. Of course, you have an option to combine these options into one. 

### Arguments

First You need to create new class inheriting from Argumentable. Then fill empty fields `arg`, `alias` and run your logic in `execute()` method.
See example below.
```python
class SampleSubchoice(Argumentable):
    arg = "--sample"
    alias = "-s"
    help = "Przykladowa komenda"

    def execute(self, args) -> str:
        if len(args) > 0:
            return " ".join(args)
        return "Testowo"
```
If your program is executed from command line with first argument matching `arg` or `alias` then `args` parameter is set to the list of said arguments excluding the first one.

### Menu

Just like before let's start with creating a new class inheriting from BaseChoice. The simplest choices require you to override only `execute()` and `__str__()` methods. After your choice is configured the way you want you have to register it in `main.py` file by using `MenuManager.add_choice()`. See example below
```python
class ExitChoice(BaseChoice):
    def execute(self, args) -> str:
        raise KeyboardInterrupt()

    def __str__(self):
        return "Zamknij"
```
A choice can have its own sub-choices. To set up sub-choices you just neet to override `register_subchoices()` and append new class inheriting from `BaseChoice` to `sub_choices` parameter. See example below
```python
class SampleChoice(BaseChoice):
    def execute(self, args) -> str:
        pass

    def register_subchoices(self) -> None:
        sub_choice = SampleSubchoice(indent=self.indent)

        self.sub_choices.append(sub_choice)

    def __str__(self):
        return "Testowa opcja z podopcjami"


class SampleSubchoice(BaseChoice):
    is_subchoice = True

    def execute(self, args) -> str:
        if len(args) > 0:
            return " ".join(args)
        return "Testowo"

    def __str__(self):
        return "Pod opcja"
```