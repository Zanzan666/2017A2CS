#Jenny Zhan

class Course:
    def __init__(self,t,m):
        self.__CourseTitle=t
        self.__MaxStudents=m
        self.__NumberOfLessons=0
        self.__CourseLesson=[]
        self.__CourseAssessment=Assessment
    def AddLesson(self,t,d,r):
        self.__NumberOfLessons=self.__NumberOfLessons+1
        self.__CourseLesson.append(Lesson(t,d,r))
    def AddAssessment(self,t,m):
        self.__CourseAssessment=Assessment(t,m)
    def OutputCourseDetails(self):
        print(self.__CourseTitle,"Maximum number: ",self.__MaxStudents)
        print('Courses:')
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].OutputLessonDetails())
        print('Assessment:')
        self.__CourseAssessment.OutputAssessmentDetails()
class Lesson:
    def __init__(self,t,d,r):
        self.__LessonTitle=t
        self.__DurationMinutes=d
        self.__RequiresLab=r
    def OutputLessonDetails(self):
        print(self.__LessonTitle,self.__DurationMinutes)
class Assessment:
    def __init__(self,t,m):
        self.__AssessmentTitle=t
        self.__MaxMarks=m
    def OutputAssessmentDetails(self):
        print(self.__AssessmentTitle,self.__MaxMarks)
def Main():
    MyCourse=Course('Computing',10)
    MyCourse.AddAssessment('Programming',100)
    MyCourse.AddLesson('Problem Solving',60,False)
    MyCourse.AddLesson('Theory',60,False)
    MyCourse.OutputCourseDetails()

Main()
