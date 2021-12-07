from math import sqrt


def solve():
  with open('input/q7.txt', 'r') as f:
    crabs = list(map(int, f.readline().split(',')))

  print('Answer 1:', solve1(crabs[:]))
  print('Answer 2:', solve2(crabs[:]))


def solve1(crabs):
  crabs.sort()
  median = crabs[len(crabs)//2]
  return sum(map(lambda n: abs(n-median), crabs))


def solve2(crabs):
  crabs.sort()
  def cost(ref_point):
    return sum(map(lambda x: (x*(x+1))/2, map(lambda x: abs(x-ref_point), crabs)))

  left = min(crabs)
  right = max(crabs)
  min_cost = cost(right+1)
  while left <= right:
    mid = left + (right-left)//2
    c = cost(mid)
    if c < min_cost:
      min_cost = c
    cost_plus_one = cost(mid + 1)
    if cost_plus_one < c:
      left = mid + 1
    else:
      right = mid - 1
  return min_cost


if __name__ == '__main__':
  solve()