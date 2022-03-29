# Student Class - Defines the student object
class Student:

    grade = 0
    passing_score = 75
    award_credit = False

    
    #initializer sometimes called a constructor
    def __init__(self, first_name, last_name, status):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name.lower() + self.last_name.lower() + '@gmail.com'
        self.status = status

    def print_Student_info(self):
        print('STUDENT:', self.first_name, self.last_name, 
        '\nEMAIL:', self.email, 
        '\nSTATUS:', self.status,
        '\nPassing', self.award_credit)

    def set_grade(self, new_grade):
        self.grade = new_grade
        if (self.grade >= self.passing_score):
            self.award_credit = True
        if(self.grade < self.passing_score):
            self.award_credit = False


tess = Student('Tess','Heiner','Full time') #tess is an instance of the Student class
sophie = Student('Sophie','Heiner','Full time') #sophie is an instance of the Student class

tess.set_grade(80)
sophie.set_grade(35)


print('\n')
tess.print_Student_info()

print('\n')
sophie.print_Student_info()



