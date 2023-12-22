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
