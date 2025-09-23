# 🔹 Conditional Statements in Python

# 1) If Statement - 
# If will only Execute if the given condition is true

age = 20
if age >= 18:
    print("You are eligible to vote! " )


age = int(input("Enter your age in Numbers : "))
if age >= 18:
          print(age,"Is ELigible to vote ")


# 2) If-Else Statement
#    Executes one block if condition is True, otherwise another block.

age = int(input("Enter your age in Numbers : "))
if age >= 18:
          print(age,"Is ELigible to vote ")
else:
    print(age," Not eligible to Vote")


marks = 45
if marks >= 40:
    print("You passed.")
else:
    print("You failed.")


# 3) If-Elif-Else Statement (Elif Ladder)
#    Useful when there are multiple conditions

age = int(input("Enter Your age in Integer : "))
if age == 0:
    print("Not born Yet ")
elif age > 0 and age <=19:
    print(age," Teenager")
elif age >= 20 and age <= 60:
    print("adult")
else:
    print(age," Senior Citizen") 


score = 85
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Grade D")


# 4) Nested If (or Nested Elif)
# 	• An if (or elif) inside another if.


num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")


# if statement
marks = 41
if marks > 40:
    print("you have clear The Test ")
else:
    print("You havn't Clear The Test " ) 



#Q1. If the Score is int the range of 30 to 80 then give in the range else "out of range"
Score = float(input("Enter The Score :"))
if Score >= 30 and Score<= 80:
    print("In The Given range ")
else:
    print("Out of range")
