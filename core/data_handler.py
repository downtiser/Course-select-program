#Downtiser
#Downtiser
import pickle
import os
import sys
import pickle
from core.class_mod import *
from conf import settings




data_path=settings.data_base['base_path']


def dump_info(obj_file,item):
    '''
    to dump object from database
    :param obj_file:
    :param item:
    :return:
    '''
    path = data_path + '\\%s' % obj_file
    f = open(path,'wb')
    f.write(pickle.dumps(item))
    f.flush()
    f.close()









def load_data(obj_file):
    '''
    to load object from database
    :param obj_file:
    :return:
    '''
    path=data_path+'\\%s'%obj_file
    f = open(path,'rb')
    data = pickle.loads(f.read())
    f.flush()
    f.close()
    return data



