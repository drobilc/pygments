from pygments.style import Style
from pygments.token import Keyword, Comment

__all__ = ['StgyleStyle']

class StgyleStyle(Style):
    """
    Black and white style inspired by the Pygments bw style. It is meant to be
    used with the stg lexer.
    """
    name = 'stgyle'

    styles = {
        Comment:                   "italic #959595",
        Keyword.Reserved:          "bold #000000",
        Keyword.Other:             "bold #000000",
    }
