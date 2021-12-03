def solve():
  with open('input/q3.txt', 'r') as f:
    lines = list(map(lambda s: s.strip(), f.readlines()))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def count_ones(numbers):
  cnts = [0] * len(numbers[0])
  for num in numbers:
    for i, c in enumerate(num):
      if c == '1':
        cnts[i] += 1
  return cnts


def solve1(numbers):
  cnts = count_ones(numbers)  

  g = 0
  multiplier = 1
  for i in range(len(cnts)-1, -1, -1):
    if 2*cnts[i] >= len(numbers):
      g += multiplier
    multiplier *= 2
  
  return g * (multiplier-g-1)


def solve2(numbers):
  num_of_bits = len(numbers[0])
  # o2, co2
  reports = [numbers[:], numbers[:]]
  popular = ['1', '0']

  for i in range(num_of_bits):
    for j in range(len(reports)):
      report = reports[j]
      if len(report) > 1:
        cnts = count_ones(report)
        value = popular[j] if 2*cnts[i] >= len(report) else popular[(j+1)%2]
        reports[j] = [v for v in report if v[i] == value]

  o2, co2 = map(lambda s: int(s, 2), map(lambda r: ''.join(r), reports))
  return o2 * co2


if __name__ == '__main__':
  solve()