# Taking input from the student of their academic details
Name=input("Enter your Name: ")
rno=input("Enter your Roll Number: ")
classs=input("Enter your Class: ")
marks=int(input("Enter your Total Marks: "))

# Conditions to check the grade of the student based on their marks
if (marks >=900):
    grade="A+"
elif (marks >=800):
    grade="A"
elif (marks >=700):
    grade="B+"
elif (marks >=600):
    grade="B"
elif (marks >=500):
    grade="C"
else :
    grade="D"
# Displaying academic details of the student
print("\nHello", Name + "!")
print("Your marks are", marks)
print("Your grade is:", grade, ". Congratulations! for the achievement. ")

# End of the program

