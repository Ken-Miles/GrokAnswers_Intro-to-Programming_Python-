day_input = input("Which days had rain? ")
withoutrain = 7 - len(day_input.split())
print("Number of days without rain: " + str(withoutrain))