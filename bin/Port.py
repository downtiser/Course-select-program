#Downtiser
import sys
import os
import time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import data_handler
from core.class_mod import *
from core import faculty_view
from core import manage_view
from core import student_view
view_dict = {
    '1':manage_view.manage_port,
    '2':faculty_view.faculty_port,
    '3':student_view.student_port
}

def run():
    '''
    when user choose to run the program,the function will open three port for different user to
    operate
    :return:
    '''
    while True:
        user_exit_choice = input('input q to quit or input any other value to continue>>>')
        if user_exit_choice == 'q':
            exit('exit successfully!')
        print('----View list----')
        print('1 manage view')
        print('2 faculty view')
        print('3 student view')
        user_choice = input('please choose the view>>>')
        if user_choice in view_dict:
            view_dict[user_choice]()
        else:
            print('invalid input')
            continue


while True:
    user_exit_choice = input('input q to quit or input any other value to continue>>>')
    if user_exit_choice == 'q':
        exit('exit successfully!')
    run()