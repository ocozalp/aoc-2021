def solve():
  with open('input/q1.txt', 'r') as f:
    lines = list(map(int, f.readlines()))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(numbers):
  return sum([1 for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]])


def solve2(numbers):
  return solve1([sum(numbers[i-2:i+1]) for i in range(2, len(numbers))])


if __name__ == '__main__':
  solve()