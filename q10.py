from collections import defaultdict, deque

close_to_open = {
  '}': '{',
  ']': '[',
  ')': '(', 
  '>': '<'
}

corruption_points = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

completion_points = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

def solve():
  with open('input/q10.txt', 'r') as f:
    lines = list(map(lambda l: l.strip(), f.readlines()))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  result = 0
  for line in lines:
    stack = deque()
    for c in line:
      if c not in close_to_open:
        stack.append(c)
      else:
        opening_char = close_to_open[c]
        if len(stack) == 0 or stack.pop() != opening_char:
          result += corruption_points[c]
          break 
  return result


def solve2(lines):
  open_to_close = {close_to_open[k]: k for k in close_to_open}

  scores = []
  for line in lines:
    stack = deque()
    is_corrupted = False
    for c in line:
      if c not in close_to_open:
        stack.append(c)
      else:
        opening_char = close_to_open[c]
        if len(stack) == 0 or stack.pop() != opening_char:
          is_corrupted = True
          break 
    if not is_corrupted:
      score = 0
      while stack:
        top_elm = stack.pop()
        closing_char = open_to_close[top_elm]
        score = score * 5 + completion_points[closing_char]
      scores.append(score)

  scores.sort()
  return scores[len(scores)//2]


if __name__ == '__main__':
  solve()