from enum import Enum
import inquirer


class CjkProgramState(Enum):
    SelectOption = 0


class CjkProgram:
    def __init__(self):
        self.state = CjkProgramState.SelectOption.value

    def start(self):
        while True:
            if self.state == CjkProgramState.SelectOption.value:
                answers = inquirer.prompt(
                    [
                        inquirer.List(
                            "action",
                            message="What do you want to do?",
                            choices=["Translate word", "Quit"],
                        )
                    ]
                )
                if answers is None:
                    break
                elif answers["action"] == "Translate word":
                    print("would have translated word here")
                elif answers["action"] == "Quit":
                    break
