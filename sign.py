import datetime  # Importing the datetime module

def flush_input():
    pass  # Fix skipping issues

# Function to capture student details
def get_student_details():
     # Fix skipping issues
    flush_input()  

    name = input("Enter student name: ").strip().title()
    age = get_valid_integer("Enter age: ", min_value=18, max_value=100)
    gender = get_valid_gender("Enter gender (Male/Female): ")
    program = input("Enter program: ").strip().title()
    year = get_valid_integer("Enter year of study: ", min_value=1)
    faculty = input("Enter faculty: ").strip().title()
    dob = get_valid_date("Enter date of birth (YYYY-MM-DD): ")

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "program": program,
        "year": year,
        "faculty": faculty,
        "dob": dob
    }

# Example function to validate integer input
def get_valid_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Example function to validate gender input
def get_valid_gender(prompt):
    while True:
        gender = input(prompt).strip().lower()
        if gender in ["male", "female"]:
            return gender.title()
        else:
            print("Invalid input! Please enter 'Male' or 'Female'.")

# Example function to validate date input
def get_valid_date(prompt):
    while True:
        try:
            date_str = input(prompt)
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return date_obj
        except ValueError:
            print("Invalid date format! Please enter in YYYY-MM-DD format.")

# Run the function
student_info = get_student_details()
print("\nStudent Details:")
for key, value in student_info.items():
    print(f"{key}: {value}")

