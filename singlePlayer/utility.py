import random
from . import filter_question_data as filter_qa
from inputimeout import inputimeout, TimeoutOccurred

def init_game_round_variables():
  
  next_question = True
  correct_answer = None
  question = None 
  user_answers = None
  options = None
  score = 0
  
  game_round_state = {
    "next_question": next_question, 
    "correct_answer": correct_answer, 
    "question": question, 
    "options": options, 
    "user_answers": user_answers,
    "score": score
  }

  return game_round_state 

def user_input(entry):
  timer = {
    "very_slow": 35, "slow": 30, "medium": 27,
    "fast": 20, "very_fast": 15, "untimed": 999999999999
  }

  point_system = {
    "very_slow": 2, "slow": 5, "medium": 10,
    "fast": 15, "very_fast": 20, "untimed": 2
  }


  speed = entry.speed
  level = entry.lvl
  arithmetic  = entry.arithmetic
  difficulty = entry.difficulty

  if speed not in timer:
    raise Exception("Invalid input speed")
  countdown, scoring = timer[speed], point_system[speed] 

  settings = {
    "level": level, 
    "arithmetic": arithmetic, 
    "difficulty": difficulty, 
    "speed": speed, 
    "countdown": countdown, 
    "scoring": scoring
  }
  return settings

def initialize_question(data, game_round_state):
    
  data = filter_qa.filter_data(data)
  #randomly pick a correct answer in the data
  answer_index = random.randint(0, len(data) -1)  
  key_list = list(data)
  correct_answer = key_list[answer_index]
  game_round_state["correct_answer"] = correct_answer

  #randomly pick a question from the correct answer 
  question_index = random.randint(0, len(data[correct_answer]) -1 ) 
  question = data[correct_answer][question_index]
  game_round_state["question"] = question

  #randomly pick two wrong answer as options for the user 
  while True:
    option_1 = random.randint(0, len(data) -1)
    option_2 = random.randint(0, len(data) -1)
    if option_1 != answer_index and option_2 != answer_index:
      break
  option_1 = key_list[option_1]
  option_2 = key_list[option_2]

  # Randomly place the 2 wrong answer along with the correct answer in a list
  options = [option_1, option_2]
  options.insert(random.randint(0, len(options) - 1), correct_answer)
  game_round_state["options"] = options 
  
  return game_round_state