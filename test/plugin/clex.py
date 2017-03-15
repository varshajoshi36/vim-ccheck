import re
import sys
# Build the lexer
sys.path.append('/home/varsha/.vim/bundle/test/plugin/ply')
#from ply import *
#import importlib.util
#spec = importlib.util.spec_from_file_location("ply", "/home/varsha/.vim/bundle/test/plugin/myparser/ply")
#lex = importlib.util.module_from_spec(spec)
sys.path.insert(0, '.')
import lex

#class ansic_lexer (object):
#    def __init__ (self, error_func):
#        self.prev_token = None;
#
#    def lexer_input_data (self, data):
#        self.lexer.input (data);
#
#    def build_lexer(self):
#        self.lexer = lex.lex(object=self)
#
#    def t_NEWLINE(self, t):
#        r'\n+'
#        t.lexer.lineno += t.value.count("\n")
#
#    def t_comment(self, t):
#        r'/\*(.|\n)*?\*/'
#        t.lexer.lineno += t.value.count('\n')
#
#    # Preprocessor directive (ignored)
#    def t_preprocessor(self, t):
#        r'\#(.)*?\n'
#        t.lexer.lineno += 1
#
#    def t_error(self, t):
#        print("Illegal character %s" % repr(t.value[0]))
#        t.lexer.skip(1)

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Preprocessor directive (ignored)
def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)

#List of token names. Do not delete.
#Always required.
keywords = (
    'AUTO',
    'BREAK',
    'CASE',
    'CHAR',
    'CONST',
    'CONTINUE',
    'DEFAULT',
    'DOUBLE',
    'DO',
    'ELSE',
    'ENUM',
    'EXTERN',
    'FLOAT',
    'FOR',
    'GOTO',
    'IF',
    'INLINE',
    'INT',
    'LONG',
    'REGISTER',
    'RESTRICT',
    'RETURN',
    'SHORT',
    'SIGNED',
    'SIZEOF',
    'STATIC',
    'STRUCT',
    'SWITCH',
    'TYPEDEF',
    'UNION',
    'UNSIGNED',
    'VOID',
    'VOLATILE',
    'WHILE',
    )

tokens = keywords + (
    #Identifiers
    'ID',

    #Type defined identifiers
    'TYPEID',

    #Constants
    #String Constant
    'STRING_LITERAL',

    #Integer Constant
    'INT_CONST_DEC', 'INT_CONST_OCT', 'INT_CONST_HEX',

    #Floating Constant
    'FLOAT_CONST', 'HEX_XFLOAT_CONST',

    #Operators
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'LT', 'LEQ', 'GT', 'GEQ', 'EQ', 'NEQ',
    'BOR', 'BAND', 'BNOT', 'XOR', 'LSHIFT', 'RSHIFT',
    'LOR', 'LAND', 'LNOT',

    #Assignment operators
    'ASSIGN', 'RSHIFT_ASSIGN', 'LSHIFT_ASSIGN', 'ADD_ASSIGN',
    'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN',
    'AND_ASSIGN', 'XOR_ASSIGN', 'OR_ASSIGN',

    #Unary operators
    'INC', 'DEC',
    'PTR_OP', #->
    'IS_TRUE', #?
    'DOT', #.

    #Delimiters
    'COLON', 'SEMICOLON',
    'COMMA',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'LSQUARE', 'RSQUARE',

    #Ellipsis
    'ELLIPSIS' #...
    )

#Once the tokens are declared. Define them with rules for each.
t_INT_CONST_DEC = r'[0-9]+';
t_STRING_LITERAL = r'\"([^\\\n]|(\\.))*?\"';
Hexadecimal_Prefix = r'[0x][0X]';
Hexadecimal_Digits = r'[a-fA-F0-9]+';
Octal_Digits = r'0[0-7]+';
Exponent_Constant = r'[Ee][+-]?{D}+';
Fractional_Constant = r"""([0-9]*\.[0-9]+)|([0-9]+\.)"""
#Floating_Suffix = r'[fFlL]';
#Integer_Suffix = r'[uUlL]';
#Fractional_Suffix = 'r[fFlL]';


keywords_map = {}
for r in keywords:
    keywords_map[r.lower()] = r

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = keywords_map.get(t.value, "ID")
    return t

t_ignore = ' \t'

#Regex for inc and dec
t_INC = r'\+\+'
t_DEC = r'--'

#Regex for operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LT = r'<'
t_LEQ = r'<='
t_GT = r'>'
t_GEQ = r'>='
t_EQ = r'=='
t_NEQ = r'!='
t_BOR = r'\|'
t_BAND = r'&'
t_BNOT = r'~'
t_XOR = r'\^'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_LOR = r'\|\|'
t_LAND = r'&&'
t_LNOT = r'!'

#Regex for assignment operators
t_ASSIGN = r'='
t_RSHIFT_ASSIGN = r'>>='
t_LSHIFT_ASSIGN = r'<<='
t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN = r'-='
t_MUL_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_AND_ASSIGN = r'&='
t_XOR_ASSIGN = r'\^='
t_OR_ASSIGN = r'\|='

#Regex for unary ops
t_PTR_OP = r'->'
t_IS_TRUE = r'\?'
t_DOT = r'\.'

#Delimiters
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'

#Ellipsis
t_ELLIPSIS = r'\.\.\.'

lexer = lex.lex()
if __name__ == "__main__":
    lex.runmain(lexer)
