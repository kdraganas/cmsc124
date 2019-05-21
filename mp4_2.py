import re
import sys

operators = ['+', '-', '*', '/', '%', '^']
priority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}


def check_type(user_input):
    copy = user_input
    # copy = re.sub(r'\([^)]*\)', '', copy)
    copy = copy.replace('(', '')
    copy = copy.replace(')', '')
    # print(copy)
    ls_copy = copy.split()
    # print(ls_copy)
    if ls_copy[0] in operators:
        return 'prefix'
    elif ls_copy[0].isdigit() and ls_copy[1].isdigit():
        return 'postfix'
    else:
        return 'infix'


def prefix_to_infix(user_input):
    user_input = user_input.split()
    stack = []
    for i, ch in enumerate(reversed(user_input)):
        if ch != ' ':
            if ch in operators:
                a = stack.pop()
                b = stack.pop()
                if i != len(user_input) - 1:
                    exp = '(' + a + ch + b + ')'
                else:
                    exp = a + ch + b
                stack.append(exp)
            else:
                stack.append(ch)
    print(stack[-1])
    return stack[-1]


def postfix_to_infix(user_input):
    user_input = user_input.split()
    stack = []
    for i, ch in enumerate(user_input):
        if ch != ' ':
            if ch not in operators:
                stack.append(ch)
            else:
                b = stack.pop()
                a = stack.pop()
                if i != len(user_input) - 1:
                    exp = '(' + a + ch + b + ')'
                else:
                    exp = a + ch + b
                stack.append(exp)
    return stack[-1]


def ask_input():
    user_input = input('Expression: ')
    # user_input = re.sub(r'\s+', '', user_input)
    input_type = check_type(user_input)
    try:
        if input_type == 'prefix':
            # print("Prefix to Infix: {}".format(prefix_to_infix(user_input)))
            print('Answer: {}'.format(
                eval(prefix_to_infix(user_input).replace('^', '**'))))
        elif input_type == 'infix':
            print('Answer: {}'.format(eval(user_input)))
        else:
            # print("Postfix to Infix: {}".format(postfix_to_infix(user_input)))
            print('Answer: {}'.format(
                eval(postfix_to_infix(user_input).replace('^', '**'))))
    except IndexError as e:
        print("Invalid input!")
        sys.exit(1)
    except SyntaxError as e:
        print("Invalid input!")
        sys.exit(1)


ask_input()
