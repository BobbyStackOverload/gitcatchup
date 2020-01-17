number = int(input("Day (0-6)? "))

if (number == 0 ):
    day = "Sunday"
elif (number == 1 ):
    day = "Monday"
elif (number == 2):
    day = "Tuesday"
elif (number == 3):
    day = "Wednesday"
elif (number == 4):
    day = "Thursday"
elif (number == 5):
    day = "Friday"
elif (number == 6):
    day = "Saturday"
else: 
    day = "Please enter number between 0 and 6 "

print(day) 
