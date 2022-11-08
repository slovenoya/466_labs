DELTA=0.001

def compare_list(l1:list, l2:list) -> bool:
  for i in range(len(l1)):
    if abs(l1[i]-l2[i]) >= DELTA:
      return False
  return True

def marklov(y:float, P:'list[list[float]]', R:'list[float]') -> 'list[float]':
  rewards_old = R.copy()
  while True:
    rewards_new = R.copy()
    for i in range(len(rewards_old)):
      for j in range(len(P[0])):
        rewards_new[i] += P[i][j] * y * rewards_old[j]
    if compare_list(rewards_new, rewards_old):
      return rewards_new
    rewards_old = rewards_new.copy()

def main():
  lines = []
  with open('file.txt', 'r') as f:
    lines = f.readlines()
  y = float(lines[0])
  R=lines[1].split(' ')
  P=[]
  for i in range(len(R)):
    R[i] = float(R[i])
  for i in range(len(R)):
    P.append(lines[i + 2].split(' '))
  for i in range(len(P)):
    for j in range(len(P)):
      P[i][j] = float(P[i][j])

  result = marklov(y, P, R)
  for i in range(len(result)):
    result[i] = result[i].__round__(2)
  print(result)

if __name__ == '__main__':
  main()