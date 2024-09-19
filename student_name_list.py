# Create a list of 20 student names
student_names = ["Alice", "Bob", "Charlie", "David", "Emily",
                 "Frank", "Grace", "Henry", "Isabella", "Jack",
                 "Kevin", "Lily", "Mia", "Noah", "Olivia",
                 "Penelope", "Quinn", "Robert", "Sophia", "Thomas"]

# a. Print the entire list
print("Student Names:")
for name in student_names:
  print(name)

# b. Access and print the 15th index
print("\n15th index is:", student_names[14])

# c. Update the 12th index to "John"
student_names[11] = "John"
print("\nUpdated List:")
for name in student_names:
  print(name)

# d. Delete the 10th index
del student_names[9]
print("\nUpdated List after deletion:")
for name in student_names:
  print(name)

# e. Slice the list from index 2 to 5 and print the sliced portion
sliced_list = student_names[2:5]
print("\nSliced list (index 2 to 5):", sliced_list)

# f. Print the last index of the list
print("\nLast index is:", student_names[-1])