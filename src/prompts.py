from gpt4all import GPT4All

model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")


def get_translated_word(word: str, language: str):
    return model.generate(
        f"""
        [INST]translate "{word}" to {language}, and give an example sentence using "{word}" in {language}. include english translation of the example sentence.[/INST]
        """,
        max_tokens=500,
    )
