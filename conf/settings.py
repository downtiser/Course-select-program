#Downtiser
import sys
import os
'''
  fundamental data base settings
'''
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_base = {
    'base_engine':'file storage',
    'base_name':'my file',
    'base_path':BASE_DIR+'\\data'
}