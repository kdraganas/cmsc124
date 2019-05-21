# grammar
# <term><operator><term>
# <term> = x | y | z
# <operator> = - | +

from itertools import tee, islice, chain

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

def classify(item):
    if item == 'x' or item == 'y' or item == 'z':
        return 0
    if item == '+' or item == '-':
        return 1
    if item == '(':
        return 2
    if item == ')':
        return 3
    if item == '~':
        return 4
    return -1

def syntax(string):
    str_arr = list(string)
    syntax = [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 0]
    ]
    count_open = 0
    count_close = 0
    
    for previous, item, nxt in previous_and_next(str_arr):
        if(previous == None):
            curr_item = classify(item)
            if(curr_item == 1 or curr_item == 3):
                print("Invalid")
                break
        
        if(previous == None and nxt == None):
            curr_item = classify(item)
            if(curr_item == 4):
                print("Invalid")
                break

        if(nxt != None):
            curr_item = classify(item)
            nxt_item = classify(nxt)
            if(curr_item == 2):
                count_open += 1
            if(curr_item == 3):
                count_close += 1
            if(syntax[curr_item][nxt_item] == 1):
                print(grammar(item), end ="");
                continue
            else:
                print("Invalid")
                break
        
        else:
            if(nxt_item == 3):
                count_close += 1
            if(count_open == count_close):                
                print(grammar(item))
                print("Valid")
            else:
                print("Invalid")
    
def grammar(item):
    if item == 'x' or item == 'y' or item == 'z':
        return "<term>"
    if item == '+' or item == '-':
        return "<operator>"
    if item == '(':
        return ""
    if item == ')':
        return ""
    return ""

def main():
    string = input('Enter string: ')
    syntax(string)
  
if __name__== "__main__":
    main()
