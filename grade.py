marks = []

print(" Welcome to the Student Grade Calculator")
print("Please enter marks for 5 subjects (between 0 and 100).")

for i in range(1, 6):
    while True:  
        try:
            mark = float(input(f"Enter marks for subject {i}: "))
            if 0 <= mark <= 100:   
                marks.append(mark)
                break
            else:
                print("❌ Marks should be between 0 and 100. Try again.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"
print("\n ### Results ### ")
print(f"Total Marks   : {total}")
print(f"Average Marks : {average:.2f}")
print(f"Grade         : {grade}")
print("Thank you for using the Grade Calculator! ☺️ ")
