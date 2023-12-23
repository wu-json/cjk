from config import LANGUAGES, FLAGS
from enum import Enum
from graphics import print_line
from prompts import get_translated_word
from yaspin import yaspin
from yaspin.spinners import Spinners
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
                    print_line(thick=True)
                    print(word)
                    print_line()
                    translations = []
                    for lang in LANGUAGES:
                        with yaspin(
                            text=f'translating "{word}" to {lang}', color="green"
                        ) as spinner:
                            translation = get_translated_word(word, lang)
                            translations.append(translation)
                            success_emoji = (
                                FLAGS[lang] if FLAGS[lang] is not None else "✅"
                            )
                            spinner.ok(success_emoji)

                    for i, lang in enumerate(LANGUAGES):
                        print_line()
                        emoji = FLAGS[lang] if FLAGS[lang] is not None else "✅"
                        print(f"{lang} {emoji}")
                        print(translations[i])

                    print_line()

                    self.state = CjkProgramState.SelectAction.value
