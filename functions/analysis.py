def FindTopper(student_dict):
    highest_percent = 0
    total_marks = 0
    subject_count = 0
    student_id = ""
    for key in student_dict:
        for subject in student_dict[key]["Marks"]:
            total_marks += student_dict[key]["Marks"][subject]
            subject_count += 1
        if subject_count != 0:
            total_possible_marks = 100 * subject_count
            percentage = ((total_marks/ total_possible_marks)*100)
            if percentage > highest_percent:
                highest_percent = percentage
                student_id = key
        total_marks = 0
        subject_count = 0
    if student_id == "":
        print("No student with marks found!")
    else:
        print(f"🏆 Topper\nStudent ID: {student_id}\nName: {student_dict[student_id]['Student Name']}\nPercentage: {highest_percent:.2f}%")

def FindLowestScorer(student_dict):
    lowest_percent = 101
    total_marks = 0
    subject_count = 0
    student_id = ""
    for key in student_dict:
        for subject in student_dict[key]["Marks"]:
            total_marks += student_dict[key]["Marks"][subject]
            subject_count += 1
        if subject_count != 0:
            total_possible_marks = 100 * subject_count
            percentage = ((total_marks/ total_possible_marks)*100)
            if lowest_percent > percentage:
                lowest_percent = percentage
                student_id = key
        total_marks = 0
        subject_count = 0
    if student_id == "":
        print("No student with marks found!")
    else:
        print(f"Lowest Scorer\nStudent ID: {student_id}\nName: {student_dict[student_id]['Student Name']}\nPercentage: {lowest_percent:.2f}%")

def RankStudents(student_dict):
    student_id_list = []
    student_name_list = []
    student_percent_list = []
    for student_id in student_dict:
        if student_dict[student_id]["Marks"] != {}:
            total_marks_obtained = 0
            subject_count = 0
            for subject in student_dict[student_id]["Marks"]:
                total_marks_obtained += student_dict[student_id]["Marks"][subject]
                subject_count += 1
            total_possible_marks = 100 * subject_count
            percentage = ((total_marks_obtained/ total_possible_marks)*100)
            student_id_list.append(student_id)
            student_name_list.append(student_dict[student_id]["Student Name"])
            student_percent_list.append(percentage)
        else:
            student_id_list.append(student_id)
            student_name_list.append(student_dict[student_id]["Student Name"])
            student_percent_list.append(0)               
    highest_number = 0
    count = 1
    index = 0
    while len(student_percent_list) != 0:
        highest_number = 0
        for i in range(len(student_percent_list)):
            if student_percent_list[i] >= highest_number:
                highest_number = student_percent_list[i]
                index = i
    
        print(f"Rank {count}\nID: {student_id_list[index]}\nName: {student_name_list[index]}\nPercentage: {student_percent_list[index]}\n")
        student_percent_list.pop(index)
        student_id_list.pop(index)
        student_name_list.pop(index)
        count += 1

def ScholarshipEligibility(student_dict):
    try:
        user_attendance = int(input("Enter attendance eligibility limit: "))
        user_percent = int(input("Enter percentage eligibility limit: "))
        count = 0
        if (0 <= user_attendance <= 100) and (0 <= user_percent <= 100):
            for student_id in student_dict:
                if (student_dict[student_id]["Marks"] != {}) and (student_dict[student_id]["Attendance"] != ""):
                    total_marks_obtained = 0
                    subject_count = 0
                    for subject in student_dict[student_id]["Marks"]:
                        total_marks_obtained += student_dict[student_id]["Marks"][subject]
                        subject_count += 1
                    total_possible_marks = 100 * subject_count
                    percentage = ((total_marks_obtained/ total_possible_marks)*100)
                    if (percentage >= user_percent) and (student_dict[student_id]["Attendance"] >= user_attendance):
                        print(f"ID: {student_id}\nName: {student_dict[student_id]['Student Name']}\nPercentage: {percentage}%\nAttendance: {student_dict[student_id]['Attendance']}%\n")
                        count += 1  
        else:
            print("Attendance and Percentage should be between 0-100!")
        if (count == 0):
            print("No student eligible for scholarship!")
    except ValueError:
        print("Attendance and Percentage should be integer values!")
    except Exception:
        print("Something went wrong!")

def AverageClassPercent(student_dict):
    percent_list = []
    for student_id in student_dict:
        total_marks = 0
        subject_count = 0
        max_marks = 0
        if student_dict[student_id]["Marks"] != {}:
            for subject in student_dict[student_id]["Marks"]:
                    total_marks += student_dict[student_id]["Marks"][subject]
                    subject_count += 1
            max_marks = 100*subject_count
            percentage = (total_marks/max_marks)*100
            percent_list.append(percentage)
    if len(percent_list) != 0:
        total_percent = 0
        count = 0
        for percent in percent_list:
            total_percent += percent
            count += 1
        average_percent = total_percent/count
        print("The average percentage of all students:", average_percent)  
    else:
        print("No students with marks found!")   
 
 