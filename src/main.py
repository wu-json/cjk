from graphics import CJK_ASCII_ART, print_line


def print_welcome_message():
    """Prints the welcome message when CJK is first opened."""
    print_line(thick=True)
    print(CJK_ASCII_ART)
    print_line(thick=True)
    print(
        "Welcome to CJK! This is an LLM-powered command line tool for learning words in 中文,日本語、and 한국어 all at once!"
    )
    print_line()


def main():
    print_welcome_message()


if __name__ == "__main__":
    main()
