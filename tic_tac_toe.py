import random

INITIAL_STATE = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def isFulfilled(s):
    flag = True
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == '-':
                flag = flag & False
    return flag


def F(s):
    ret = []    
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == '-':
                ret.append([i, j])
    return ret


def mode(s):
    return s

def G(x):
    return F(x)

def tran(s, a, step):
    '''
    dom: states and actions
    codom: states
    '''
    ret = []    
    for i in range(len(s)):
        row_ret = []
        for j in range(len(s[i])):
            if i == a[0] and j == a[1]:
                row_ret.append('○' if step % 2 == 0 else '×')
            else:
                row_ret.append(s[i][j])
        ret.append(row_ret)        
    return ret

def pass_(s, a):
    '''
    dom: states and actions
    codom: states
    '''
    if isFulfilled(s):
        return [None, None]
    else:
        return a

# controller (forw and back)
def controller_forw(s):
    return s

def controller_backw(s, a, step):
    return tran(s, a, step)

# view (forw and back)
def view_forw(s):
    return mode(s)

def view_backw(s, a):
    return pass_(s, a)

# obs and upd
def obs(s):
    return(mode(s))

def upd(s, a, step):
    return tran(s, a, step)

def print_board(s, indent=0):
    for i in range(len(s)):
        indent_str = ''
        for _ in range(indent):
            indent_str += '  '
        row = indent_str + '|'
        for j in range(len(s[0])):
            row += (str(s[i][j]) + '|')
        print(row)

def stop(s):
    cond1 = (s[0][0] == s[0][1]) and (s[0][1] == s[0][2]) and (s[0][0] != '-') and (s[0][1] != '-') and (s[0][2] != '-') 
    if cond1:
        print('row 0')

    cond2 = (s[1][0] == s[1][1]) and (s[1][1] == s[1][2]) and (s[1][0] != '-') and (s[1][1] != '-') and (s[1][2] != '-')
    if cond2:
        print('row 1')

    cond3 = (s[2][0] == s[2][1]) and (s[2][1] == s[2][2]) and (s[2][1] != '-') and (s[2][2] != '-') and (s[0][0] != '-')
    if cond3:
        print('row 2')

    cond4 = (s[0][0] == s[1][0]) and (s[1][0] == s[2][0]) and (s[0][0] != '-') and (s[1][0] != '-') and (s[2][0] != '-')
    if cond4:
        print('col 0')

    cond5 = (s[0][1] == s[1][1]) and (s[1][1] == s[2][1]) and (s[0][1] != '-') and (s[1][1] != '-') and (s[2][1] != '-')
    if cond5:
        print('col 1')

    cond6 = (s[0][2] == s[1][2]) and (s[1][2] == s[2][2]) and (s[0][2] != '-') and (s[1][2] != '-') and (s[2][2] != '-')
    if cond6:
        print('col 2')

    cond7 = (s[0][0] == s[1][1]) and (s[1][1] == s[2][2]) and (s[0][0] != '-') and (s[1][1] != '-') and (s[2][2] != '-')
    if cond7:
        print('＼')

    cond8 = (s[0][2] == s[1][1]) and (s[1][1] == s[2][0]) and (s[0][2] != '-') and (s[1][1] != '-') and (s[2][0] != '-')
    if cond8:
        print('／')

    return cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7 or cond8


def main():
    s = INITIAL_STATE
    for step in range(9):
        print("F(s): {0}".format(F(s)))
        print("mode(s): {0}".format(mode(s)))
        print("G(mode(s)): {0}".format(G(mode(s))))
        print("step: {0}".format(step))
        action = random.choice(F(s))
        print("action: {0}".format(action))
        s = upd(s, action, step)
        print_board(s)
        if stop(s):
            break
        print('---')


if __name__ == "__main__":
    main()
