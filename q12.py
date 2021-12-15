from collections import defaultdict


def solve():
  with open('input/q12.txt', 'r') as f:
    lines = list(map(lambda s: tuple(s.strip().split('-')), f.readlines()))
  graph = construct_graph(lines)

  print('Answer 1:', solve1(graph))
  print('Answer 2:', solve2(graph))


def construct_graph(lines):
  graph = defaultdict(set)
  for line in lines:
    node1, node2 = line
    graph[node1].add(node2)
    graph[node2].add(node1)
  return graph


def solve1(graph):
  def count(current_node, visited):
    if current_node == 'end':
      return 1
    
    is_small_cave = 'a' <= current_node[0] <= 'z'
    if is_small_cave:
      if current_node in visited:
        return 0
      visited = visited.union(set([current_node]))
    
    result = 0
    for n in graph[current_node]:
      result += count(n, visited)
    return result
  
  return count('start', set())


def solve2(graph):
  def count(current_node, visited, visited_twice=None):
    if current_node == 'end':
      return 1
    
    if current_node == 'start' and current_node in visited:
      return 0

    is_small_cave = 'a' <= current_node[0] <= 'z'
    added=False
    if is_small_cave:
      if current_node == visited_twice:
        return 0

      if current_node in visited:
        if visited_twice is not None:
          return 0
        visited_twice = current_node
      else:
        added=True
        visited.add(current_node)
    
    result = 0
    for n in graph[current_node]:
      result += count(n, visited, visited_twice)

    if added:
      visited.remove(current_node)

    return result
  
  return count('start', set())


if __name__ == '__main__':
  solve()