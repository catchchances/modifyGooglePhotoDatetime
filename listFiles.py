import os
import glob

path = '../Photos from 2020'
for filename in glob.glob(os.path.join(path, '*.json')):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
      # do your stuff
      print(filename)
