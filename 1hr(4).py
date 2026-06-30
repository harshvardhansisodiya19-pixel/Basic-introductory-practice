#for loop = used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.(string, list,tuple, set)
# repeat a block of code an exact amount of times.

for i in range(91,111,2):#first inclusive last exclusive one more comma defines interval
    print(i)
name =" Mega Slayer"

for letter in name:
    print(letter, end="-")

import time
for i in range(10,0,-1):
    print(i)
    time.sleep(2)
print("Happy New Year 🎉")
