def AddAttendance(student_dict):
    user_id = input("Enter Student ID: ")
    if user_id in student_dict:
        while True:
            try:
                user_attendance = int(input("Enter Attendance: "))
                if 0 <= user_attendance <= 100:
                    student_dict[user_id]["Attendance"] = user_attendance
                    print("Successfully added!")
                    break
                else:
                    print("Attendance should be between 0 - 100")
            except ValueError:
                print("Please enter integer values only!")
    else:
        print("Student ID doesn't exist!")

def UpdateAttendance(student_dict):
    user_id = input("Enter Student ID: ")
    if user_id in student_dict:
        if student_dict[user_id]['Attendance'] != '':
            print(f"Current Attendance: {student_dict[user_id]['Attendance']}%")
        else:
            print("No attendance added for Student")
        try:
            new_attendance = int(input("Enter New Attendance: "))
            if (0 <= new_attendance <= 100):
                student_dict[user_id]["Attendance"] = new_attendance
                print("Attendance successully updated!")
            else:
                print("Attendance should be between 0- 100!")
        except ValueError:
            print("Please enter a valid number!")
        except Exception:
            print("Error!")
    else:
        print("Student ID doesn't exist!")

def AttendanceWarning(student_dict):
    count = 0
    try:
        min_attendance = int(input("Enter the minimum attendance requirement: "))
        if (0 <= min_attendance <= 100):
            for student in student_dict:
                if student_dict[student]["Attendance"] != "":
                    if student_dict[student]["Attendance"] < min_attendance:
                        count += 1
                        print(f"Student ID: {student}\nName: {student_dict[student]['Student Name']}\nAttendance: {student_dict[student]['Attendance']}%\n")
        else:
            print("Minimum attendance should be between 0 - 100!")
            
        if count == 0:
            print("All students are above the minimum attendance limit.")
    except ValueError:
        print("Enter an integer value!")
    except Exception:
        print("Error!")
