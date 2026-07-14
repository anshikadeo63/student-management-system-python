import os
import json
from functions.student import *
from functions.attendance import *
from functions.marks import *
from functions.report import *
from functions.analysis import *

def LoadData():
    try:
        with open("student_info.json", "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        return {}

def SaveData(student_dict):
    with open("student_info.json", "w") as f:
        json.dump(student_dict, f, indent=4)

student_dict = LoadData()

def LoopFormat():
    os.system("cls")
    print()
    print("========== STUDENT MANAGEMENT SYSTEM ==========")
    print("---------------------------------------------------")
    user_choice = input("(A) Student Management\n(B) Marks Management\n(C) Attendance Management\n(D) Performance Analysis\n(E) Reports\n(F) Exit\n---------------------------------------------------\nEnter choice: ")
    print()   
    return user_choice.upper()

user_choice = LoopFormat()

while user_choice != "F":
    if user_choice == "A":
        while True:
            print("\n---------- STUDENT MANAGEMENT ----------")
            user_choice_2 = input("(A) Add Student\n(B) Delete Student\n(C) Update Student\n(D) Search Student\n(E) Display All Students\n(F) Back\n----------------------------------------\nEnter choice: ").upper()
            print()

            if user_choice_2 == "A":
                AddStudent(student_dict)
                SaveData(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_2 == "B":
                DeleteStudent(student_dict)
                SaveData(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_2 == "C":
                UpdateStudent(student_dict)
                SaveData(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_2 == "D":
                SearchStudent(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_2 == "E":
                DisplayAllStudents(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_2 == "F":
                break

            else:
                print("Please choose from the above options only!")
                input("\nPress Enter to continue...")

    elif user_choice == "B":
        while True:
            print("\n---------- MARKS MANAGEMENT ----------")
            user_choice_3 = input("(A) Add Marks\n(B) Update Marks\n(C) Calculate Average\n(D) Calculate Percentage\n(E) Calculate Grade\n(F) Back\n--------------------------------------\nEnter choice: ").upper()
            print()

            if user_choice_3 == "A":
                AddMarks(student_dict)
                SaveData(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_3 == "B":
                UpdateMarks(student_dict)
                SaveData(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_3 == "C":
                CalculateAverage(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_3 == "D":
                CalculatePercentage(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_3 == "E":
                CalculateGrade(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_3 == "F":
                break

            else:
                print("Please choose from the above options only!")
                input("\nPress Enter to continue...")
    
    elif user_choice == "C":
        while True:
            print("\n---------- ATTENDANCE MANAGEMENT ----------")
            user_choice_4 = input("(A) Add Attendance\n(B) Update Attendance\n(C) Attendance Warning\n(D) Back\n-------------------------------------------\nEnter choice: ").upper()
            print()

            if user_choice_4 == "A":
                AddAttendance(student_dict)
                input("\nPress Enter to continue...")
                SaveData(student_dict)

            elif user_choice_4 == "B":
                UpdateAttendance(student_dict)
                input("\nPress Enter to continue...")
                SaveData(student_dict)

            elif user_choice_4 == "C":
                AttendanceWarning(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_4 == "D":
                break

            else:
                print("Please choose from the above options only!")
                input("\nPress Enter to continue...")

    elif user_choice == "D":
        while True:
            print("\n---------- PERFORMANCE ANALYSIS ----------")
            user_choice_5 = input("(A) Rank Students\n(B) Find Topper\n(C) Find Lowest Scorer\n(D) Average Class Percentage\n(E) Scholarship Eligibility\n(F) Back\n------------------------------------------\nEnter choice: ").upper()
            print()

            if user_choice_5 == "A":
                RankStudents(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_5 == "B":
                FindTopper(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_5 == "C":
                FindLowestScorer(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_5 == "D":
                AverageClassPercent(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_5 == "E":
                ScholarshipEligibility(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_5 == "F":
                break

            else:
                print("Please choose from the above options only!")
                input("\nPress Enter to continue...")

    elif user_choice == "E":
        while True:
            print("\n---------- REPORTS ----------")
            user_choice_6 = input("(A) Report Card\n(B) Back\n-----------------------------\nEnter choice: ").upper()
            print()

            if user_choice_6 == "A":
                ReportCard(student_dict)
                input("\nPress Enter to continue...")

            elif user_choice_6 == "B":
                break

            else:
                print("Please choose from the above options only!")
                input("\nPress Enter to continue...")

    else:
        print("Invalid option!")
        input("\nPress Enter to continue...")

    user_choice = LoopFormat()

print("Thank you for using Student Management System!")
