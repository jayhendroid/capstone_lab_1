# Part 2: List of classes - lists and loops
#
# Write a program that asks for the names of all of the classes you are taking this semester
# Save these class names in a list.
# Print all the items in the list, one per line.

num_classes = int(input('How many classes do you have? '))

classes = []



for i in range(num_classes):
    class_name = input(f'Enter the name of class #{i + 1}: ')
    classes.append(class_name)

print('\nYour classes this semester:')
for course in classes:
    print(course)