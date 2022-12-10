import os.path
from os import path

# Dataset File location
def filter_question_dataset(settings):

  directory = 'singlePlayer/questions/'

  levels = ["lvl1","lvl2", "lvl3"]
  arithmetics = ["addition","subtraction", "multiplication", "division"]
  difficulties = ["very_easy", "easy", "medium", "hard", "very_hard"]

  if settings["level"] in levels:
    level = settings["level"]
  else:
    raise Exception("Invalid input level")

  if settings["arithmetic"] in arithmetics:
    arithmetic = settings["arithmetic"]
  else:
    raise Exception("Invalid input arithmetic")
   
  if settings["difficulty"] in difficulties:
    difficulty = settings["difficulty"]
  else:
    raise Exception("Invalid input difficulty")

  directory = directory + level + "/" + arithmetic + "/" + difficulty + ".txt"

  if (path.exists(directory)):
    with open(directory) as f:
      data = f.readlines()
    return data
  else:
    raise Exception("File does not exist")

def filter_data(data):
  doc = {}

  for i in range(1, len(data)):
    line = data[i].split(":") 
    
    answer = line[0].replace(" ", "")
    question = line[1].split(",")
    
    for i in range(len(question)):
        question[i] = question[i].replace(" ", "")
    question[len(question) -1] = question[len(question) -1].replace("\n", "")    

    doc[answer] = question

  return doc