message = input("Message? ")
length = len(message)
output = ""
for i in range(0,length-1,3):
  output = output+(message[i]+" ")
print(output.rstrip())