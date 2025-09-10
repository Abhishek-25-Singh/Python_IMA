# # 26_june_25 <------------------> 05_09_25 4:20pm

# Python dose The inferencing Automatically.
a = 10.226  # float
b = 5.229  # Float
c = a + b  # result(c) also be float because both operands (a,b) are float
print("a + b = ",c)
print("Type of c :",type(c))
print("Round od The Value upto 2 Decimal :",round(c,2))


x = 10  # x infers This as Integer
y = 10.5 # y infers This as Float
z = "hello" # z infers This as String
# Here You Never Told Python That "x is Integer","y is Float" and "z is String" Python infers it From The Value.


# This is a single-line comment
a = 20  # This is an inline comment

# 🔹 2. Multi-line comments (using triple quotes)
"""
This is a multi-line comment
spanning across
multiple lines
"""
'''
Another way to write
multi-line comment
'''
# In JupyterLab (or Python in general), this is not a comment.
# 👉 In Python, triple quotes (''' or """) create a multi-line string literal.

# 👉 If you want Jupyter not to show the output, you can: Assign the string to a variable:
x = '''
Another way to write
multi-line comment
'''

# 👉 If you want Jupyter not to show the output, you can: Or add a semicolon at the end:
'''
Another way to write
multi-line comment
''';

def add(a, b):
    """
    This function takes two numbers
    and returns their sum.
    """
    return a + b

print(add.__doc__)

# 🔹There are two types Conversion in Python.
#  Implicity Type COnversion
#  Explicit TYpe COnversion

# ✅ Example 1: int → float
a = 5    # Integer
b = 2.5  # Float
c = a + b # int + float
print(" c : ",c)
print("Type of c :",type(c))
# ➡️ Here, a (int) is automatically converted to float before addition.

# ✅ Example 2: int → complex
a = 10         # int
b = 3.5j       # Complex
c = a + b
print(" c : ",c)
print("Type of c :",type(c))
# ➡️ int is promoted to complex.

# ✅ Example 3: Boolean → int
a = True    # bool (value = 1)
b = 5       # int
c = a + b
print(" c : ",c)
print("Type of c :",type(c))
# ➡️ True becomes 1 and addition is done.


# BUILT - IN FUNCTION
#input() - Take user input 
name = input("Enter Your name : ")
print("Type of name is ",type(name))

print("How Are you",name,"?")

#type() - Check type of data
age = input("Enter your age : ")
print("Type Before conversion : ", type(age))
#Changed String into Integer Explicitly
print("Type of age changed Explicitly : ",type(int(age)))

age = int(input("Enter your age : "))
print("Type of age is :", type(age) )

name = input("What's you'r name : ")
length = len(name)
print("the length od the name :" , length)
print("Type of the length is : " ,type(length))
print(id(length))

Marks = [88,72,66,98,65.9,65.89]
print("highest Marks : ",max(Marks))
print("Lowest MArks : ", min(Marks))
print("Total MArks : ", sum(Marks))
print("Total Marks upto 1 Decimal Point : ",round(sum(Marks,2)))

#abs() function --> Absolute Value
# The abs() function in Python is used to return the absolute value of a number.
# 👉 Absolute value simply means the distance of a number from 0 on the number line, without considering the sign (always non-negative).
num1 = -100
print("Absolute Value of num1 : ",abs(num1))
num2 = 10.4
print("Absolute Value of num1 : ",abs(num2))

# round Function
num2 = 18.6757896
print("Round off upto 1 ", round(num2,0))
print("Round off upto 1 ", round(num2,1))
print("Round off upto 1 ", round(num2,2))
print("Round off upto 1 ", round(num2,3))
print("Round off upto 1 ", round(num2,-3))

num2 = 18.6757896
print("Round off upto 1 ", round(num2,-3))

# Sort the list 
S1 = [11,23,45,67,87,64,56]
print("Sort the Given List in the Ascending order : ",sorted(S1)) # ➡️ Ascending Order
print("Sort the Given List in the Descending order : ",sorted(S1,reverse= 0))
print("Sort the Given List in the Descending order : ",sorted(S1,reverse= True)) # ➡️ Descending Order
print("Sort the Given List in the Descending order : ",sorted(S1,reverse= 1))

#Q1 Create Two Variable and Print their Sum
num1 = 10
num2 = 20
Sum = num1 + num2
print("Sum of num1 And num2 : ", Sum)

#INput From the User for the Sum
num1 = int(input("Enter the num1 : "))
num2 = int(input("Enter the num2 : "))
Sum = num1 + num2 
print("Addition of num1 and num2 : ",Sum)
print("Type of Sum is : ", type(Sum))

# Q2 Store name in a variable and print it's length
name = "Abhishek"
print("The length of the name : ",len(name))

#Q3 TAke user inputfor phone number and display its data type
Phone_number = int(input("Enter Your 10 Digit Phone Number : "))
print("Data Type of Phone NUmber is : ",type(Phone_number))

# Q4 Convert String number to integer and add 5
str1 = "100"
Convert = int(str1)
Addition = Convert + 5
print("Addition of str1 and 5 :",Addition)

# DATA TYPE IN PYTHON


