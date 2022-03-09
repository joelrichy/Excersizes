class Student:
    def __init__(self, name, age, phone_number, form_class, subjects, is_male):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = is_male
        self.enroll_details = True
        student_list.append(self)

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Phone number: ", self.phone_number)
        print("Form class: ", self.form_class)
        print("Subjects: ", self.subjects)
        print("Gender: ", self.is_male)
        print(self.enroll_details)
        print("####################")
        if self.is_male:
            print(self.name, "is male")
        else:
            print(self.name, "is female")
        print("Enrolled: ", self.enroll_details)
        print()


# invokes display info, prints student details
def print_student_details():
    for student in student_list:
        student.display_info()


def select_student_age():
    age = int(input("Age to print above: "))
    count = 0
    for student in student_list:
        if student.age > age:
            student.display_info()
    print(f"There are {count} students above {age}")

def generate_students():
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[4] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)


def count_students():
    count = 0
    subject = input("What class are you looking for: ")
    for student in student_list:
        if subject in student.classes:
            count += 1
    if count > 0:
        print(f"\n There are {count} students in {subject}")
    else:
        print(f"\n There are no students in {subject}")


def find_student(text):
    student_input = input(text).title()
    found = False
    for student in student_list:
        if student_input == student.name:
            found = True
            student.display_info()
    if not found:
        print(f"Sorry we do not have {student_input} in our database.")


# main routine


student_list = []

generate_students()

# menu loop

choice = ""
while choice != "Q" and choice != 'q':
    print("")
    print("*****MENU*****")
    print("")
    print("1. Count students taking a particular subject")
    print("2. Print a full list of students")
    print("3. Print a list of students above a particular age")
    print("4. Get details of a particular student")
    menu_choice = input("What would you like to do"
                   " - enter a number of press Q to exit: ")
    print("")
    if menu_choice == "1":
        count_students()
    elif menu_choice == "2":
        print_student_details()
    elif menu_choice == "3":
        select_student_age()
    elif menu_choice == "4":
        student_to_find = find_student("What student are you looking for: ")
    elif choice == "Q" or choice == "q":
        print("Goodbye")
    else:
        print("***That is not a valid option***")
