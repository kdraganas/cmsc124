def palindrome(string, i, j):
    if i + 1 >= j:
        if i == 0:
            # print('1')
            print('<palindrome>')
            print('<letter>')
        elif i + 1 == j:
            # print('2')
            print(str(string[:i]) + '<letter> <palindrome> <letter>' + str(string[j + 1:]))
            print(str(string[:i + 1]) + '<palindrome>' + str(string[j:]))
            print(str(string[:i + 1]) + '<letter>' + str(string[j:]))
            print(str(string[:i + 1]) + '<null>' + str(string[j:]))
        else:
            print(str(string[:i]) + '<letter>' + str(string[j + 1:]))
        print(string)
        return True
    else:
        if i + 1 <= j - 1:
            if i == 0:
                # print('3')
                print('<palindrome>')
                print('<letter> <palindrome> <letter>')
                print(str(string[:i + 1]) + '<palindrome>' + str(string[j:]))
            else:
                # print('4')
                print(str(string[:i]) + '<letter> <palindrome> <letter>' + str(string[j + 1:]))
                print(str(string[:i + 1]) + '<palindrome>' + str(string[j:]))              
        else: 
            # print('5')
            print(str(string[:i + 1]) + '<palindrome>' + str(string[j:]))
            print(str(string[:i + 1]) + '<letter>' + str(string[j:]))
        if string[i] == string[j]:
            i += 1
            j -= 1
            return palindrome(string, i, j)
        else:
            return False

def run_palindrome():
    string = input('Enter string: ')
    string = ''.join(e for e in string if e.isalnum())
    str_arr = list(string.lower().replace(' ', ''))
    print(str_arr)
    print('\n')

    if palindrome(str_arr, 0, len(str_arr) - 1):
        print('Palindrome')
    else:
        print('Not Palindrome')


def main():
    run_palindrome()
  
if __name__== "__main__":
    main()
