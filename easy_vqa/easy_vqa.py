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
  return (texts, answers, image_ids)

train_qs, train_answers, train_image_ids = read_questions('data/train/questions.json')
test_qs, test_answers, test_image_ids = read_questions('data/test/questions.json')

def read_images(rel_dir):
  ims = {}
  dir_path = path.join(BASE_PATH, rel_dir)
  for filename in os.listdir(dir_path):
    if filename.endswith('.png'):
      image_id = int(filename[:-4])
      ims[image_id] = path.join(dir_path, filename)
  return ims

train_im_paths = read_images('data/train/images')
test_im_paths = read_images('data/test/images')

with open(path.join(BASE_PATH, 'data/answers.txt'), 'r') as answers_file:
  all_answers = [a.strip() for a in answers_file]

def get_train_data():
  return train_qs, train_answers, train_image_ids, train_im_paths

def get_test_data():
  return test_qs, test_answers, test_image_ids, test_im_paths

def get_answers():
  return all_answers
