name = input("Enter student name: ")
math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))


if not (0 <= math <= 100) or not (0 <= english <= 100) or not (0 <= python <= 100):
    print("Invalid marks. Marks must be between 0 and 100.")
else:
    
    average = (math + english + python) / 3

    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    
    print(f"Student Name: {name}")
    print(f"Average Marks: {average:.2f}")
    print(f"Final Grade: {grade}")
    