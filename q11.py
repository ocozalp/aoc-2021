from collections import defaultdict


def solve():
  with open('input/q11.txt', 'r') as f:
    lines = list(map(lambda s: map(int, s.strip()[:]), f.readlines()))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(numbers):
  energy_map = [set() for _ in range(10)]
  for i, row in enumerate(numbers):
    for j, level in enumerate(row):
      energy_map[level].add((i, j))

  res = 0
  zero_idx = 0
  nine_idx = 9
  for _ in range(100):
    zero_idx = (zero_idx - 1) % 10
    nine_idx = (nine_idx - 1) % 10
    frontier = list(energy_map[zero_idx])

    flashed = set()
    while frontier:
      current = frontier.pop(0)
      if current in flashed:
        continue

      idx = -1
      for i, elms in enumerate(energy_map):
        if current in elms:
          idx = i
          break

      if idx == zero_idx:
        flashed.add(current)
        for n in get_n(current[0], current[1], len(numbers), len(numbers[0])):
          frontier.append(n)
      else:
        next_idx = (idx + 1) % 10
        energy_map[idx].remove(current)
        energy_map[next_idx].add(current)
        if next_idx == zero_idx:
          frontier.append(current)

    res += len(flashed)

  return res


def get_n(i, j, rowc, colc):
  for di in range(-1, 2):
    for dj in range(-1, 2):
      if di == 0 and dj == 0:
        continue
      ni = i + di
      nj = j + dj
      if 0 <= ni < rowc and 0 <= nj < colc:
        yield (ni, nj)


def solve2(numbers):
  energy_map = [set() for _ in range(10)]
  for i, row in enumerate(numbers):
    for j, level in enumerate(row):
      energy_map[level].add((i, j))
  total_elms = len(numbers)*len(numbers[0])

  zero_idx = 0
  nine_idx = 9
  step = 0
  while True:
    step += 1
    zero_idx = (zero_idx - 1) % 10
    nine_idx = (nine_idx - 1) % 10
    frontier = list(energy_map[zero_idx])

    flashed = set()
    while frontier:
      current = frontier.pop(0)
      if current in flashed:
        continue

      idx = -1
      for i, elms in enumerate(energy_map):
        if current in elms:
          idx = i
          break

      if idx == zero_idx:
        flashed.add(current)
        for n in get_n(current[0], current[1], len(numbers), len(numbers[0])):
          frontier.append(n)
      else:
        next_idx = (idx + 1) % 10
        energy_map[idx].remove(current)
        energy_map[next_idx].add(current)
        if next_idx == zero_idx:
          frontier.append(current)

    if len(energy_map[zero_idx]) == total_elms:
      return step


if __name__ == '__main__':
  solve()