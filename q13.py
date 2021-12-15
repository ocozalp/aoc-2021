def solve():
  with open('input/q13.txt', 'r') as f:
    lines = list(map(lambda s: s.strip(), f.readlines()))
  dots = set()
  for line in lines:
    if len(line) == 0:
      break
    c, r = map(int, line.split(','))
    dots.add((r, c))

  folds = list()
  for line in lines[len(dots)+1:]:
    line = line[len('fold along '):]
    horizontal = line[0] == 'y'
    idx = int(line[2:])
    folds.append((horizontal, idx))

  print('Answer 1:', solve1(dots, folds))
  print('Answer 2:', solve2(dots, folds))


def fold(dots, folds):
  for horizontal, fold_index in folds:
    new_dots = set()
    for r, c in dots:
      if horizontal and r > fold_index:
        r = fold_index - (r - fold_index)
      elif not horizontal and c > fold_index:
        c = fold_index - (c - fold_index)

      new_dots.add((r, c))
    dots = new_dots
  return dots


def solve1(dots, folds):
  return len(fold(dots, folds[:1]))
  

def print_dots(dots):
  minr = min([d[0] for d in dots])
  maxr = max([d[0] for d in dots])
  minc = min([d[1] for d in dots])
  maxc = max([d[1] for d in dots])

  for r in range(minr, maxr+1):
    chars = []
    for c in range(minc, maxc+1):
      chars.append('#' if (r, c) in dots else '.')
    print(''.join(chars))


def solve2(dots, folds):
  new_dots = fold(dots, folds)
  print_dots(new_dots)


if __name__ == '__main__':
  solve()