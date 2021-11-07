## Python Programs for Grok "Introduction to Python"

## Module 1

## M1A1: "Hello world"
print("Hello, World!")

## M1A2: "Hello to you, too"
name = input('What is your name? ')
print('Hello, ' + name)

## M1A3: "Hello with attitude"
name = input("What is your name? ")
print("So you call yourself '" + name + "' huh?")

## M1A4: "Hello to you three!"
f1 = input("Friend: ")
f2 = input("Friend: ")
f3 = input("Friend: ")
print("Hello, young " + f1)
print("Hello, wise " + f2)
print("Hello, brave " + f3)

## Module 2

## M2A1: "Length of a string"
input = input("Enter text: ")
print(len(input))

## M2A2: "1-Up"
old = int(input("Please enter a number: "))
offset = int(1)
print(old + offset)

## M2A3: "Python! ^_^" 
user = int(input("Enter a number: "))
print("^" + str("_") * user + "^" )

## M2A4: "Repeaterbot"
word = input("What do you want me to say? ")
times = int(input("How many times do you want me to say it? "))
print(word * times)

## Module 3

## M3A1: "Open sesame!"
password = input("What is the password Ali? ")
if password == "Open sesame!":
    print("The cave door opens!")

## M3A2: "Access denied"
password = input("Enter password: ")
if password == "chEEzburg3rz":
    print("Access granted")
else: 
    print("Access denied")

## M3A3: "In the black"
Number = int(input("Number: "))
if Number >= 0:
    print("In the black :)")
else:
    print("In the red :(")

## M3A4: "Method of transportation"
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

## Module 4

## M4A1: "Aardvark!"
name = input('Enter line: ') 
if 'aardvark' in name:
  print('Aardvark!')
else:
  print('No aardvarks here :(')

## M4A2: "Don't SHOUT!""
loud = input("Loud: ")
print("Quiet: " + loud.lower())

## M4A3: "Broken keyboard"
n = input("What did she say? ")
n = n.replace('###', 'o')
n = n.replace('%%', 'a')
n = n.replace('##', 'e')
print("She meant to say: " + n)

## M4A4: "Short/Long Names"
name = input("Enter your name: ")
if len(name) <= 3:
    print("Hi " + name + ", you have a short name.")

elif len(name) >= 4 and len(name) <= 8:
    print("Hi " + name + ", nice to meet you.")
    
else:
    print("Hi " + name + ", you have a long name.")

## Module 5

## M5A1: "Give me a G!"
name = input('Cheer: ')
for character in name:
  print("Give me a " + character + ", " + character + "!")
print("What does it spell?")
print(name.upper())

## M5A2: "Count to N"
number = int(input("Enter a number: "))
for i in range(1, number):
    print(i)
print(number)

## M5A3: "Speaking Backwards!"
name = input("Line: ")