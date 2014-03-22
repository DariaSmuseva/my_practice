def wins(grid):
    rows = [[grid[i+j] for j in 0, 1, 2] for i in 0, 3, 6]
    cols = [[grid[i+j] for j in 0, 3, 6] for i in 0, 1, 2]
    digs = [[grid[i] for i in 0, 4, 8], [grid[i] for i in 2, 4, 6]]
    return any(all(cell is 'x' for cell in row) or
               all(cell is 'o' for cell in row)
               for row in rows + cols + digs)

def full(grid):
    return all(cell is 'x' or cell is 'o' for cell in grid)

def move(grid, cell, symbol):
    moved = list(grid)
    moved[cell] = symbol
    return moved

def moves(grid, symbol):
    return [move(grid, cell, symbol) for cell in 0, 1, 2, 3, 4, 5, 6, 7, 8
            if grid[cell] not in ('x', 'o')]

def minimax(grid, symbol):
    if wins(grid):
        return (1 if symbol is 'o' else -1), None
    elif full(grid):
        return 0, None
    elif symbol is 'x':
        best_score = -2
        best_move = None
        for move in moves(grid, 'x'):
            score, mv = minimax(move, 'o')
            if score >= best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    elif symbol is 'o':
        best_score = 2
        best_move = None
        for move in moves(grid, 'o'):
            score, mv = minimax(move, 'x')
            if score <= best_score:
                best_score = score
                best_move = move
        return best_score, best_move

def tictac(grid, turn):
    score, move = minimax(grid, turn)
    result = ('x win' if score is 1 else
              'o win' if score is -1 else
              'draw')
    print 'On grid %s best move is %s and %s.' % (grid, ''.join(move), result)


#The above code is fairly simple and needs no comment.
#But that's not all. No examples of the use it will not complete.

tictac('xo-'
       'x-o'
       '-xo', 'x')
# On grid xo-x-o-xo best move is xo-x-oxxo and x win.

tictac('xo-'
       'x-o'
       '-xo', 'x')
# On grid xo-x-o-xo best move is xo-x-oxxo and x win.

tictac('xox'
       'oxo'
       'ox-', 'x')
# On grid xoxoxoox- best move is xoxoxooxx and x win.

tictac('x-o'
       '-ox'
       '-x-', 'o')
# On grid x-o-ox-x- best move is x-o-oxox- and o win.

tictac('x-o'
       '---'
       '---', 'x')
# On grid x-o------ best move is x-o-----x and x win.

tictac('---'
       '--x'
       'oo-', 'x')
# On grid -----xoo- best move is -----xoox and x win.

tictac('ox-'
       '-x-'
       'oox', 'x')
# On grid ox--x-oox best move is ox-xx-oox and draw.