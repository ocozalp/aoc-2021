from collections import defaultdict


def solve():
  with open('input/q5.txt', 'r') as f:
    lines = list(map(convert, f.readlines()))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def convert(l):
  _p1, _p2 = map(lambda t: t.strip(), l.split('->'))
  p1 = tuple(map(int, _p1.split(',')))
  p2 = tuple(map(int, _p2.split(',')))
  return (p1, p2)


def solve1(lines, filter_func=lambda line:line[0][0] == line[1][0] or line[0][1] == line[1][1]):
  filtered_lines = [line for line in lines if filter_func(line)]
  points = defaultdict(int)
  for line in filtered_lines:
    dx = (line[1][0]-line[0][0])/abs(line[1][0]-line[0][0]) if line[1][0] != line[0][0] else 0
    dy = (line[1][1]-line[0][1])/abs(line[1][1]-line[0][1]) if line[1][1] != line[0][1] else 0
    current = line[0]
    while current != line[1]:
      points[current] += 1
      current = (current[0]+dx, current[1]+dy)
    points[line[1]] += 1

  return len([p for p in points if points[p] > 1])


def solve2(lines):
  return solve1(lines, filter_func=lambda line:line[0][0] == line[1][0] or line[0][1] == line[1][1] or abs(line[1][0]-line[0][0])==abs(line[1][1]-line[0][1]))


if __name__ == '__main__':
  solve()