# Create a list of the first 20 positive integers. Print the list.

first_20_positive_integers = range(1,21)
list_of_nos = list(first_20_positive_integers)
print(list_of_nos)

# Print the first, middle, and last elements of the list created in Assignment 1. 
first_element = list_of_nos[0]
length_of_list = len(list_of_nos)
middle_index = length_of_list/2
print(middle_index)
middle_element = list_of_nos[int(middle_index)]
last_element = list_of_nos[-1]

print(first_element, middle_element, last_element)

# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
first_Five_Elements = list_of_nos[:5]
last_Five_elements = list_of_nos[-5:]
list_Elements_5_to_15 = list_of_nos[5:16]
print(first_Five_Elements, last_Five_elements, list_Elements_5_to_15)

# Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.
list_of_random_nos = [5,3,1,8,2]
list_of_random_nos.sort()
print(list_of_random_nos)
print(sorted(list_of_random_nos, reverse=True))
print(set(list_of_random_nos))


# Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix) 
print(matrix[1][2])

# Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.
students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 72},
    {'name': 'Charlie', 'score': 95},
    {'name': 'David', 'score': 65},
    {'name': 'Eve', 'score': 78}
]

sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
for student in sorted_students:
    print(student)

# Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.
list1 = [1, 2, 3, 4, 5]
list1.reverse()
print(list1)
## or 
print(list1[::-1])

# Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.
first_10_positive_integers = list[int](range(1,11))

