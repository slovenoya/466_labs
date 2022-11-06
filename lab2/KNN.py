from matplotlib.colors import CenteredNorm


class Point:
  def __init__(self, x, y) -> None:
    self.x = x 
    self.y = y

  def __eq__(self, __o: object) -> bool:
    if not __o or not isinstance(__o, Point):
      return False
    return self.x == __o.x and self.y == __o.y
  
  def __repr__(self) -> str:
    return f'({self.x}, {self.y})'

  def __hash__(self) -> int:
    return hash((self.x, self.y))

  def get_dist(self, p: 'Point') -> float:
    x = self.x - p.x
    y = self.y - p.y
    return x * x + y * y

def get_center(points: 'list[Point]') -> 'Point':
  x = 0
  y = 0
  for point in points:
    x += point.x
    y += point.y
  return Point(x / len(points), y / len(points))

def find_closest(point: 'Point', point_lst: 'list[Point]') -> 'Point':
  shortest = point.get_dist(point_lst[0])
  closest = point_lst[0]
  for center in point_lst:
    if point.get_dist(center) < shortest:
      shortest = point.get_dist(center)
      closest = center
  return closest

def cluster(centers: 'list[Point]', points: 'list[Point]') -> 'list[Point]':
  clusters = dict()
  for center in centers:
    clusters[center] = []
  for point in points:
    closest_center = find_closest(point, centers)
    clusters[closest_center].append(point)
  for i in range(len(centers)):
    centers[i] = get_center(clusters[centers[i]])
  return centers

def KNN(centers: 'list[Point]', points:'list[Point]') -> 'list[Point]':
  old_centers = centers
  while True:
    new_centers = cluster(centers, points)
    if new_centers == old_centers:
      return new_centers
    old_centers = new_centers

def main():
  centers = [Point(1, 5), Point(2, 5)]
  points = [Point(1, 1), Point(2, 1), Point(0, 1), Point(4, 1), Point(4, 2), Point(3, 1)]
  clusted_centers = KNN(centers, points)
  print(clusted_centers)

if __name__ == '__main__':
  main()