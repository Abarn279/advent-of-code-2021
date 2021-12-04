from aoc_utils import Vector2, Grid2d

def get_winning_board_score(board, drawn, last_drawn):
    # check rows
    for row in range(5):
        is_winner = True
        for col in range(5):
            if board[Vector2(col, row)] not in drawn:
                is_winner = False
                break
        if is_winner: break
        else: is_winner = False

    # after checking rows, if there's no winner, then it's time to check columns. 
    if not is_winner:
        for col in range(5):
            is_winner = True
            for row in range(5):
                if board[Vector2(col, row)] not in drawn:
                    is_winner = False
                    break
            if is_winner: break
            else: is_winner = False
    
    # after checking rows and there's a winner, or checking columns too and there's a winner
    if is_winner:
        return sum(i for i in board.values() if i not in drawn) * last_drawn

    # there's no winner here, just return none
    else:
        return None

with open('./inp/04.txt') as f:
    draws_s, boards_s = f.read().split("\n\n", 1)

# Part A
draw_order = list(map(int, draws_s.split(',')))
drawn = set()
boards = []

# Set boards
for board_s in boards_s.split('\n\n'):
    grid = Grid2d(None)
    lines = board_s.split('\n')
    for y in range(5):
        line = lines[y]
        spaces = [int(i) for i in line.split(' ') if i != '']
        for x in range(5):
            grid[Vector2(x, y)] = spaces[x]
    boards.append(grid)

def print_score():
    for d in draw_order:
        drawn.add(d)
        for b in boards:
            score = get_winning_board_score(b, drawn, d)
            if score is not None:
                print(score)
                return

print_score()

# Part B

def print_score_b():
    global boards
    for d in draw_order:
        drawn.add(d)
        non_winners = []
        for b in boards:
            score = get_winning_board_score(b, drawn, d)
            if score is None:
                non_winners.append(b)
        
        if len(non_winners) == 0:
            print(score)
            return
        boards = non_winners

print_score_b()