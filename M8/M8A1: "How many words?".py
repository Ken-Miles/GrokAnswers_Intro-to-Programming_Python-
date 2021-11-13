a = []
n = "Word: "
line = input(n)
while line:
    a.append(line)
    line = input(n)
a = list(set(a))
a.sort()
print("You know",len(a),"unique word(s)!")