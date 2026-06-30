#List[]= mutable, most flexible
#Tuple() immutable, faster
#set{}= mutable(add,remove),unordered
#       No duplicates best for membership testing 

fruits = {"apple","orange","bannana", "coconut"}
#fruits[0]="Pineapple" to replace
#fruits.append("mango") add krne ke liye
#fruits.remove("bannana")#remove krne ke liye
#fruits.pop(2) to remove by index
#fruits.clear()#to clear the list

#for fruit in fruits:
#   print(fruit, end=" ")

#Tupple cant be changed but their elements are faster to retrieve
#Good if you need a lust that you dont wanna change
#sets the order isnt fixed so they print randomly, they dont support index assignments they can be added using .add() method and removed using remove() method   fruits.add("mango")
fruits.add("mango")
fruits.remove("bannana")
#clear can be used pop doesnt work as they dont have index
#fruits.remove("apple")
fruit= input("Enter a fruit to check if it is present in the set: ")
if fruit in fruits:
    print(f"{fruit} is present in the set")
else:   
    print(f"{fruit} is not present in the set") 

#And we are done with our first video of python it was a good introduction