def solve():
  with open('input/q6.txt', 'r') as f:
    ages = list(map(int, f.readline().split(',')))

  print('Answer 1:', solve1(ages[:]))
  print('Answer 2:', solve2(ages[:]))


def solve1(ages, iter=80):
  zero_index = 0
  counts = [0] * 9
  for age in ages:
    counts[age] += 1
  
  for _ in range(iter):
    to_add = counts[zero_index]
    counts[zero_index] = 0
    zero_index = (zero_index+1) % 9
    eight_idx = (zero_index+8) % 9
    six_idx = (zero_index+6) % 9
    counts[eight_idx] += to_add
    counts[six_idx] += to_add
  return sum(counts)


def solve2(ages):
  return solve1(ages, 256)


if __name__ == '__main__':
  solve()