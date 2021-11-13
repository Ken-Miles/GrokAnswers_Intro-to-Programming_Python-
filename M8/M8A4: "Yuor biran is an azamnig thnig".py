n = input("Enter words: ")
m = n.split()
w1 = m[0]
w2 = m[1]
w1a = list(w1)
w2a = list(w2)
w1a.sort()
w2a.sort()
if w1a == w2a and w1[0] == w2[0] and w1[-1] == w2[-1]:
  print("Super Anagram!")
else:
  print("Huh?")