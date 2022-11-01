import os
import random
import time
from colored import fg, stylize

INITIAL_STATE = [13, 13]
history_state = []

def F(s):
    ret = []
    if s[0] > 0:
        ret.append('U')
    if s[0] < 100:
        ret.append('D')
    if s[1] < 100:
        ret.append('R')
    if s[1] > 0:
        ret.append('L')
    return ret


def mode(s):
    return s


def G(x):
    return F(x)


def tran(s, a):
    '''
    dom: states and actions
    codom: states
    '''
    if a == 'U':
        return [max(0, s[0] - 1), s[1]]
    elif a == 'D':
        return [min(s[0] + 1, 25), s[1]]
    elif a == 'L':
        return [s[0], max(0, s[1] - 1)]
    elif a == 'R':
        return [s[0], min(s[1] + 1, 25)]


def pass_(s, a):
    '''
    dom: states and actions
    codom: states
    '''
    return a

# controller (forw and back)
def controller_forw(s):
    return s

def controller_backw(s, a):
    return tran(s, a)

# view (forw and back)
def view_forw(s):
    return mode(s)

def view_backw(s, a):
    return pass_(s, a)

# obs and upd
def obs(s):
    return(mode(s))


def upd(s, a):
    return tran(s, a)


def print_board(s):
    for i in range(25):
        row = '|'
        for j in range(25):
            if s[0] == i and s[1] == j:
                row += (stylize('亀', fg("green")) + '|')
            else:
                row += ('　' + '|')
        print(row)
    print('---')


def print_history():
    for i in range(25):
        row = '|'
        for j in range(25):
            if [i, j] in history_state:
                if history_state[len(history_state) - 1] == [i, j]:
                    row += (stylize('亀', fg("light_green")) + '|')
                else:
                   row += (stylize('亀', fg("dark_green")) + '|')
            else:
                row += ('　' + '|')
        print(row)


def main():
    s = INITIAL_STATE
    os.system('cls')
    print("F(s): {0}".format(F(s)))
    print("mode(s): {0}".format(mode(s)))
    print("G(mode(s)): {0}".format(G(mode(s))))
    print_board(s)
    history_state.append(s)
    while True:
        # s = upd(s, input("action: "))
        s = upd(s, random.choice(F(s)))
        history_state.append(s)
        os.system('cls')
        print("F(s): {0}".format(F(s)))
        print("mode(s): {0}".format(mode(s)))
        print("G(mode(s)): {0}".format(G(mode(s))))
        print_history()
        time.sleep(0.25)
        

if __name__ == "__main__":
    main()
