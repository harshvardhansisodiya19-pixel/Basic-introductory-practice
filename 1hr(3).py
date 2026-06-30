#While loop= used to repeat a block of code as long as a condition is true we recheck the condition at end of loop.
#while 1==1:
    #print("This is an infinite loop")
    #break
name = input("Enter your name: ")
while name =="":
    name =input("Enter your name:")

age=int(input("Enter your age: "))
print(f"Hello {name}!")
while age<0:
    print("Age cannot be negative. Please enter a valid age.")
    age=int(input("Enter your age: "))

print(f"You are {age} years old.")