class Student:
    def __init__(self,name,roll_num,marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

    def display(self):
        print(self.name,self.roll_num,self.marks)

    def update_marks(self,new_marks):
        self.marks = new_marks

    def update_name(self,new_name):
        self.name = new_name

student1 = Student("Ashi",101,85)
student1.display()
student2 = Student("Rahul",102,80)
student2.display()

student1.update_marks(95)
student2.update_marks(88)
student1.display()
student2.display()

student1.update_name("Akanksha")
student2.update_name("Puneet")
student1.display()
student2.display()

students = [student1,student2]
for student in students:
    student.display()