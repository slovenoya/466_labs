import math

class Point:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y


def min(a, b):
  return a if a < b else b


def dist(a : 'Point', b:'Point'):
  dx = a.x - b.x
  dy = a.y - b.y
  return math.sqrt(dx*dx + dy*dy).__round__(1)


def get_dist_matrix(points: 'list[Point]') -> 'list[list[float]]':
  matrix = []
  for point in points:
    row = []
    for point_other in points:
      row.append(dist(point, point_other))
    matrix.append(row)
  return matrix


def get_smallest_position(matrix: 'list[list[float]]') -> 'tuple[int, int]':
  smallest = math.inf
  smallest_pos = (0, 0)
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if not i == j and smallest > matrix[i][j] and i > j:
        smallest = matrix[i][j]
        smallest_pos = (i, j)
  return smallest_pos


def print_matrix(matrix, label):
  print(' '*15 + str(label))
  for i in range(len(matrix)):
    print(str(label[i]).ljust(15), str(matrix[i]).ljust(15))


def matrix_transform(matrix:'list[list[float]]', merge:'tuple[int, int]', label:'list[str]'):
  a, b = merge
  label[min(a, b)] = label[min(a, b)] + ',' + label[max(a, b)]
  del label[max(a, b)]
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if j == a and not i == a:
        matrix[i][j] = min(matrix[i][j], matrix[i][b])
      if not j == a and i == b:
        matrix[i][j] = min(matrix[a][j], matrix[b][j])
  del matrix[max(a, b)]
  for i in range(len(matrix)):
    del (matrix[i])[max(a, b) - 1]
  for i in range(len(matrix)):  
    matrix[i][i] = 0.0


def main():
  A = Point(1, 1)
  B = Point(2, 1)
  C = Point(0, 1)
  D = Point(4, 1)
  E = Point(4, 2)
  F = Point(3, 1)
  points = [A, B, C, D, E, F]
  label = ['A', 'B', 'C', 'D', 'E', 'F']
  dist_matrix = get_dist_matrix(points)
  print_matrix(dist_matrix, label)
  while not len(dist_matrix) == 1:
    matrix_transform(dist_matrix, get_smallest_position(dist_matrix), label)
    print_matrix(dist_matrix, label)

if __name__ == '__main__':
  main()