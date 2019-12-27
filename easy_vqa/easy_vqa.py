import os
from os import path
import json

BASE_PATH = path.dirname(__file__)

def read_questions(rel_path):
  with open(path.join(BASE_PATH, rel_path), 'r') as file:
    qs = json.load(file)
  texts = [q[0] for q in qs]
  answers = [q[1] for q in qs]
  image_ids = [q[2] for q in qs]
  return texts, answers, image_ids

def read_image_paths(rel_dir):
  ims = {}
  dir_path = path.join(BASE_PATH, rel_dir)
  for filename in os.listdir(dir_path):
    if filename.endswith('.png'):
      image_id = int(filename[:-4])
      ims[image_id] = path.join(dir_path, filename)
  return ims

#####

def get_train_questions():
  return read_questions('data/train/questions.json')

def get_test_questions():
  return read_questions('data/test/questions.json')

def get_train_image_paths():
  return read_image_paths('data/train/images')

def get_test_image_paths():
  return read_image_paths('data/test/images')

def get_answers():
  with open(path.join(BASE_PATH, 'data/answers.txt'), 'r') as answers_file:
    return [a.strip() for a in answers_file]
