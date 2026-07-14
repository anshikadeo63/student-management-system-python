def AddStudent(student_dict):
    Student_ID = input("Enter Student ID: ")
    while True:
        if Student_ID != "":
            break
        else:
            print("No Student ID entered! Try again")
            Student_ID = input("Enter Student ID: ")
    if Student_ID not in student_dict:
        student_dict[Student_ID] = {"Student Name": "","Age": "", "Gender": "", "Email ID": "",
                                    "Phone number": "", "Course": "","Semester": "",
                                        "Marks": {}, "Attendance": ""}
        Student_Name = input("Enter Name: ")
        while True:
            if Student_Name != "":
                student_dict[Student_ID]["Student Name"] = Student_Name
                break
            else:
                print("No Student Name entered! Try again")
                Student_Name = input("Enter Name: ")
        while True:
            try:
                Student_age = int(input("Age: "))
                while True:
                    if (5 <= Student_age <= 100):
                        student_dict[Student_ID]["Age"] = Student_age
                        break
                    else:
                        print("Age should be between 5-100!")
                        Student_age = int(input("Age: "))
            except ValueError:
                print("Please enter integer value!")
            else:
                break
        Student_gender = input("Gender (M/F): ")
        while True:
            if (Student_gender.upper() == "F") or (Student_gender.upper() == "M"):
                student_dict[Student_ID]["Gender"] = Student_gender.upper()
                break
            else:
                print("Please choose between F/M ONLY")
                Student_gender = input("Gender (M/F): ")
        Student_Email = input("Email: ")
        student_dict[Student_ID]["Email ID"] = Student_Email
        Student_Phone_no = input("Phone number: ")
        while True:
            if Student_Phone_no.isdigit():
                student_dict[Student_ID]["Phone number"] = Student_Phone_no
                break
            else:
                print("Please enter digits only!")
                Student_Phone_no = input("Phone number: ")
        Student_course = input("Course: ")
        while True:
            if Student_course != "":
                student_dict[Student_ID]["Course"] = Student_course
                break
            else:
                print("Please enter a value!")
                Student_course = input("Course: ")
        while True:
            try:
                Student_semester = int(input("Semester: "))
                if 1 <= Student_semester <= 8:
                    student_dict[Student_ID]["Semester"] = Student_semester
                    break
                else:
                    print("Semester should be between 1-8.")
            except ValueError:
                print("Please enter integer values only!")
            
        print("Student ID",Student_ID,"added successfully!")
    else:
        print("Student ID already in system!")

def DeleteStudent(student_dict):
    student_ID = input("Enter Student ID: ")
    if student_ID in student_dict:
        student_dict.pop(student_ID)
        print("Student ID",student_ID,"successfully deleted!")
    else:
        print("Student not found!")

def UpdateStudent(student_dict):
    user_choice = input("Enter Student ID: ")
    if user_choice in student_dict:
        user_choice_update = input("(A)Name\n(B)Age\n(C)Gender\n(D)Email ID\n(E)Phone number\n(F)Course\n(G)Semester\n(H)Marks\n(I)Attendance\nWhat would you like to update?: ")
        user_choice_update = user_choice_update.upper()
        if user_choice_update == "A":
            while True:
                user_update_name = input("Enter new student name: ")
                if user_update_name != "":
                    student_dict[user_choice]["Student Name"] = user_update_name
                    print("Name updated!")
                    break
                else:
                    print("Name cannot be empty!")
        elif user_choice_update == "B":
            while True:
                try:
                    user_update_age = int(input("Enter new student age: "))
                    if 5 <= user_update_age <= 100:
                        student_dict[user_choice]["Age"] = user_update_age
                        print("Age updated!")
                        break
                    else:
                        print("Age should be between 5 and 100.")
                except ValueError:
                    print("Please enter an integer value!")
        elif user_choice_update == "C":
            while True:
                user_update_gender = input("Enter new student gender (M/F): ").upper()
                if user_update_gender in ["M", "F"]:
                    student_dict[user_choice]["Gender"] = user_update_gender
                    print("Gender updated!")
                    break
                else:
                    print("Please choose only M or F.")
        elif user_choice_update == "D":
            user_update_email = input("Enter new Email ID: ")
            student_dict[user_choice]["Email ID"] = user_update_email
            print("Email updated!")
        elif user_choice_update == "E":
            while True:
                user_update_number = input("Enter new Phone Number: ")
                if user_update_number.isdigit():
                    student_dict[user_choice]["Phone number"] = user_update_number
                    print("Phone number updated!")
                    break
                else:
                    print("Please enter digits only!")
        elif user_choice_update == "F":
            while True:
                user_update_course = input("Enter new Course: ")
                if user_update_course != "":
                    student_dict[user_choice]["Course"] = user_update_course
                    print("Course updated!")
                    break
                else:
                    print("Course cannot be empty!")
        elif user_choice_update == "G":
            while True:
                try:
                    user_update_sem = int(input("Enter new Semester: "))
                    if 1 <= user_update_sem <= 8:
                        student_dict[user_choice]["Semester"] = user_update_sem
                        print("Semester updated!")
                        break
                    else:
                        print("Semester should be between 1 and 8.")
                except ValueError:
                    print("Please enter an integer value!")
        else:
            print("Invalid option!")
    else:
        print("Student doesn't exist!")

def SearchStudent(student_dict):
        print("Search by : \n(A) Student Name \n(B) Course\n(C) Student ID")
        user_choice = input("Enter choice: ")
        user_choice = user_choice.upper()
        if user_choice == "A":
            student_name = input("Enter Student Name: ")
            count = 0
            for key in student_dict:
                if (student_dict[key]["Student Name"] == student_name):
                    print(key,"-",student_name)
                    count += 1 
            if count == 0:
                print(student_name, "was not found")
        elif user_choice == "B":
            student_course = input("Enter Student Course: ")
            count_2 = 0
            for key in student_dict:
                if (student_dict[key]["Course"] == student_course):
                    print(key, "-", student_dict[key]["Student Name"])
                    count_2 += 1
            if count_2 == 0:
                print("No student has taken the course:", student_course+"!")
        elif user_choice == "C":
            search_ID = input("Student ID to search: ")
            if search_ID in student_dict:
                print("Student ID",search_ID,"found!")
            else:
                print("Student ID",search_ID,"not found!")
        else:
            print("Invalid Input!")
            
def DisplayAllStudents(student_dict):
    print("------------------------------------------------")    
    if not student_dict:
        print("No student in database!")
    else:
        for studentID in student_dict:
            print("Student ID:", studentID)
            for key in student_dict[studentID]:
                if key == "Marks":
                    print("Marks:")
                    if student_dict[studentID]["Marks"]:
                        for subject in student_dict[studentID]["Marks"]:
                            print(f"  {subject}: {student_dict[studentID]['Marks'][subject]}")
                    else:
                        print("  No marks available!")
                else:
                    print(key + ":", student_dict[studentID][key])
            print("------------------------------------------------")

