def students():
    #list to store multiple students' data
    students =[]
    print("WELCOME TO OUR PROGRAM  THANK")
#ask how many students the user wants to enter
    num_students = int(input("please enter the number of students"))

#loop to collect data for each student
    for i in range(num_students):
        print(f"\n please enter student details{i +1}")

        name = input("please enter your name:" )
        gender =input("enter your name")
        age = input("enter your age:")
        program = input("enter the kind program you are working on:")
        date = input("please enter data of study:")
        faculty =input("please your faculty:")

    #input  the test score for student
        try:
            test_one = int(input("please enter your marks for the first test"))
            test_two = int(input("please enter your marks for second test "))
            course_work = int(input("please enter your course work marks"))
        except ValueError:
            print("invalid input!  marks should be numbers. Try again later")
            continue

        student_data ={
            "Name": name,
            "Gender": gender,
            "Age": age,
            "Program": program,
            "faculty": faculty,
            "Test 1": test_one,
            "Test 2": test_two,
            "Course Work": course_work
    }
    # Add student data to the list
    students.append(student_data)
 

# Define function to calculation for the best two marks for two tests 

    result = (test_one + course_work)/2 * (0.4)


