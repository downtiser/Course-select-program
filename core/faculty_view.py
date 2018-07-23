#Downtiser
import sys
import os
import time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import data_handler
from core.class_mod import *

def choose_grade(faculty):
    '''
    the function is used for faculty to choose a grade in her grade list
    :param faculty:
    :return:
    '''
    while True:
        for i, item in enumerate(faculty.grade):
            print(i + 1, item.grade_name)
        user_choice = input('please choose your grade>>>')
        if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(faculty.grade):
            return faculty.grade[int(user_choice)-1]
        else:
            print('invalid input!')
            return False


def look_over_student_list(grade):
    '''
    the function is used to exhibit the student list of a grade
    :param grade:
    :return:
    '''
    data_handler.load_data(grade.grade_name)
    for i,item in enumerate(grade.grade_student):
        print(i+1,item.name)
    time.sleep(2)



def mark_operation(grade):
    '''
    the function is used to let faculty to operate the student's mark, such as add mark, modify
    the mark(will be achieved in future)
    :param grade:
    :return:
    '''
    while True:
        user_exit_choice = input('input q to quit or input any other value to continue to manage your student>>>')
        if user_exit_choice == 'q':
            print('successfully quit')
            return 0
        data_handler.load_data(grade.grade_name)
        for i, item in enumerate(grade.grade_student):
            print(i + 1, item.name)

        user_choice = input('please choose a student to operate>>>')
        if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(grade.grade_student):
            mark = input('please input the mark you want to add>>>')
            student = grade.grade_student[int(user_choice)-1]
            student.mark_add(mark)
            grade.grade_student[int(user_choice) - 1] = student
            for faculty in grade.grade_faculty:
                for i, grade_obj in enumerate(faculty.grade):
                    if grade_obj.grade_name == grade.grade_name:
                        faculty.grade[i] = grade
                        data_handler.dump_info(faculty.name,faculty)
            data_handler.dump_info(grade.grade_name,grade)
            print('Add mark successfully!')
        else:
            continue







faculty_sever_dict = {
    '1':look_over_student_list,
    '2':mark_operation
}


def faculty_port():
    '''
    the function is used to provide a port for faculty to manage his grade
    and students
    :return:
    '''
    while True:
        user_exit_choice = input('input q to quit or input any other value to continue to manage>>>')
        if user_exit_choice == 'q':
            print('successfully quit')
            break
        user_name = input('please input your name>>>')
        if os.path.isfile(BASE_DIR+"\\data\\%s"%user_name) == False:
            print('invalid name,please check your input!')
            continue
        faculty = data_handler.load_data(user_name)
        grade = choose_grade(faculty)
        if grade == False:
            continue
        while True:
            user_exit_choice2 = input('input q to quit or input any other value to continue to manage your grade>>>')
            if user_exit_choice2 == 'q':
                break
            print('----Sever list----')
            print('1 look over student list')
            print('2 mark operation')
            user_choice = input('please choose a sever>>>')
            if user_choice in faculty_sever_dict:
                faculty_sever_dict[user_choice](grade)
            else:
                print('invalid input!')





