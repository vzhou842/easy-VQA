# easy-vqa

[![Build Status](https://travis-ci.com/vzhou842/easy-vqa.svg?branch=master)](https://travis-ci.com/vzhou842/easy-vqa)
![PyPI](https://img.shields.io/pypi/v/easy-vqa)

The official repository for the easy-VQA dataset. Contains:
- the official Python package for the dataset
- the source code for generating the dataset

## Installing the Package

`pip install easy-vqa`

## Using the Package

### Questions

Each question has 3 parts:
- the question text
- the answer
- the image ID

The question getters return corresponding arrays for each of the 3 parts:

```python
from easy_vqa import get_train_questions, get_test_questions

train_questions, train_answers, train_image_ids = get_train_questions()
test_questions, test_answers, test_image_ids = get_test_questions()

# Question 0 is at index 0 for all 3 arrays:
print(train_questions[0]) # what shape does the image contain?
print(train_answers[0])   # circle
print(train_image_ids[0]) # 0
```

### Images

The image path getters return dicts that map image ID to absolute paths that can be used to load the image.

```python
from easy_vqa import get_train_image_paths, get_test_image_paths

train_image_paths = get_train_image_paths()
test_image_paths = get_test_image_paths()

print(train_image_paths[0]) # ends in easy_vqa/data/train/images/0.png
```

### Answers

The answers getter returns an array of all possible answers.

```python
from easy_vqa import get_answers

answers = get_answers()

print(answers) # ['teal', 'brown', 'black', 'gray', 'yes', 'blue', 'rectangle', 'yellow', 'triangle', 'red', 'circle', 'no', 'green']
```

## Generating the Dataset

The easy-VQA dataset was generated by running

```shell
python gen_data/generate_data.py
```

which writes to the `easy_vqa/data/` directory. Be sure to install the dependencies for dataset generation running `generate_data.py`:

```shell
pip install -r gen_data/requirements.txt
```

If you want to generate a larger easy-VQA dataset, simply modify the `NUM_TRAIN` and `NUM_TEST` constants in `generate_data.py`. Otherwise, if you want to modify the dataset itself, the files and code in the `gen_data/` directory should be pretty self-explanatory.
