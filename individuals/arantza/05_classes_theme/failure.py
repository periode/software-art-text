class Failure:
    def __init__(self, subject, exam, student):
        self.subject = subject
        self.exam = exam
        self.student = student

    def study(self):
        might_pass = True
        print self.student + " did study for the " + self.subject + ' ' + self.exam + "."
        # the student
        return might_pass

    def no_study(self):
        might_fail = True
        print self.student + ' did not study for the ' + self.subject + ' ' + self.exam + "."
        # the student
        return might_fail

    def take_exam(self, did_study):
        if (self.subject.lower() == 'algorithms' or self.subject.lower() == 'algorithm'):
            if (did_study == True):
                return 1
            else:
                return 0
        else:
            return 2

    def get_back_results(self, grade):
        # any exam
        if (grade == 2):
            return self.student + ' passed!'
        # algorithms exam
        if (grade == 1):
            return self.student + ' still probably failed.'
        if (grade == 0):
            return self.student + ' still probably failed.'

student = Failure("Algorithms", "Midterm", "Arantza")

probable_results = student.study()
actual_results = student.take_exam(probable_results)
final_grade = student.get_back_results(actual_results)
print final_grade
