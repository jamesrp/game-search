
# Assume starting player is computer for now

def command_line_play(initial_board,instructions,children,terminal_value,ask,\
        to_str,depth,negamax):
    def report(board):
        tval = terminal_value(board)
        if tval != None:
            print "Game over:",
            if tval == 1:
                print "computer wins."
            elif tval == 0:
                print "Draw!"
            elif tval == -1:
                print "You win."
            return 0
        return 1
    
    def choose(board):
        return max(children(board),key = lambda c: -negamax(c,depth,-2,2,-1))

    board = initial_board
    print instructions
    while report(board):
        board = choose(board)
        print "Computer moved to:"
        print to_str(board)
        if report(board) == 0:
            break
        board = ask(board)
        print "You moved to:"
        print to_str(board)


