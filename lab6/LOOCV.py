class Point:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y
    self.dist = 0
  
  def __repr__(self) -> str:
    return f'({self.x}, {self.y})'
  
def KNN(points: 'list[Point]', k:int, x:float) -> float:
  for point in points:
    point.dist = abs(x - point.x)
  points.sort(key=lambda point:point.x)
  sum = 0
  for point in points[:k]:
    sum += point.y
  return sum/k


def LOOCV(points: 'list[Point]', k:int) -> float:
  MSE = 0
  for i in range(len(points)):
    current = points[i]
    rest_list = points[:i] + points[i+1:]
    err = current.y - (KNN(rest_list, k, current.x))
    MSE += err * err
  return MSE / len(points)

def main():
  k = int(input('k: '))
  p1 = Point(1, 1)
  p2 = Point(2, 2)
  p3 = Point(0, 0)
  p4 = Point(4, 4)
  p5 = Point(3, 3)
  p_list = []
  p_list.append(p1)
  p_list.append(p2)
  p_list.append(p3)
  p_list.append(p4)
  p_list.append(p5)
  print(LOOCV(p_list, k))

main()