import math

RESULT_COL = 4
OUTLOOK_COL = 0
TEMP_COL = 1
HUM_COL = 2
WIND_COL = 3
TOTAL_COL = 5
TOTAL_CONDITION = 4
NO = 0
YES = 1
BASE = 2
OUTLOOK_RANGE = 3
TEMP_RANGE = 3
HUM_RANGE = 2
WIND_RANGE = 2


#convert the string file into a table of integers that represent the states
def convert_table(file:str):
  lst = []
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      entry = []
      words = line.split('  ')
      for word in words:
        word = word.lower().strip()
        if word == 'sunny' or word == 'hot' or word == 'normal' or word == 'weak' or word == 'yes':
          entry.append(1)
        elif word == 'overcast' or word == 'mild' or word == 'high' or word == 'strong':
          entry.append(2)
        elif word == 'no':
          entry.append(0)
        else:
          entry.append(3) 
      lst.append(entry)
  return lst


def entropy(p:float):
  if p == 0 or p == 1:
    return 0
  return (p * math.log(p, BASE) + (1-p) * math.log((1-p), BASE)) * (-1)


def p_cond(table, condition, column):
  y = len([entry for entry in table if entry[column] == condition and entry[RESULT_COL] == YES])
  n = len([entry for entry in table if entry[column] == condition and entry[RESULT_COL] == NO])
  p = y/(y+n)
  return entropy(p)

def sum_entr(table, cond_cnt, column):
  sum = 0
  for i in range(cond_cnt):
    p_condition = len([entry for entry in table if entry[column] == i+1]) / len(table)
    sum += p_cond(table, i + 1, column) * p_condition
  return sum

def main():
  table = convert_table('table')
  p_true = len([entry for entry in table if entry[RESULT_COL] == YES])/len(table)
  init_entropy = entropy(p_true)
  outlook_entropy = sum_entr(table, OUTLOOK_RANGE, OUTLOOK_COL)
  temp_entropy = sum_entr(table, TEMP_RANGE, TEMP_COL)
  hum_entropy = sum_entr(table, HUM_RANGE, HUM_COL)
  wind_entropy = sum_entr(table, WIND_RANGE, WIND_COL)
  print('largest gain: ', max(outlook_entropy, temp_entropy, hum_entropy,wind_entropy ))
  print(init_entropy, 
  '\noutlook: ', init_entropy - outlook_entropy, 
  '\ntemperature: ', init_entropy - temp_entropy, 
  '\nhumidity: ', init_entropy - hum_entropy, 
  '\nwind: ', init_entropy - wind_entropy)

if __name__ == '__main__':
  main()