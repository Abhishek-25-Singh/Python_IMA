# 🧠 Syntax of range() : **range(start, stop, step/skip)**
number = list(range(11)) # it will Take default From 0
print(number)
print(list(range(5)))
for i in range(5):
    print(i)


range(2,6)

for i in range(2,6):
    print(i)


range(0, 10, 2)

print(list(range(0,10,2)))

for i in range(0,10,2):
    print(i)

numbers = range(5)
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

numbers = range(5)
it = iter(numbers)
print("Iterator : ",(hasattr (numbers,"__next__")))
print("Iterator : ",(hasattr (it, "__next__")))

number = list(range(11))
print("numbers : " , number)

# Syntax of range : (start , stop , step/skip)
number = list(range(2 , 21, 2))
print("numbers : " , number)

for i in number:
    print(i + 1)

name = ["Abhishek", "piyush","roni","shera", "chikki"]
for i in name:
    print(i)

for i in name:
    print("hello ", i, " !")

num_list = [10,55,88,109,108,44,34,102]
count_even = 0
count_odd = 0

for i in num_list:
    if (i % 2 == 0):
        count_even+=1
    else:
        count_odd +=1
print("count of Even in num list : " , count_even)
print("count of odd in num list  : " , count_odd)


# Q Print the table of 5 from 1 to 10
number = list(range(1,11))
for i in number:
    print("5 ","* ", i , " = ",5 * i)

# Post-increment
num = int(input("Enter The Integer : "))
count = 1
while count<=10:
    print(num," * ",count," = ", num*count)
    count+=1

# pre-increment
num = int(input("Enter The Integer : "))
count = 0
while count<10:
    count+=1
    print(num," * ",count," = ", num*count)

# There are two types of loop Commands
# 1.break
# 2.Continue

for i in range(1,10):
    if i == 7:
        continue
    print(i)

for i in range(1,5):
    if i == 3:
        break
    print(i)

for i in range(1, 4):
    if i == 2:
        pass   # does nothing, just a placeholder
    print(i)
print("Iterator : " , hasattr(i,"__next__"))
print("Iterator : " , hasattr(range,"__next__"))

Vowel = ['A','a','e','E','i',"I",'o','O','u','U']
name = input("ENter any String : ")
count=0
for i in name:
    if i in Vowel:
        count+=1
        print(i)
print(count)


text = input("ENter a String : ")
vowels="AEIOUaeiou"
count=0
for char in text:
    if char in vowels:
        count+=1
print("Number of Vowels in String : ",count)
