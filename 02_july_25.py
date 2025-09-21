# 🔢 Arithmetic Operators in Python
# Example Code 
a = 10 
b = 3

print("Addition        ",end="=> ")
print(a,"+",b , "  = " ,a + b)

print("Subtraction     ",end ="=> ")
print(a,"-",b , "  = " ,a - b)

print(" Multiplication ",end="=> ")
print(a,"*",b , "  = " ,a * b)


print("Division        ",end = "=> ")
print(a,"/",b , "  = " ,a / b)

print("Floor Division  ",end="=> ")
print(a,"//",b , " = " ,a // b)


print("Modulus         ",end = "=> ")
print(a,"%",b , "  = " ,a % b)


print("Exponentiation  ",end ="=> ")
print(a,"**",b , " = " ,a ** b)


num1 = int(input("Please Enter First Integer"))
num2 = int(input("Please Enter Second Integer"))
print("Division :",num1/num2 ,"\tType of",num1,"/",num2," = ",type(num1/num2))

# ⚡ Important Points to Remember
# 1. Division always gives float Even if both numbers are integers:
# 2. Floor division removes decimals.
# 3. Modulo (%) with negative numbers (Python always ensures remainder has same sign as divisor)
# 4. Exponentiation (Power)
# 5. Operators also work with floats.
a = 5.5
b = 2.0

print("Addition:", a + b)       # 7.5
print("Subtraction:", a - b)    # 3.5
print("Multiplication:", a * b) # 11.0
print("Division:", a / b)       # 2.75
print("Floor Division:", a // b) # 2.0 (gives float)
print("Modulo:", a % b)         # 1.5
print("Exponent:", a ** b)      # 30.25
# 6. Order of Operations (PEMDAS/BODMAS rule applies) Python follows Parentheses → Exponent → Multiplication/Division → Addition/Subtraction:

# Comparison Operator

# ⚡ Important Things to Know About Comparison Operators

# 1. Return Type is Boolean (True or False)
print("10 > 5 = ", 10 > 5)
print("Type of (10 > 5 ) = ",type(10>5))

# 2. They can be chained (Python feature 😎)
x = 10

print(" 5 < x      = ", 5 < x )
print(" x < 15     = ", x < 15 )
print(" 5 < x < 10 = ", 5 < x < 15 ) # True (same as 5 < x and x < 15)
print(" 5 < x > 20 = ", 5 < x > 120 )

# 3. Work with different data types
    # 1.Numbers
print(" 5 <= 5   : ", 5 <= 5)
print(" 3.0 == 3 : ", 3.0 == 3)

# 2. String
print ("apple < banana = ", "apple" < "banana")   # True
print("Abc < abc       = ","Abc" < "abc")        # True ('A' has smaller ASCII code than 'a')

# String --> Lexicographically --> Dictionary Order dictionary order, based on ASCII/Unicode):
print ("apple < banana = ", "apple" < "banana")
print ("cat > bat      = ", "cat" > "bat")
print("apple == apple  = ", "apple" == "apple") # Every character matches
print("apple < app     = ", "apple" < "app") # 'apple' is longer than app , So python consider "apple">"app"
print("Apple < apple   = ", "Apple" < "apple") # Uppercase Vs Lowecase 'A' = 67 'a' = 97 Asiic value --> 65 < 97 = True
print("Abc < abc       = ","Abc" < "abc")

# 🔹 4. Unicode / ASCII Values
print("ASCII Values of A = ", ord('A'))  # 65
print("ASCII Values of a = ",ord('a'))  # 97
print("ASCII Values of b = ",ord('b'))  # 98

# 3. Lists and tuples (compared element by element):
print("[1,2,3] == [1,2,3] : ",[1,2,3] == [1,2,3])
print("[1,2] == [1,2,3]   : ",[1,2] == [1,2,3])
print("[1,2] < [1,2,3]    : ",[1,2] < [1,2,3])
print("[1,2,3,4,5] < [1,2,3,3,99] : ",[1,2,3,4,5] < [1,2,3,3,99])

# 4. Difference between = and ==

# 5. Objects comparison → is vs ==
x = [1,2,3]
y = [1,2,3]
print("x == y : ",x == y)   # True (same contents)
print("x is y : ",x is y)   # False (different memory locations)

# 🔹 3. Logical Operators 
a = 10 
b = 5
c= 20
# and (both conditions must be True)
print("a > b and c > a : ",a > b and c > a) # 10 > 5 and 20 > 10 => Trur

# or (at least one condition True)
print("a < b or c > a  : ", a < b or c > a) # 10 < 5 or 20 > 10

# not(flips The reuslt)
print("not(a > b)      : ",not(a > b))

# ⚡ Important Points About Logical Operators
#  1. Boolean Return Type
#  2. Short-Circuit Evaluation (and ,or)
#  3. not is a unary operator (applies to only one condition/value).
#  4. Works with non-boolean values (truthy/falsy)

# 1. Boolean Return Type
print("a < b or c > a  : ", a < b or c > a) # 10 < 5 or 20 > 10
print("not(a > b)      : ",not(a > b))

# 2. Short-Circuit Evaluation (and ,or)
def check():
    print("Checked")
    return True

print("False and check() : ",False and check())  # Output: False  (second not checked)
print("True or check()   : ",True or check())    # Output: True   (second not checked)

def check():
    print("Checked")
    return True
print("check() and True : ", check() and True ) # True and True => True 
print("check() and True : ", check() and False) # True and False => False


# 3. not is a unary operator (applies to only one condition/value).

# 4. Works with non-boolean values (truthy/falsy)
# falsy values
print("Empty list []  : ",bool([]))
print("Empty tuple () : ",bool(()))

print([] or "Hello")   # Hello (empty list is False, so returns second value)
print("Hi" and 100)    # 100 (both True, so returns last value)

# 🔹 Membership Operators in Python
name = "Abhishek"
print("'a' in name : ",'a' in name)
print("'A' in name : ",'A' in name)
print("'Ah' in name : ",'Ah' in name)
print("'Ab' in name : ",'Ab' in name)


fruits = ["apple","grapes","mango"]
print("'banana' in fruits : ",'banana' in fruits)
print("'apple' in fruits : ",'apple' in fruits)

# ⚡ Important Points About Membership Operators
# 1. Case-sensitive (for strings)
# 2. works with substrings.
# 3. Works with lists, tuples, sets and dictionary.
#    a. With dictionaries in checks keys, not values.
#    b. With sets Fast membership check because sets are optimized for lookup.
# 4. Performance Note.
#    a. Checking membership in sets and dicts is faster than in lists/tuples, because sets/dicts use hashing internally.


# 1. Case-sensitive (for strings)
fruit = "Apple"
print(" \"a\" in \"Apple\"   : ", "a" in fruit)
print(" \"A\" in \"Apple\"   : ", "A" in fruit)

print(" \"app\" in \"Apple\" : ", "a" in fruit)
print(" \"App\" in \"Apple\" : ", "A" in fruit)

# 2. works with substrings . in checks whether the substring exists, not just a single character.
print("shi" in "Abhishek")    # True
print("xyz" in "Abhishek")    # False

# 3. Works with lists, tuples, sets and dictionary
# list
number = [1,2,3,4,5]
print("1 in number : ", 1 in number)
print("2 in number : ", 2 in number)
print("3 in number : ", 3 in number)
print("30 in number : ", 30 not in number)
print("4 not in number : ", 4 not in number)
print("5 not in number : ", 5 not in number)

# not in
print("6 in number  : ", 6 in number)
print("50 in number : ", 50 in number)


# tuple
number = (1,2,3,4,5)
print("1 in number : ", 1 in number)
print("2 in number : ", 2 in number)
print("3 in number : ", 3 in number)
print("34 in number : ", 34 in number)

# not in
print("10 not in number  : ", 10 not in number)
print("5 not in number : ", 5 not in number)


# set
number = {1,2,3,4,5}
print("1 in number  : ", 1 in number)
print("2 in number  : ", 2 in number)
print("51 in number : ", 51 in number)

# not in
print("51 not in number : ", 51 not in number)
print("6 not in number  : ", 6 not in number)
print("5 not in number  : ", 5 not in number)
