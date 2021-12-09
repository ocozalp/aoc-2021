from functools import reduce

neighbors = [
  (-1, 0),
  (0, 1),
  (1, 0),
  (0, -1)
]

def solve():
  with open('input/q9.txt', 'r') as f:
    numbers = list(map(lambda l2: list(map(int, l2)), map(lambda l: list(l.strip()), f.readlines())))

  print('Answer 1:', solve1(numbers[:]))
  print('Answer 2:', solve2(numbers[:]))


def solve1(numbers):
  low_points = find_low_points(numbers)
  return sum(map(lambda lp: numbers[lp[0]][lp[1]], low_points)) + len(low_points)


def find_low_points(numbers):
  result = list()
  for i, row in enumerate(numbers):
    for j, num in enumerate(row):
      if is_low_point(numbers, i, j):
        result.append((i, j))
  return result

def is_low_point(numbers, i, j):
  return len([1 for r1, c1 in get_n(numbers, i, j) if numbers[r1][c1] <= numbers[i][j]]) == 0

def get_n(numbers, i, j):
  result = list()
  for n in neighbors:
    ni, nj = i + n[0], j + n[1]
    if 0 <= ni < len(numbers) and 0 <= nj < len(numbers[0]):
      result.append((ni, nj))
  return result


def solve2(numbers):
  low_points = find_low_points(numbers)
  sizes = []
  for lp in low_points:
    visited = set()
    frontier = [lp]
    while frontier:
      current = frontier.pop(0)
      if current in visited or numbers[current[0]][current[1]] == 9:
        continue

      visited.add(current)
      for n in get_n(numbers, current[0], current[1]):
        frontier.append(n)

    sizes.append(len(visited))
  
  sizes.sort()
  return reduce(lambda a, b: a*b, sizes[-3:], 1)


if __name__ == '__main__':
  solve()