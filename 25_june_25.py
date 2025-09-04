# 25_june_25 <------------------------> 02_Sep_25 8:00pm(practice)
# Store and print Variables
x = 10      # x stores the number 10
name = "Abhishek"   # name stores a string
is_active = True    # stores a boolean (True/False)
# ✅ Rules for Naming Variables in Python
# 1. Must Start with a letter or Underscores(_)
name = "Abhishek"
_age = 23
# 1num = 1 # SyntaxError: invalid decimal literal
# $name = "abhishek" # SyntaxError: invalid syntax
# 1name = "Abhishek" # SyntaxError: invalid decimal literal

# 2.Cannot start with a number
num1 = 1
# 1num = 1 # SyntaxError: invalid decimal literal
name = "abhishek"
# 1name = "Abhishek" # SyntaxError: invalid decimal literal

# 3. Can only contain letters, numbers, and underscores
user_id = 10
# user-id = 10 # SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
score2 = 99
# score 2 = 99 # SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

#.4 Case-Sensitive 👉 All three are different variables.
age = 20
Age = 25
AGE = 30
# type () : function in python tells us data Type of the given value or Variable.
#Number
print("10   :",type(10))
print("3.14 :",type(3.14))

# String
name = "Abhishek"
print("type of name :",type(name))

# Boolean
flag = True
print("Type of flag :",type(flag))

#List
fruits = ["Apple","Banana"]
print("Type of fruits : ",type(fruits))

# Dictionary
person = {"name": "Abhishek", "age": 23}
print("Type of person : ",type(person))   # <class 'dict'>

value = "100"
print("type of value : ",type(value))

x = 10
if type(x) == int:
    print("x is a integer")

name = "Abhishek"
if type(name) == str:
    print("name is a String")
