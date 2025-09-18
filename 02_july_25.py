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
