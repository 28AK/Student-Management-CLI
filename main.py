class Student:
    def __init__(self,name,roll_num,marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

    def display(self):
        print(self.name,self.roll_num,self.marks)

student1 = Student("Ashi",101,85)
student1.display()
student2 = Student("Rahul",102,80)
student2.display()

# update marks
student1.marks = 95
student1.display()

student2.marks = 88
student2.display()

