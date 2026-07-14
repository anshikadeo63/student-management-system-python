def ReportCard(student_dict):
    user_id = input("Enter User ID: ")
    print()
    count = 0
    if user_id in student_dict:
        print("==================================\n          REPORT CARD          \n==================================")
        print(f"Student ID: {user_id}\nStudent Name: {student_dict[user_id]['Student Name']}")
        print(f"Student Course: {student_dict[user_id]['Course']}\nSemester: {student_dict[user_id]['Semester']}\n")
        print("Marks\n-------------------")
        for subject in student_dict[user_id]["Marks"]:
            print(f"{subject}: {student_dict[user_id]['Marks'][subject]}")
            count += 1
        if count == 0:
            print("No marks available.")
        print("-------------------")
        if student_dict[user_id]["Marks"] != {}:
            total_marks_obtained = 0
            subject_count = 0
            for subject in student_dict[user_id]["Marks"]:
                total_marks_obtained += student_dict[user_id]["Marks"][subject]
                subject_count += 1
            total_possible_marks = 100 * subject_count
            percentage = ((total_marks_obtained / total_possible_marks) * 100)

            if 90 <= percentage <= 100:
                grade = "A"
            elif 80 <= percentage < 90:
                grade = "B"
            elif 70 <= percentage < 80:
                grade = "C"
            elif 60 <= percentage < 70:
                grade = "D"
            else:
                grade = "F"

            print(f"Total: {total_marks_obtained}")
            print(f"Percentage: {percentage:.2f}%")
            print(f"Grade: {grade} ({percentage:.2f}%)")

            if student_dict[user_id]["Attendance"] != "":
                print(f"Attendance: {student_dict[user_id]['Attendance']}%\n")
            else:
                print("Attendance: Not Available\n")

            print("==================================")
        else:
            print("Report card cannot be generated because marks are not available.")
            print("==================================")
    else:
        print("Student ID does not exist!")
