from gpt4all import GPT4All

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")


def get_random_word():
    random_word = model.generate(prompt="give me a word")
    print("rando")
    print(random_word)
    return random_word
