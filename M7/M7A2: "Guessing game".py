n = "electricity"
print("What is my favourite food?")
us = input("Guess? ")
while us != n:
    print("Not even close.")
    us = input("Guess? ")
if us == n:
  print("You guessed it! Buzzzz")