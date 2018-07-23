#Downtiser
import sys
import os
import time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import data_handler
from core.class_mod import *
student_school_dict = {
    '1':'Beijing_school',
    '2':'Shanghai_school'
}
def query_mark():
    '''
    the function is used to query a student's mark through his grade and his name
    :return:
    '''
    while True:
        user_exit_choice = input('input q to quit or input any other value to continue to choose your grade>>>')
        if user_exit_choice == 'q':
            print('successfully quit')
            break
        print('----School list----')
        print('1 %s' % student_school_dict['1'])
        print('2 %s' % student_school_dict['2'])
        user_choice = input('please choose school>>>')
        if user_choice in student_school_dict:
            student_school = data_handler.load_data(student_school_dict[user_choice])
        else:
            print('invalid input!')
            continue
        for i,item in enumerate(student_school.grade):
            print(i+1,item.grade_name)
        user_choice2 = input('please choose a grade>>>')
        if user_choice2.isdigit() and int(user_choice2) > 0 and int(user_choice2) <= len(student_school.grade):
            student_grade = data_handler.load_data(student_school.grade[int(user_choice2)-1].grade_name)
            while True:
                user_exit_choice = input('input q to quit or input any other value to continue to Query>>>')
                if user_exit_choice == 'q':
                    print('successfully quit')
                    break
                student_name = input('please input your name>>>')
                state = False
                for i in student_grade.grade_student:
                    if i.name == student_name:
                        state = True
                        student_obj = i
                        print(student_obj.mark)
                        break
                if state == False:
                    print('you are not in the grade,please check your input')





def pay_tuition(course):
    '''
    the function is used to pay tuition and verify the student
    :param course:
    :return:
    '''
    pay_choice = input('Are you sure to pay %s $ for the %s course? input y to confirm or input any other value to quit!'%(course.course_price,course.course_name))
    if pay_choice == 'y':
        print('pay success!')
        return True
    else:
        print('you have cancel the transaction!')
        return False




def select_course(student_school):
    '''
    the function is used to bind the student with the course
    :param student_school:
    :return:
    '''
    while True:
        print('----Course list----')
        for i, item in enumerate(student_school.course):
            print(i + 1, item.course_name, item.course_price,'$', item.course_period)
        user_choice = input('please choose a course>>>')
        if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(student_school.course):
            course_obj = student_school.course[int(user_choice) - 1]
            return course_obj
        else:
            print('invalid input!')
            continue



def select_grade(student_school):
    '''
    the function is used to exhibit the grade of the school for student to choose
    :param student_school:
    :return:
    '''
    while True:
        print('----Grade list----')
        for i, item in enumerate(student_school.grade):
            print(i + 1, item.grade_name)
        user_choice2 = input('please choose a grade to join>>>')
        if user_choice2.isdigit() and int(user_choice2) > 0 and int(user_choice2) <= len(student_school.grade):
            grade_obj = student_school.grade[int(user_choice2) - 1]
            return grade_obj,int(user_choice2)
        else:
            print('invalid input!')
            continue



def student_port():
    '''
    the function is used to provide a port for student to query his mark and
    enroll in.
    :return:
    '''
    while True:
        user_exit_choice0 = input('input q to quit or input any other value to continue to join our course!>>>')
        if user_exit_choice0 == 'q':
            print('successfully quit')
            break
        sever_dict = {
            '1':'query your mark',
            '2':'enroll in!'
        }
        print('----Sever list----')
        print('1 query your mark')
        print('2 enroll in!')

        student_choice = input('please choose a sever>>>')
        if student_choice in sever_dict:
            if student_choice == '1':
                query_mark()
            else:
                while True:
                    user_exit_choice = input('input q to quit or input any other value to continue to join our course!>>>')
                    if user_exit_choice == 'q':
                        print('successfully quit')
                        break

                    print('----School list----')
                    print('1 %s'%student_school_dict['1'])
                    print('2 %s'%student_school_dict['2'])
                    user_choice = input('please choose school>>>')
                    if user_choice in student_school_dict:
                        student_school = data_handler.load_data(student_school_dict[user_choice])
                    else:
                        print('invalid input!')
                        continue
                    course_obj = select_course(student_school)
                    grade_obj,user_grade_choice = select_grade(student_school)
                    name = input('please input your name>>>')
                    age = input('please input your age>>>')
                    sex = input('please input your sex>>>')
                    mobile_phone = input('please input your mobile phone number>>>')
                    state = pay_tuition(course_obj)
                    if state == False:
                        continue
                    student = Student(name,age,sex,mobile_phone,student_school)
                    student.change_state(state)
                    grade_obj.bind_student(student)
                    student.bind_grade(grade_obj)
                    student_school.grade[user_grade_choice-1] = grade_obj
                    data_handler.dump_info(grade_obj.grade_name,grade_obj)
                    data_handler.dump_info(student_school.name,student_school)
                    for faculty in grade_obj.grade_faculty:
                        for i,grade in enumerate(faculty.grade):
                            if grade.grade_name == grade_obj.grade_name:
                                faculty.grade[i] = grade_obj
                                data_handler.dump_info(faculty.name,faculty)
                    print('Successfully enroll in!')
        else:
            print('invalid input!')
            continue









