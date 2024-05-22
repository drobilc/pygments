from pygments.lexer import RegexLexer
from pygments.token import Comment, Operator, Keyword, Name, \
    Number, Punctuation, Whitespace
from pygments import unistring as uni

__all__ = ['STGLexer']

class STGLexer(RegexLexer):
    """
    A lexer for the STG (spineless, tagless G-machine) language.
    """
    name = 'STG'
    aliases = ['stg']
    filenames = ['*.stg']

    reserved = ("case", "of", "let", "in")
    objects = ("THUNK", "FUN", "PAP", "CON", "BLACKHOLE")

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'--(?![!#$%&*+./<=>?@^|_~:\\]).*?$', Comment),
            (r'\b({})(?!\')\b'.format('|'.join(reserved)), Keyword.Reserved),
            (r'\b({})(?!\')\b'.format('|'.join(objects)), Keyword.Other),
            (r"'?[_" + uni.Ll + r"][\w']*", Name),
            (r'(->)', Operator),
            (r'[=&*]+', Operator),
            (r'\d(_*\d)*', Number.Integer),
            (r'[][()]', Punctuation),
        ],
    }


