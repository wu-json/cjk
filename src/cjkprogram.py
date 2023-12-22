from enum import Enum
import inquirer


class CjkProgramState(Enum):
    SelectOption = 0


class CjkProgram:
    def __init__(self):
        self.state = CjkProgramState.SelectOption.value

    def start(self):
        if self.state == CjkProgramState.SelectOption.value:
            while True:
                questions = [
                    inquirer.List(
                        "action",
                        message="What do you want to do?",
                        choices=["Learn random word", "Quit"],
                    )
                ]
                answers = inquirer.prompt(questions)
                if answers is None:
                    break
                elif answers["action"] == "Learn random word":
                    print("hello")
                elif answers["action"] == "Quit":
                    break
