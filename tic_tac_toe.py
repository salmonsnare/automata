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
    if isFulfilled(s):
        return "fulfilled"
    else:
        ret = []    
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] == '-':
                    ret.append([i, j])
        return str(ret)

def G(x):
    if x == "fulfilled":
        return set()
    else:
        return set(eval(x))

def tran(s, a, step):
    '''
    dom: states and actions
    codom: states
    '''
    if isFulfilled(s):
        return s 
    else:
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


# for state in [(0, 0), (0, 1), (1, 1), (2, 1)]:
#     print("state: {0}".format(state))
#     print("F(state): {0}".format(F(state)))
#     print("mode(state): {0}".format(mode(state)))
#     print("G(mode(state)): {0}".format(G(mode(state))))
#     print("---")

# s = (0, 0)
# print(s)
# for index in range(13):
#     s = upd(s, 10)
#     print(s)
# print("---")
# s = (0, 0)
# print(s)
# s = upd(s, 10)
# print(s)
# s = upd(s, 10)
# print(s)
# s = upd(s, 100)
# print(s)
# print("---")
# s = (0, 0)
# print(s)
# s = upd(s, 100)
# print(s)
# s = upd(s, 10)
# print(s)
# s = upd(s, 10)
# print(s)
# s = upd(s, 10)
# print(s)

# print(upd(upd((0, 0), 10), 100))
def main():
    s = INITIAL_STATE
    for step in range(9):
        print("mode(s): {0}".format(mode(s)))
        print("step: {0}".format(step))
        action = random.choice(F(s))
        print("action: {0}".format(action))
        s = upd(s, action, step)
        print_board(s)
        if stop(s):
            break
        print('---')

    def process(state, action, step):
        state = upd(state, action, step), step
        print_board(state)
        print('---')
        return state

    # for action1 in F(INITIAL_STATE):
        
    #     for action2 in F(s1):
    #         process(INITIAL_STATE, action1, 0)

    #         for action3 in F(s2):
    #             s3 = upd(s2, action3, 2)
    #             print_board(s3, 2)
    #             if stop(s3):
    #                 break
    #             print('---')

    #             for action4 in F(s3):
    #                 s4 = upd(s3, action4, 3)
    #                 print_board(s4)
    #                 if stop(s4):
    #                     break
    #                 for action5 in F(s4):
    #                     s5 = upd(s4, action5, 4)
    #                     print_board(s5)
    #                     if stop(s5):
    #                         break
    #                     for action6 in F(s5):
    #                         s6 = upd(s5, action6, 5)
    #                         print_board(s6)
    #                         if stop(s6):
    #                             break
    #                         for action7 in F(s6):
    #                             s7 = upd(s6, action7, 6)
    #                             print_board(s7)
    #                             if stop(s7):
    #                                 break


if __name__ == "__main__":
    main()


