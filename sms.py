students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll no: ")
    age = input("Enter age: ")
    dept = input("Enter department: ")
    
    students.append({
        "name": name,
        "roll": roll,
        "age": age,
        "dept": dept
    })
    print("Student added!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Age: {s['age']}, Dept: {s['dept']}")
    print()

def search_student():
    roll = input("Enter roll no to search: ")
    for s in students:
        if s["roll"] == roll:
            print("Student found:", s, "\n")
            return
    print("Student not found!\n")

def delete_student():
    roll = input("Enter roll no to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted!\n")
            return
    print("Student not found!\n")

while True:
    print("""
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit
""")
    
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid choice!\n")

