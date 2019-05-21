# <expr> ::= <expr>+<term> | <expr>-<term> | <term>
# <term> ::= <term>*<factor> | <term>/<factor> | <factor>
# <factor> ::= (<expr>) |<digit>
# <digit> ::= 0|1|2|3
# Terminate every input string with ‘$’.

# P ---> E '$'
# E ---> T  { ( '+' | '-' ) T }
# T ---> F { ( '*' | '/' ) F }
# F ---> '(' E ')' | 0|1|2|3

import sys

current = None
string = ""
ptr = 0


def P():
    global string
    string = input('Enter equation: ')
    string = string.replace(" ", "")

    if '$' not in string:
        print('Invalid')
        sys.exit(1)

    move()
    if current == '$':
        sys.exit(1)
    E()
    if current == '$':
        print('Valid')
    else:
        print('Invalid')
        sys.exit(1)


def E():
    # print('<expr>', current)
    T()
    while current == '+' or current == '-':
        move()
        T()
    # print('<expr> ===> current = ', current)
    return


def T():
    # print('<term>', current)
    F()
    while current == '*' or current == '/':
        move()
        F()
    # print('<term> ===> current = ', current)
    return


def F():
    # print('<factor>', current)
    if current in ['0', '1', '2', '3']:
        move()
        # print('<factor> ===>', current)
        return
    elif current == '(':
        move()
        E()
        if current == ')':
            move()
            # print('<factor> ===> current = ', current)
            return
        else:
            print('Invalid')
            sys.exit(1)
    else:
        print('Invalid')
        sys.exit(1)


def move():
    global current
    global ptr
    current = string[ptr]
    # print('current: ', current)
    ptr += 1
    return


P()
