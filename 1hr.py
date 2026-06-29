#This is my first python program

print("I like bubble tea")
print("It's really good")

# A vairable= A eusable container for a value (string,integer, float boolean)
#The variable behaves as if it was the value it contains( wriing it down for future refrence)

full_name = "Mega Slayer"
age =19
gpa= 9.5 #hypothetical
is_student=True

print(f"Hello {full_name}")
print(f"You are {age} years old")
print(f"Your gpa is {gpa}")
print(f"Are you a student?:{is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a student")

'''Arithematic =+ addition
                - subtraction
                * multiplication
                /division returns a float
                //integer division
                %remainder of a division'''

friends =5
friends+=1

print(friends)

friends-=5
print(friends)

friends*=49
print(friends)

friends/=7
print(friends)

friends //=7
print(friends)

remaining_friends=friends%11
print(remaining_friends)

#Typecasting= the process of converting a variable from one data type to another 
#str(), int(), float(), bool()

#gpa=int(gpa)
#print(gpa)

#age= str(age)
#print(type(age))
#age+=1(wont work now since it is a string)
#age+="1"
#print(age)#i am now 191 year old like real old
#full_name = bool(full_name) 
#print(full_name)
#false implies no name input
#looks like if i drag this single file too long it will become complex so on to the next one