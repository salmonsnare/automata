import os
import random
import time

INITIAL_STATE = [13, 13]


def F(s):
    ret = []
    if s[0] > 0:
        ret.append('U')
    if s[0] < 100:
        ret.append('D')
    if s[1] > 0:
        ret.append('R')
    if s[1] < 100:
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
                row += ('亀' + '|')
            else:
                row += ('　' + '|')
        print(row)
    print('---')


def main():
    s = INITIAL_STATE
    os.system('cls')
    print("F(s): {0}".format(F(s)))
    print("mode(s): {0}".format(mode(s)))
    print("G(mode(s)): {0}".format(G(mode(s))))
    print_board(s)
    while True:
        # s = upd(s, input("action: "))
        s = upd(s, random.choice(F(s)))
        os.system('cls')
        print("F(s): {0}".format(F(s)))
        print("mode(s): {0}".format(mode(s)))
        print("G(mode(s)): {0}".format(G(mode(s))))
        print_board(s)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
