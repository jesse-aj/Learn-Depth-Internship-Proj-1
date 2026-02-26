### Student Record Manager ####

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))
    
    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
    
    students.append(student)
    print("Student added successfully!\n")




def view_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        for student in students:
            print("Name:", student["name"])
            print("Roll:", student["roll"])
            print("Marks:", student["marks"])
            print("----------------------")
    print()



def search_student():
    roll = input("Enter roll number to search: ")
    found = False
    
    for student in students:
        if student["roll"] == roll:
            print("Student Found:")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            found = True
            break
    

    if not found:
        print("Student not found.")
    print()



def calculate_average():
    if len(students) == 0:
        print("No students available.\n")
    else:
        total = 0
        for student in students:
            total += student["marks"]
        average = total / len(students)
        print("Average Marks:", average)
        print()


def display_topper():
    if len(students) == 0:
        print("No students available.\n")
    else:
        topper = students[0]
        for student in students:
            if student["marks"] > topper["marks"]:
                topper = student
        
        print("Topper:")
        print("Name:", topper["name"])
        print("Marks:", topper["marks"])
        print()


def menu():
    while True:
        print("===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Calculate Average Marks")
        print("5. Display Topper")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            display_topper()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()