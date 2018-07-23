#Downtiser
# from core import manage_view
import pickle
class School(object):
    '''
    the class is used to create a school and append the course and
    grade i it.
    '''
    def __init__(self,school_name,addr):
        self.name=school_name
        self.addr=addr
        self.course=[]
        self.grade=[]
        self.faculty=[]

    def grade_create(self,grade_obj):
        self.grade.append(grade_obj)


    def course_create(self,course_obj):
        self.course.append(course_obj)

    def faculty_create(self,faculty_obj):
        self.faculty.append(faculty_obj)



class Course(object):
    '''
    to create a course object with its name, price and course period
    '''
    def __init__(self,course_name,course_price,course_period):
        self.course_name=course_name
        self.course_price=course_price
        self.course_period=course_period






class Grade(object):
    '''
    the Grade class is used to create a grade object with its name, course object,
    and with a list to store the student object and another list to store the
    faculty object.
    '''
    def __init__(self,grade_name,course_obj):
        self.grade_name=grade_name
        self.grade_student=[]
        self.grade_faculty=[]
        self.course = course_obj



    def bind_student(self,student_obj):
        self.grade_student.append(student_obj)

    def bind_faculty(self,faculty_obj):
        self.grade_faculty.append(faculty_obj)


class School_Member(object):
    '''
    the parent class of Faculty class and Student Class with some mutual attributes,
    such as name, age, sex.
    '''
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def member_info(self):
        pass

class Faculty(School_Member):
    '''
    the children class of School_Member,add some attributes such as
    the faculty's salary, course, and a list to store th e faculty's
    grade object. and a private attribute to bind grade object.
    '''
    def __init__(self,name,age,sex,course_obj,salary):
        super(Faculty,self).__init__(name,age,sex)
        self.course=course_obj
        self.salary=salary
        self.grade=[]


    def bind_grade(self,grade_obj):
        self.grade.append(grade_obj)


class Student(School_Member):
    '''
    the class is used to create a student object
    '''
    def __init__(self,name,age,sex,phone,school_obj):
        super(Student,self).__init__(name,age,sex)
        self.school=school_obj
        self.grade=[]
        self.phone = phone
        self.__state =False
        self.mark = []
    def bind_grade(self,grade_obj):
        self.grade.append(grade_obj)

    def change_state(self,state):
        self.__state = state

    def verify_state(self):
        return self.__state

    def mark_add(self,mark):
        self.mark.append(mark)

    def mark_change(self,mark_no,mark):
        self.mark[mark_no] = mark

