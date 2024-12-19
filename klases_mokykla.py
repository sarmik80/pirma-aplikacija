

class Student:
    def __init__(self, first_name, last_name, grades):

        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def grade_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def max_grade(self):
        if not self.grades:
            return None
        return max(self.grades)
    
    def min_grade(self):
        if not self.grades:
            return None
        return min(self.grades)
    
student_1 = Student("John", "Malkovich", [6, 9 , 7, 6])
student_2 = Student("Amanda", "Lear", [5, 10 , 8, 7])
student_3 = Student("Brad", "Pitt", [5, 8 , 4, 8])
    
print(f"Student's {student_1.first_name} {student_1.last_name} average of grades is: {student_1.grade_average()}")
print(f"Max grade is : {student_1.max_grade()}")
print(f"Min grade is: {student_1.min_grade()}")


# print(f"Student's {student_3.first_name} {student_3.last_name} average of grades is: {student_3.grade_average()}")
# print(f"Max grade is : {student_3.max_grade()}")
# print(f"Min grade is: {student_3.min_grade()}")


# Sukurkite Abiturientas klasę, kuri paveldi Mokinys klasę ir prideda papildomą funkcionalumą, pvz., gebėjimą pridėti egzamino rezultatus
#  ir skaičiuoti bendrą vidurkį, įskaitant ir egzamino rezultatus. 

class Graduate(Student):
    def __init__(self, first_name, last_name, grades, exam_grades):
        super().__init__(first_name, last_name, grades)

        self.exam_grades = exam_grades

    def total_average(self):
       all_grades = self.grades + self.exam_grades
       return sum(all_grades)/ len(all_grades)
    
graduate_1 = Graduate("Amanda", "Lear", [5, 10 , 8, 7],[8, 7, 6])

print(f"Student's {graduate_1.first_name} {graduate_1.last_name} average of grades is: {graduate_1.total_average()}")


# Sukurkite Mokykla klasę, kuri turės sąrašą Mokinys objektų. Įtraukite metodus, 
# kurie leistų pridėti naują mokinį, pašalinti mokinį, bei skaičiuoti visos mokyklos mokinių pažymių vidurkius.

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, first_name, last_name):
        for student in self.students:
            if student.first_name == first_name and student.last_name == last_name:
                self.students.remove(student)
                return
            print(f"Student {first_name} {last_name} was not found")

    def all_grades(self):
        all_grades = []
        for student in self.students:
            all_grades.extend(student.grades)
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0
        
school = School()
school.add_student(Student("Ben", "Affleck", [5, 6, 4, 8, 9]))
school.add_student(Graduate("Lisa", "Kudrow", [6, 7, 9, 10, 5], [8, 9, 7]))

print(f"Shcool average grade is {school.all_grades()}")

school.remove_student("John", "Malkovich")
print(f"Shcool average grade after stedent remove is: {school.all_grades()}")


# Atnaujinkite Mokinys klasę. Sukurkite metodus, kurie leistų saugiai pridėti ir gauti pažymius,
# užtikrinant, kad nebūtų galima pridėti netinkamų pažymių (pvz., neigiamų ar didesnių nei 10).
