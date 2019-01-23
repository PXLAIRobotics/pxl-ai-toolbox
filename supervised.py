import os
from fastai.vision import image

''' 
1) Add 'test' folder next to 'train', 'valid', models'
2) In 'test', divide samples in class folders (like you did in 'train' & 'valid')
3) Add runTestSet(path_to_main_data_folder)   >>   folder that contains 'train', 'valid', 'test', ...
4) Sit back and hit 100% !

Disclaimer: it will probably break if you don't follow these rules.

Example: 
run_test('drive/My Drive/Colab Notebooks/data/Rick & Morty/', show_images=True, test_folder='test1')
'''
def run_test(model, path, show_images=False, test_folder='test'):
  count = 0
  correct = 0
  if not path[-1] == '/':
    path += '/'
  testpath = path + test_folder + '/'
  for folder in os.listdir(testpath):
    folderpath = testpath+folder
    if os.path.isdir(folderpath):
      for img in os.listdir(folderpath):
        imgpath = folderpath + '/' + img
        img = image.open_image(imgpath)
        p = model.predict(img)
        if show_images:
          img.show(title=p)
        prediction = str(p[0])
        if prediction == folder:
          correct += 1
        count += 1
  print("Result for test: " + str(correct) + "/" + str(count) + "(" + str(correct/count) + ")")
  # TODO show more results?

import os, random, shutil

# Function can be executed when new data is added to 'samples', data will be added to already exisiting sets
#
# base dir must have 'samples' folder with images, thewe will be divided in train, validation & test set
# divide contains division of (train, validation, test) set, like (0.8, 0.1, 0.1)
# keep_samples True means samples will be COPIED instead of MOVED (so they also remain in the sample folder) TODO test this

# TODO keep class folders intact or generate class folders based on filename
def splitSamples(base, divide=(0.8,0.1,0.1), keep_samples=False):
  if not base[-1] == "/":
    base += "/"
    
  # create folders if they don't exist already
  train = os.path.join(base, "train")
  valid = os.path.join(base, "valid")
  test = os.path.join(base, "test")
  sample = os.path.join(base, "samples")
  
  print(str(sample))
  
  if not os.path.exists(sample):
    print("Nothing here...")
    return
    
  if not os.path.exists(train):
    os.makedirs(train)
  if not os.path.exists(valid):
    os.makedirs(valid)
  if not os.path.exists(test):
    os.makedirs(test)
    
  numSamples = len(os.listdir(sample))
  print("# samples: " + str(numSamples))
    
  for img in os.listdir(sample):
    r = random.uniform(0, 1)
    target = train
    if r > divide[0] + divide[1]:
      target = test
    elif r > divide[0]:
      target = valid      
      
    orig_full_path = os.path.join(sample, img)
    new_full_path = os.path.join(target, img)
    print("Move to " + new_full_path)
    if keep_samples:
      copyfile(orig_full_path, new_full_path)
    else:
      os.rename(orig_full_path, new_full_path)
      
  return (train, valid, test)


# counts number of features in all subfolder in a set (e.g. train set)
def count_features(path):
  count = 0
  for subdir in os.listdir(path):
    subdir_path = os.path.join(path, subdir)
    for sp in os.listdir(subdir_path):
      count += 1
  return count