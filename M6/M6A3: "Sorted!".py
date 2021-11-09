students = input("Students: ")
array = students.split()
array.sort()
print("Class Roll")
for student in array:
  print(student)