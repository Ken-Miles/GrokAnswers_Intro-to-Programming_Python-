x = "electricity"
print("What is my favourite food?")
guess = input("Guess? ")
while guess != x:
    print("Not even close.")
    guess = input("Guess? ")
if guess == x:
  print("You guessed it! Buzzzz")
