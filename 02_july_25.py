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
