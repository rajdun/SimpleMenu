import unittest
from unittest.mock import patch

from MenuManager import MenuManager, clear_console
import os
from Choices.ExitChoice import ExitChoice
from Choices.SampleChoice import SampleChoice, SampleSubchoice


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.manager = MenuManager()

    def test_add_choice(self):
        # add correct choice
        self.manager.add_choice(ExitChoice)

        self.assertEqual(len(self.manager.choice_list), 1)
        self.assertIsInstance(self.manager.choice_list[0], ExitChoice)

        # add correct choice but instance not class
        self.assertRaises(TypeError, self.manager.add_choice, ExitChoice())

        # add incorrect choice
        self.assertRaises(TypeError, self.manager.add_choice, str)

    def test_draw_menu(self):
        # check empty menu
        self.assertEqual(self.manager.draw_menu(), "")

        # menu with one choice
        self.manager.add_choice(ExitChoice)
        self.assertEqual(self.manager.draw_menu(), f"1. {str(ExitChoice())}\n")

        self.manager.add_choice(SampleChoice)

        # menu with two choices
        val = f"1. {str(ExitChoice())}\n2. {str(SampleChoice())}\n"
        self.assertEqual(self.manager.draw_menu(), val)

        # menu with two choices and selected choice has subchoices
        val += f" 1. {str(SampleSubchoice())}\n"
        val = "0. Powrót\n" + val
        self.manager.get_choice('2')
        self.assertEqual(self.manager.draw_menu(), val)

        # menu with two choices and no selected one
        self.manager.get_choice("0")
        val = f"1. {str(ExitChoice())}\n2. {str(SampleChoice())}\n"
        self.assertEqual(self.manager.draw_menu(), val)

        self.manager.last_message = "Test"
        val = f"1. {str(ExitChoice())}\n2. {str(SampleChoice())}\n\nTest"

        self.assertEqual(self.manager.draw_menu(), val)

    def test_get_choice(self):
        self.manager.add_choice(ExitChoice)  # 1
        self.manager.add_choice(SampleChoice)  # 2

        # correct choice
        self.manager.get_choice("1")
        self.assertIsInstance(self.manager.current_choice, ExitChoice)
        self.manager.current_choice = None

        # select choice with subchoices
        self.manager.get_choice("2")
        self.assertIsInstance(self.manager.current_choice, SampleChoice)
        self.manager.get_choice("1")
        self.assertIsInstance(self.manager.current_choice, SampleSubchoice)
        self.manager.current_choice = None

        # select option 0 when subchoice is selected
        self.manager.get_choice('2')
        self.manager.get_choice("0")
        self.assertIsNone(self.manager.current_choice)
        self.manager.current_choice = None

        # select invalid arguments
        self.assertEqual(self.manager.get_choice("asd"), "Wartość musi być liczbą.")
        self.assertEqual(self.manager.get_choice("-1"), "Wybór nie może być niższy niż 0.")
        self.assertEqual(self.manager.get_choice("3"), "Wybór nie może być spoza zakresu.")

        self.manager.get_choice("2")
        self.assertEqual(self.manager.get_choice("asd"), "Wartość musi być liczbą.")
        self.assertEqual(self.manager.get_choice("-1"), "Wybór nie może być niższy niż 0.")
        self.assertEqual(self.manager.get_choice("2"), "Wybór nie może być spoza zakresu.")

        self.manager.last_message = "Test"
        self.assertEqual(self.manager.get_choice("0"), "Test")

    def test_execute_choice(self):
        self.manager.add_choice(ExitChoice)  # 1
        self.manager.add_choice(SampleChoice)  # 2

        self.manager.get_choice(1)
        self.manager.execute_choice()
        self.assertEqual(self.manager.is_running, False)

        self.manager.current_choice = None

        self.manager.get_choice(2)
        self.assertIsNone(self.manager.execute_choice())

        self.manager.get_choice(1)
        self.manager.execute_choice()
        self.assertEqual(self.manager.last_message, "Testowo")

    def test_clear_console(self):
        with patch("os.system") as mock_system:
            os.name = "nt"
            clear_console()
            mock_system.assert_called_with("cls")

            os.name = ""
            clear_console()
            mock_system.assert_called_with("clear")

if __name__ == '__main__':
    unittest.main()
