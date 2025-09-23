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
