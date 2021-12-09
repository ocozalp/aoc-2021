import itertools


segments = {
  '0': 'abcefg',
  '1': 'cf',
  '2': 'acdeg',
  '3': 'acdfg',
  '4': 'bcdf',
  '5': 'abdfg',
  '6': 'abdefg',
  '7': 'acf',
  '8': 'abcdefg',
  '9': 'abcdfg'
}

def solve():
  with open('input/q8.txt', 'r') as f:
    lines = list(map(lambda l: tuple(map(lambda t: tuple(t.strip().split(' ')), l.split('|'))), map(lambda s: s.strip(), f.readlines())))

  print('Answer 1:', solve1(lines[:]))
  print('Answer 2:', solve2(lines[:]))


def solve1(lines):
  lens = {len(segments[s]) for s in segments if s in ('1', '4', '7', '8')}
  return sum([sum([1 for t in line[1] if len(t) in lens]) for line in lines])


def solve2(lines):
  reverse_segments = {}
  for n in segments:
    reverse_segments[segments[n]] = n

  mapping = {}
  def convert(s):
    return ''.join(sorted([mapping[c] for c in s]))

  def get_digit(s):
    return reverse_segments[''.join(sorted(s))]
  
  def get_number(ss):
    return int(''.join(map(get_digit, map(convert, ss))))
  
  result = 0
  vals = set()
  for s in segments.values():
    vals.add(s)
  for signals, tokens in lines:
    for p in itertools.permutations('abcdefg'[:]):
      
      count = 0
      for i, t in enumerate(p):
        mapping[chr(ord('a')+i)] = t
      
      for signal in signals:
        if ''.join(sorted([mapping[c] for c in signal])) not in vals:
          break
        count += 1

      if count == 10:
        print
        result += get_number(tokens)
  return result


if __name__ == '__main__':
  solve()