from config import LANGUAGES
from enum import Enum
from graphics import print_line
from multiprocessing import Pool
from prompts import get_translated_word
import inquirer


class CjkProgramState(Enum):
    SelectAction = 0
    SelectWord = 1


class CjkProgram:
    def __init__(self):
        self.state = CjkProgramState.SelectAction.value

    def start(self):
        while True:
            if self.state == CjkProgramState.SelectAction.value:
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
                    self.state = CjkProgramState.SelectWord.value
                elif answers["action"] == "Quit":
                    break

            elif self.state == CjkProgramState.SelectWord.value:
                answers = inquirer.prompt(
                    [
                        inquirer.Text(
                            "word", message="What word do you want to translate?"
                        )
                    ]
                )
                if answers is None:
                    break
                else:
                    word = answers["word"]

                    def get_translation(lang: str):
                        return get_translated_word(word, lang)

                    pool = Pool(processes=3)
                    res = pool.map(get_translation, LANGUAGES)

                    print(res)

                    print("end")
                    self.state = CjkProgramState.SelectAction.value
