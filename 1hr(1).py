#ACCEPTING USER 
name = input("Enter your name: ")
age = input("Enter your age: ")
print(name)
age=int(age)#otherwise adding will not be possible
age+=1
print(f"Hello {name}! You are {age} years old.")

#if age >=18:
  #  print("You are a full grown man")
#else:
 #   print("You are still a child")

if age<0 : 
    print("You are not born yet")
elif age>=65:
    print("You are an old man")
elif age<18:
    print("You are still a child")
elif age>=18 and age<65:
    print("You are an adult")

has_tickets= True
if has_tickets and age>=18:
    print("You can enter the movie theater ")
elif has_tickets and age<18:
    print("Sorry this ain't a movie for kids")
elif has_tickets==False:
    print("You can't enter the movie theater without a ticket")