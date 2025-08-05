# List are Collection of Elements Which Holds any sort of Data into Square [] Bracket.
# Creating List
#Empty List
empty_list = []
print("Empty List :",empty_list)
print("Type of empty_list :",type(empty_list))

#Integer
int_list = [1,2,3,4,5]
print("int_list :",int_list)
print("Type of int_list :",type(int_list))

#String
Str_list = ["Apple","Banana","Cherry"]
print("Str_list :",Str_list)
print("Type of Str_list :",type(Str_list))

# 🔹 Accessing Elements in a List
fruits = ["Apple","Banana","Grapes","Orange"]
Colors = ["Red","Yellow","Purple","Green"]
print("fruits[0] :",fruits[0])
print("fruits[1] :",fruits[1])
print("fruits[2] :",fruits[2])
print("fruits[3] :",fruits[3])
print("Colors[-1] :",Colors[-1])
print("Colors[2] :",Colors[-2])
print("Colors[3] :",Colors[-3])
print("Colors[3] :",Colors[-4])

#🔹 Key Properties of Lists
#Mixed Data Type
Mixed_list = [1,"hello",3.14,True]
print("Mixed Type : ",Mixed_list)
print("Type of Mixed_list :",type(Mixed_list)

#2.List Can Store Repeated or Duplicate value.
Duplicates = [1,1,"Abhishek","Abhishek",True,True]
print("Duplicates :",Duplicates)
print("type of Duplicates :",type(Duplicates))

#3.List preserve the order of the inputs.
fruits = ["Apple","Banana","Mango","Cherry"]
print("Fruits :",fruits)
print("Type of fruits :",type(fruits))

fruits.append("Grapes")
print("Fruits :",fruits) #✔️ New element add hua, last mein — order ab bhi preserve hai.

#4. List are mutable in nature.
#🔹 Modifying List Elements (Mutability)

fruits = ["Apple","Banana","Mango","Cherry"]
print("fruits :",fruits)
print("Type of fruits :",type(fruits))
fruits[0] = "Grapes"
print("fruits :",fruits)
print("Type of fruits :",type(fruits))

#5.list Support indexing and Slicing.

names = ["Abhishek", "Piyush", "Neer","Ganesha"]
print("names[0] :",names[0]) # First element
print("names[1] :",names[1]) # Second Element
print("names[2] :",names[2]) # Third Element
print("names[3] :",names[3]) # Fourth Element
#Negative Indexing 
print("names[-1] :",names[-1]) # Last element
print("names[-2] :",names[-2]) # Third Element
print("names[-3] :",names[-3]) # Second Element 
print("names[-4] :",names[-4]) # First Element
