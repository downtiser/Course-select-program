#Downtiser
import sys
import os
import time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import data_handler
from core.class_mod import *

school_dict = {
    '1':'Beijing_school',
    '2':'Shanghai_school'
}

course_dict = {
    '1':'Python',
    '2':'Linux',
    '3':'Go'

}






def create_faculty(user_school):
    '''
    the function is used to create a faculty object through the class Faculty
    :param user_school:
    :return:
    '''
    while True:
        user_exit_choice = input('input q to quit or input any other value to continue to create a faculty>>>')
        if user_exit_choice == 'q':
            break
        else:
            name = input('please input the faculty name>>>')
            age = input('please input the age>>>')
            sex = input('please input the sex>>>')
            salary = input('please input the salary>>>')
            print('----Course list----')
            for i, item in enumerate(user_school.course):
                print(i + 1, item.course_name)
            user_choice = input('please choose a course to arrange a course for the faculty>>>')
            if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(user_school.course):
                course_obj = user_school.course[int(user_choice)-1]
            else:
                print('invalid input!')
                continue
            print('----Grade list----')
            for i,item in enumerate(user_school.grade):
                print(i+1,item.grade_name)
            user_choice2 = input('please choose a grade to bind with the faculty>>>')
            if user_choice2.isdigit() and int(user_choice2) > 0 and int(user_choice2) <= len(user_school.grade):
                grade_obj = user_school.grade[int(user_choice2)-1]
            else:
                print('invalid input!')
                continue
            faculty = Faculty(name,age,sex,course_obj,salary)
            faculty.bind_grade(grade_obj)
            grade_obj.bind_faculty(faculty)
            user_school.grade[int(user_choice2)-1] = grade_obj
            user_school.faculty_create(faculty)
            data_handler.dump_info(faculty.name,faculty)
            data_handler.dump_info(grade_obj.grade_name,grade_obj)
            data_handler.dump_info(user_school.name,user_school)
            print('create faculty successfully!')
            continue










def create_course(user_school):
    '''
    the function is used to create a course through the class Course
    :param user_school:
    :return:
    '''
    while True:
        user_exit_choice = input('input q to quit or input any other value to continue>>>')
        if user_exit_choice == 'q':
            break
        else:
            print('----Course list----')
            print('1 python')
            print('2 Linux')
            print('3 Go')
            user_choice2 = input('please choose a course to create>>>')
            if user_choice2 in course_dict:
                user_course_name = course_dict[user_choice2]
                user_exit_choice2 = input('input q to quit or input any other value to continue>>>')
                if user_exit_choice2 == 'q':
                    print('You will back to the last menu!')
                    time.sleep(1.5)
                    continue
                course_price = input('please input the course price>>>')
                course_outline = input('please input the course period>>>')
                course = Course(user_course_name,course_price,course_outline)
                user_school.course_create(course)
                data_handler.dump_info(user_school.name, user_school)
                print('Create course successfully')
            else:
                print('invalid input!')
                continue








def create_grade(user_school):
    '''
    the function is used to create a grade object through class Grade
    :param user_school:
    :return:
    '''
    while True:
        user_exit_choice = input('input q to quit or input any other value to continue to choose a course to create grade>>>')
        if user_exit_choice == 'q':
           break
        else:
            print('----Course list----')
            for i,item in enumerate(user_school.course):
                print(i+1,item.course_name)
            user_choice = input('please choose a course to create a grade>>>')
            if user_choice.isdigit() and int(user_choice)>0 and int(user_choice)<=len(user_school.course):
                course_obj = user_school.course[int(user_choice)-1]
                user_exit_choice2 = input('input b to back or input any other value to continue>>>')
                if user_exit_choice2 == 'b':
                    continue
                grade_name = input('please input the grade name>>>')
                grade = Grade(grade_name,course_obj)
                user_school.grade_create(grade)
                data_handler.dump_info(user_school.name,user_school)
                data_handler.dump_info(grade.grade_name,grade)
                print('Create grade successfully')
                continue
            else:
                print('invalid input!')
                continue














server_dict = {
    '1':create_course,
    '2':create_grade,
    '3':create_faculty
}


def manage_port():
    '''
    the function is the port for user to create object
    :return:
    '''
    while True:
        user_exit_choice = input('input q to quit or input any other value to continue to manage>>>')
        if user_exit_choice == 'q':
            exit('successfully quit')
        print('----School list----')
        print('1 Beijing_school')
        print('2 Shanghai_school')
        user_choice = input('please choose school>>>')
        if user_choice in school_dict:

            while True:
                user_exit_choice2 = input('input q to quit or input any other value to continue>>>')
                if user_exit_choice2 == 'q':
                    break
                print('----Server list----')
                print('1 Create course')
                print('2 Create grade')
                print('3 Create faculty')
                user_choice2 = input('please choose a server>>>')
                if user_choice2 in server_dict:
                    user_school = data_handler.load_data(school_dict[user_choice])
                    server_dict[user_choice2](user_school)
                else:
                    print('invalid input!')
                    break





