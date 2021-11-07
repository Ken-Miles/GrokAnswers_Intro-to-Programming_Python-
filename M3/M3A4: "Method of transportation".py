rain = input("Is it currently raining? ")
if rain == "Yes":
    print("You should take the bus.")
else:
    if rain == "No":
        km = int(input("How far in km do you need to travel? "))

    if km > 10:
        print("You should take the bus.")

    elif km < 2:
        print("You should walk.")
    
    else:
        print("You should ride your bike.")