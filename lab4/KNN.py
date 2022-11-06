import math

from numpy import average

class Point:
  def __init__(self, x, y) -> None:
    self.x = x 
    self.y = y
    self.dist = 0

def KNN(points: 'list[Point]', k:float, x:float) -> float:
  for point in points:
    point.dist = abs(x - point.x)
  points.sort(key=lambda point:point.x)
  sum = 0
  for point in points[:k]:
    sum += point.y
  return sum/k

def main():
  while True:
    k = int(input('give me k: '))
    x = int(input('give me x: '))
    if k > 1 and k < 5 and x >= 0 and x <= 4:
      break
    print('invalid value for x or k')
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

  print(KNN(p_list, k, x))

main()