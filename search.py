def make_negamax(terminal_value, heuristic_value, children):
    # This should probably be cached in a future version
    def negamax(node, depth, alpha, beta, color):
        tval = terminal_value(node)
        if tval != None:
            return color * tval
        elif depth == 0:
            hval = heuristic_value(node)
            return color * hval
        else:
            for child in children(node):
                val = - negamax(child, depth - 1, - beta, - alpha, - color)
                if val >= beta:
                    return val
                if val > alpha:
                    alpha = val
            return alpha
    return negamax

# Tic tac toe

lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# Always compute values from point of view of x's position.
# I.e. a win for x = 1, a win for y = -1
def terminal_value(board):
    for line in lines:
        if all(board[i] == 'x' for i in line):
            return 1
        if all(board[i] == 'o' for i in line):
            return -1
    if '.' not in board:
        return 0
    return None

def heuristic_value(board):
    total = 0
    for line in lines:
        xnum = sum(1 for i in line if board[i] == 'x')
        onum = sum(1 for i in line if board[i] == 'o')
        if xnum > onum:
            total += 1
        elif xnum < onum:
            total -= 1
    return total / 16.0

def to_str(board):
    return "{}{}{}\n{}{}{}\n{}{}{}".format(*board)

def q(s):
    if s == 'x':
        return 1
    elif s == 'o':
        return -1
    else:
        return 0

def empty_positions(board):
    return [i for i in range(9) if board[i] == "."]


def children(board):
    empty_pos = empty_positions(board)
    if len(empty_pos)%2:
        symbol = 'x'
    else:
        symbol = 'o'
    out = []
    for i in empty_pos:
        newlist = list(board)
        newlist[i] = symbol
        out.append(newlist)
    return out

ttt_nega = make_negamax(terminal_value, heuristic_value, children)

def ask(board):
    # No error checking!
    return int(raw_input("Your move?"))

def choose(board):
    return max(children(board),key = lambda c: -ttt_nega(c,3,-2,2,-1))

def report(board):
    tval = terminal_value(board)
    if terminal_value(board) != None:
        print "Game over.",
        if tval == 1:
            print "computer wins."
        elif tval == 0:
            print "Draw!"
        elif tval == -1:
            print "You win."
        return 1
    return None

def play():
    board = '.........'
    print "When entering moves, use these positions:"
    print to_str(range(9))
    while True:
        if report(board) != None:
            break
        board = choose(board)
        print "Computer moved to:"
        print to_str(board)
        if report(board) != None:
            break
        i = ask(board)
        print "You moved to:"
        board[i] = 'o'
        print to_str(board)

play()
