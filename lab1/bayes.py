RESULT_COL = 4
TOTAL_COL = 5
TOTAL_CONDITION = 4
NO = 0
YES = 1

# take inputs from user
def take_input() -> 'tuple[int, int, int, int]':
  try: 
    weather = int(input('How\'s weather today? (1. sunny 2. overcast 3. rain) '))
    temperature = int(input('How\'s temperature today? (1. hot 2. mild 3. cool) '))
    humidity = int(input('How\'s humidity today? (1. normal 2. high) '))
    wind = int(input('How\'s wind today? (1. weak 2. strong) '))
    if weather < 1 or weather > 3 or temperature < 1 or temperature > 3 or humidity < 1 or humidity > 2 or wind < 1 or wind > 2:
      print('input error!')
      return take_input()
  except ValueError:
    print('give me a number! ')
    return take_input()
  return (weather, temperature, humidity, wind)

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

def get_possiblity(table:'list[list[int]]', condition:int, column: int, state: int) -> float:
  hit = [entry for entry in table if entry[RESULT_COL] == state and entry[column] == condition]
  states = [entry for entry in table if entry[RESULT_COL] == state]
  return len(hit) / len(states)

def get_bayes_naive_possiblity(condition: 'tuple[int, int, int, int]', table:'list[list[int]]', state: int) -> float:
  not_state = YES if state == NO else NO
  yes = len([entry for entry in table if entry[RESULT_COL] == state]) / len(table)
  no = len([entry for entry in table if entry[RESULT_COL] == not_state]) / len(table)
  result = 0
  for i in range(TOTAL_CONDITION):
    yes *= get_possiblity(table, condition[i], i, state)
    no *= get_possiblity(table, condition[i], i, not_state)
  try:
    result = yes / (yes + no)
  except ZeroDivisionError:
    print('divided by zero')
  return result

def main():
  table = convert_table('table')
  user_input = take_input()
  p_yes = get_bayes_naive_possiblity(user_input, table, YES)
  print(f'possibilty for play tennis is {p_yes}')


if __name__ == '__main__':
  main()