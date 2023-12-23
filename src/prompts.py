from gpt4all import GPT4All

model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")


def get_translated_word(word: str, language: str):
    return model.generate(
        f"""
        [INST]translate "{word}" to {language}[/INST]
        """
    )
