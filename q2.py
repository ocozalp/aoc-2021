vectors = {
  # for part 1: (horizontal, vertical)
  # for part 2: (horizontal, aim, vertical)
  'forward': (1, 0, 1),
  'down': (0, 1, 0),
  'up': (0, -1, 0)
}

def solve():
  with open('input/q2.txt', 'r') as f:
    commands = map(lambda token: (token[0], int(token[1])), map(lambda l: l.split(), f.readlines()))

  print('Answer 1:', solve1(commands[:]))
  print('Answer 2:', solve2(commands[:]))


def solve1(commands):
  horizontal, depth = 0, 0
  for command in commands:
    v  = vectors[command[0]]
    horizontal += v[0] * command[1]
    depth += v[1] * command[1]
  return horizontal * depth


def solve2(commands):
  horizontal, depth, aim = 0, 0, 0
  for command in commands:
    v  = vectors[command[0]]
    horizontal += v[0] * command[1]
    aim += v[1] * command[1]
    depth += v[2] * aim * command[1]
  return horizontal * depth


if __name__ == '__main__':
  solve()