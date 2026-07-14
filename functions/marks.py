def AddMarks(student_dict):
    user_choice = input("Enter Student ID: ")
    user_yes_no = "Y"
    if user_choice in student_dict:
        while user_yes_no != "N":
            while True:
                user_subject = input("Enter subject: ")
                if user_subject != "":
                    break
                else:
                    print("Subject name cannot be empty!")
            while True:
                try:
                    user_marks = int(input("Enter marks: "))
                    if 0 <= user_marks <= 100:
                        break
                    else:
                        print("Marks should be between 0-100!")
                except ValueError:
                    print("Please enter integer values only!")
            student_dict[user_choice]["Marks"][user_subject] = user_marks
            while True:
                user_yes_no = input("Do you want to add another subject?(Y for yes and N for no): ")
                user_yes_no = user_yes_no.upper()
                if user_yes_no == "Y" or user_yes_no == "N":
                    break
                else:
                    print("Please enter Y or N only!")
        print("Marks added successfully!")
    else:
        print("Student ID not found!")

def UpdateMarks(student_dict):
    user_id = input("Enter Student ID: ")
    if user_id in student_dict:
        if student_dict[user_id]["Marks"] != {}:
            print("Which subject do you want to update?\nAvailable subjects:")
            count = 1
            for key in student_dict[user_id]["Marks"]:
                print(f"{count}) {key}")
                count += 1
            user_subject_choice = input("Enter subject: ")
            if user_subject_choice in student_dict[user_id]["Marks"]:
                while True:
                    try:
                        user_marks = int(input("Enter new marks: "))
                        if 0 <= user_marks <= 100:
                            student_dict[user_id]["Marks"][user_subject_choice] = user_marks
                            print("Marks successfully updated!")
                            break
                        else:
                            print("Marks should be between 0-100!")
                    except ValueError:
                        print("Please enter integer values only!")
            else:
                print("Subject:", user_subject_choice, "doesn't exist.")
        else:
            print("Student ID:", user_id, "doesn't contain any subjects.")    
    else:
        print("Student ID:", user_id,"doesn't exist!")

def CalculateAverage(student_dict):
    student_id = input("Enter Student ID: ")
    if student_id in student_dict:
        if student_dict[student_id]["Marks"] != {}:
            total_marks = 0
            subject_count = 0
            for subject in student_dict[student_id]["Marks"]:
                total_marks += student_dict[student_id]["Marks"][subject]
                subject_count += 1
            student_average = total_marks/subject_count
            print(f"Average marks: {student_average:.2f}")
        else:
            print("No subject exists for Student ID", student_id)
    else:
        print("Student ID", student_id, "doesn't exist!")

def CalculatePercentage(student_dict):
    student_id = input("Enter Student ID: ")
    if student_id in student_dict:
        if student_dict[student_id]["Marks"] != {}:
            total_marks_obtained = 0
            subject_count = 0
            for subject in student_dict[student_id]["Marks"]:
                total_marks_obtained += student_dict[student_id]["Marks"][subject]
                subject_count += 1
            total_possible_marks = 100 * subject_count
            percentage = ((total_marks_obtained/ total_possible_marks)*100)
            print(f"Percentage: {percentage:.2f}%")
        else:
            print("No subject exists for Student ID", student_id)
    else:
        print("Student ID", student_id, "doesn't exist!")

def CalculateGrade(student_dict):
    student_id = input("Enter Student ID: ")
    if student_id in student_dict:
        if student_dict[student_id]["Marks"] != {}:
            total_marks_obtained = 0
            subject_count = 0
            for subject in student_dict[student_id]["Marks"]:
                total_marks_obtained += student_dict[student_id]["Marks"][subject]
                subject_count += 1
            total_possible_marks = 100 * subject_count
            percentage = ((total_marks_obtained/ total_possible_marks)*100)
            if (90 <= percentage <= 100):
                grade = "A"
            elif (80 <= percentage < 90):
                grade = "B"
            elif (70 <= percentage < 80):
                grade = "C"
            elif (60 <= percentage < 70):
                grade = "D"
            else:
                grade = "F"
            print(f"Student grade: {grade} ({percentage}%)")
        else:
            print("No subject exists for Student ID", student_id)
    else:
        print("Student ID", student_id, "doesn't exist!")
