# Module 3: Data Structures Assignments
## Lesson 3.2: Tuples

### Assignment 1: Creating and Accessing Tuples
#Create a tuple with the first 10 positive integers. Print the tuple.

first_10_postive_integers_tuples=(1,2,3,4,5,6,7,8,9,10)
print(first_10_postive_integers_tuples)

### Assignment 2: Accessing Tuple Elements
#Print the first, middle, and last elements of the tuple created in Assignment 1.
first_element = first_10_postive_integers_tuples[0]
last_element= first_10_postive_integers_tuples[-1]
length_of_tuple=len(first_10_postive_integers_tuples)
middle_element= first_10_postive_integers_tuples[length_of_tuple//2]
print(first_element, middle_element, last_element)

### Assignment 3: Tuple Slicing
#Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.
first_three_elements =first_10_postive_integers_tuples[0:3]
last_three_elements= first_10_postive_integers_tuples[-3:]
index_2_to_5_elements = first_10_postive_integers_tuples[2:6]
print(first_three_elements, last_three_elements, index_2_to_5_elements)

### Assignment 4: Nested Tuples
#Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
nested_tuple=((1,2,3),(4,5,6),(7,8,9))
print(nested_tuple)
element_at_second_row_third_column=nested_tuple[1][2]
print(element_at_second_row_third_column)

### Assignment 5: Tuple Concatenation
#Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple.
tuple_one = (1,2,3)
tuple_two = (4,5,6)
concatenated_tuple = tuple_one + tuple_two
print(concatenated_tuple)

### Assignment 6: Tuple Methods
#Create a tuple with duplicate elements and count the occurrences of an element. Find the index of the first occurrence of an element in the tuple.
new_tuple =(1,2,3,4,4,5,6)
count_of_4 = new_tuple.count(4)
print(count_of_4)
index_of_4 = new_tuple.index(4)
print(index_of_4)

### Assignment 7: Unpacking Tuples
#Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.
five_element_turple =(1,2,3,4,5)
a,b,c,d,e = five_element_turple
print(a,b,c,d,e)

### Assignment 8: Tuple Conversion
#Convert a list of the first 5 positive integers to a tuple. Print the tuple.
list_of_first_5_positive_integers = [1,2,3,4,5]
tuple_of_first_5_positive_integers=tuple(list_of_first_5_positive_integers)
print(tuple_of_first_5_positive_integers)

### Assignment 9: Tuple of Tuples
#Create a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.
nested_tuple =((1,2,3),(4,5,6),(7,8,9))
for item in nested_tuple:
    print(item)

### Assignment 10: Tuple and List
#Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.
first_5_positive_integers_tuple =(1,2,3,4,5)
first_5_positive_integers_list = list(first_5_positive_integers_tuple)
first_5_positive_integers_list.append(6)
converted_back_to_tuple = tuple(first_5_positive_integers_list)
print(converted_back_to_tuple)

### Assignment 11: Tuple and String
#Create a tuple with the characters of a string. Join the tuple elements into a single string. Print the string.
character_of_string = ('h','e','l','l','o')
joined_string= "".join(character_of_string)
print(joined_string)

### Assignment 12: Tuple and Dictionary
#Create a dictionary with tuple keys and integer values. Print the dictionary.

### Assignment 13: Nested Tuple Iteration
#Create a nested tuple and iterate over the elements, printing each element.
nested_tuple =((1,2,3),(4,5,6),(7,8,9))
for item in nested_tuple:
    print(item)

### Assignment 14: Tuple and Set
#Create a tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.
duplicate_elements_tuple =(1,2,3,4,4,5,6)
set_of_duplicate_elements = set(duplicate_elements_tuple)
print(set_of_duplicate_elements)

### Assignment 15: Tuple Functions
#Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.