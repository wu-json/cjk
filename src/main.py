from gpt4all import GPT4All


def main():
    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
    output = model.generate("Who is Ichigo Kurosaki", max_tokens=30)
    print(output)


if __name__ == "__main__":
    main()
