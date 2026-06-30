#logical operators = evaluate multiple conditions (or, and,not)
#or = at least one condition must be true
#and= both must be true
#not= inverts the condition (not false, not true)
#Does remind me of logic gates i studied under semiconductor chapter during my prep 

'''temp = 39 
is_raining = False
if temp>40 or temo<0 or is_raining:
    print("The weather is bad today so the event is cancelled")
else:
    print("The weather is good today so the event is on")   
'''

temp =39
is_sunny = True
if temp>=35 and is_sunny:
    print("It is hot outside ♨️")
    print("It is sunny ☀️")
elif temp<=0 and is_sunny:
    print("It is cold outside 🥶")
    print("It is sunny ☀️")
elif temp>=35 and not is_sunny:
    print("It is hot outside ♨️")
    print("It is cloudy 🌥️")
    