'''
Question:Create a class named 'Student' with the variable 'name' and 'roll_no'. And write a Display method to display the name and roll_no. Assign the value of roll_no as '2' and that of name as "John" by creating an object of the class Student.
answer:
'''
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

# Create a student object
student1 = Student("John", 2)

# Display student information
student1.display()
