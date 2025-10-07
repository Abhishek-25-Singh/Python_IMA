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
