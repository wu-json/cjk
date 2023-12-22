import os

CJK_ASCII_ART = r"""
 ______       __     __  __    
/\  ___\     /\ \   /\ \/ /    
\ \ \____   _\_\ \  \ \  _"-.  
 \ \_____\ /\_____\  \ \_\ \_\ 
  \/_____/ \/_____/   \/_/\/_/ 
"""


def print_line(thick=False):
    """Print a separating line across the whole width of the terminal."""
    width = os.get_terminal_size().columns
    char = "=" if thick else "-"
    print(char * width)


def print_welcome_message():
    """Prints the welcome message when CJK is first opened."""
    print_line(thick=True)
    print(CJK_ASCII_ART)
    print_line(thick=True)
    print(
        "Welcome to CJK! This is an LLM-powered command line tool for learning words in 中文,日本語、and 한국어 all at once!"
    )
    print_line()
