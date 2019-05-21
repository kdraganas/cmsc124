# Grammar rules   for a   multi-digit decimal number
# <expr>  ::= +<num> | -<num> |   <num>
# <num>   ::= <num><digits>   |   <digits>
# <digits>    ::= <digit> |   <digit>.<digit>
# <digit> ::= 0|1|2|3|4|5|6|7|8|9
# Terminate   every input string  with    ‘$’.

# P ---> E
# E ---> +N | -N | N
# N ---> DD | D.D
# D ---> 0|1|2|3|4|5|6|7|8|9

import sys
import string

current = None
st = ""
ptr = 0
hasDecimal = False
hasPrefix = False
numArr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def reset():
    global ptr
    global hasDecimal
    global hasPrefix
    hasDecimal = False
    hasPrefix = False
    ptr = 0


def P():
    reset()
    global st
    st = input('Enter equation: ')
    st = st.translate(str.maketrans('', '', string.whitespace))
    move()
    if current == '$':
        # P()
        sys.exit(1)
    E()
    if current == '$':
        print('Valid')
    else:
        print('Invalid')
        sys.exit(1)


def E():
    # print('<expr>')
    N()
    return


def N():
    global hasDecimal
    # print('<number>')
    D()
    if (not hasDecimal) and current == '.':
        hasDecimal = True
        move()
        N()
    elif hasDecimal and current == '+':
        print('Invalid')
        sys.exit(1)
    elif hasDecimal and current == '-':
        print('Invalid')
        sys.exit(1)
    elif hasDecimal and current == '.':
        print('Invalid')
        sys.exit(1)
    elif current in numArr:
        N()
    return


def D():
    global numArr
    global hasPrefix
    # print('<digit>')
    
    if hasDecimal and current in ['+', '-']:
        # if no lookahead():
            print('Invalid')
            sys.exit(1)
    elif current in numArr:
        move()
        # N()
        return
    elif (not hasPrefix) and current in ['+', '-']:
        if not lookahead():
            print('Invalid')
            sys.exit(1)
        hasPrefix = True
        E()
    else:
        print('Invalid')
        sys.exit(1)


def move():
    global current
    global ptr
    current = st[ptr]
    # print('current: ', current)
    ptr += 1
    return


def lookahead():
    global ptr
    if ptr <= len(st) - 2:
        if st[ptr] == '.':
            print(ptr)
            return False
    elif ptr == len(st):
        return False
    move()
    return True


while True:
    P()
