def solve():
  with open('input/q4.txt', 'r') as f:
    lines = f.readlines()
    numbers = list(map(int, lines[0].strip().split(',')))

    number_of_boards = (len(lines)-1)//6
    boards = []
    i = 1
    for _ in range(number_of_boards):
      board = {}
      i += 1
      for j in range(5):
        line = map(int, lines[i+j].strip().split())
        for k, num in enumerate(line):
          board[num] = (j, k)

      i += 5
      boards.append(board)

  print('Answer 1:', solve1(numbers, boards))
  print('Answer 2:', solve2(numbers, boards))


def solve1(numbers, boards, stop_after=1):
  board_counts = []
  for _ in range(len(boards)):
    cols = [5] * 5
    rows = [5] * 5
    board_counts.append((rows, cols))
  
  winning_board = -1
  number_of_winners = 0
  last_num = -1
  already_won = set()
  for number in numbers:
    last_num = number

    for i, board in enumerate(boards):
      if i in already_won or number not in board:
        continue

      row, col = board[number]
      board_counts[i][0][row] -= 1
      if board_counts[i][0][row] == 0:
        number_of_winners += 1
        already_won.add(i)
        if number_of_winners == stop_after:
          winning_board = i
        continue

      board_counts[i][1][col] -= 1
      if board_counts[i][1][col] == 0:
        number_of_winners += 1
        already_won.add(i)
        if number_of_winners == stop_after:
          winning_board = i
        continue
    
    if number_of_winners == stop_after:
      break
  
  s = sum(boards[winning_board].keys())
  for i in range(len(numbers)):
    if numbers[i] in boards[winning_board]:
      s -= numbers[i]
    if numbers[i] == last_num:
      break
  
  return s * last_num


def solve2(numbers, boards):
  return solve1(numbers, boards, stop_after=len(boards))


if __name__ == '__main__':
  solve()