from easy_vqa import get_train_questions, get_test_questions, get_train_image_paths, get_test_image_paths, get_answers

def test_all_questions():
  train_qs, train_answers, train_image_ids = get_train_questions()
  test_qs, test_answers, test_image_ids = get_test_questions()
  assert len(train_qs) > 0 and len(test_qs) > 0
  assert len(train_answers) == len(train_qs) and len(test_answers) == len(test_qs)
  assert len(train_image_ids) == len(train_qs) and len(test_image_ids) == len(test_qs)

def test_all_image_paths():
  train_im_paths = get_train_image_paths()
  test_im_paths = get_test_image_paths()
  assert len(train_im_paths) > 0
  assert len(test_im_paths) > 0

def test_answers():
  answers = get_answers()
  assert len(answers) > 0
