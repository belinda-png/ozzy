def student_details():
    print("WELCOME TO OUR PROGRAM  THANK")
    name = input("enter your name")
    print('your name is ')

    age = int (input ("enter your age"))
    # Dynamic function to add a student detail
def create_student_detail():
    student = {}  # Empty dictionary to store student details
    
    def add_detail(key, value):
        """Dynamic function to add student detail."""
        student[key] = value

    def display_details():
        """Dynamic function to display student details."""
        for key, value in student.items():
            print(key + '' + value)
    
    return add_detail, display_details


# Dynamically create functions for adding and displaying student details
add_student, show_student = create_student_detail()

# Take input from the user for student details
name = input(" please enter your name: ")
age = input("please enter the your age: ")
programm = input("please your programm:")
test_one = int(input("please eneter your mark of the frist test"))
test_two = int(input("please eneter your mark of the second test"))
course_work = int(input("please eneter your your course work"))

# Use the dynamic functions to add the details
# Display the student's details
def student_details():
    student = {"name": "Rina", "age":"24",}
    marks = [60, 80,95]
    report = print(student["name"])
    for mark in marks:
        return report + mark
        print(mark)
   

# Calculate and display the average of the test marks
