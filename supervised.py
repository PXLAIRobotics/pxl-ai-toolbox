import os

''' 
1) Add 'test' folder next to 'train', 'valid', models'
2) In 'test', divide samples in class folders (like you did in 'train' & 'valid')
3) Add runTestSet(path_to_main_data_folder)   >>   folder that contains 'train', 'valid', 'test', ...
4) Sit back and hit 100% !

Disclaimer: it will probably break if you don't follow these rules.

Example: 
run_test('drive/My Drive/Colab Notebooks/data/Rick & Morty/', show_images=True, test_folder='test1')
'''
def run_test(path, show_images=False, test_folder='test'):
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
        img = open_image(imgpath)
        p = learn.predict(img)
        if show_images:
          img.show(title=p)
        prediction = str(p[0])
        if prediction == folder:
          correct += 1
        count += 1
  print("Result for test: " + str(correct) + "/" + str(count) + "(" + str(correct/count) + ")")
  # TODO show more results?
    