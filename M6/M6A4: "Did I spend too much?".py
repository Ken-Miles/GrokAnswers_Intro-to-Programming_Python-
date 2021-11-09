expenses = input("Enter the expenses: ")
data = expenses.split()
desired_array = [int(numeric_string) for numeric_string in data] # Honestly may look long but it's simpler therefore divine intellect
print("Total: $" + str(sum(desired_array))) 