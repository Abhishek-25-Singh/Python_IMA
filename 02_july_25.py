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

# Logical Operator

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
