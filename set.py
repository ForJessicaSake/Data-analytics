# Module 3: Data Structures Assignments
## Lesson 3.3: Sets

### Assignment 1: Creating and Accessing Sets
#Create a set with the first 10 positive integers. Print the set.
first_positive_numbers ={1,2,3,4,5,6,7,8,9,10}
print(first_positive_numbers)

### Assignment 2: Adding and Removing Elements
#Add the number 11 to the set created in Assignment 1. Then remove the number 1 from the set. Print the modified set.
first_positive_numbers.add(11)
first_positive_numbers.remove(1)

### Assignment 3: Set Operations
#Create two sets: one with the first 5 positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.
first_five_positive_numbers = {1,2,3,4,5}
first_even_integers = {2,4,6,8,10}

print(first_five_positive_numbers.union(first_even_integers))
print(first_five_positive_numbers.intersection(first_even_integers))
print(first_five_positive_numbers.difference(first_even_integers))
print(first_five_positive_numbers.symmetric_difference(first_even_integers))

### Assignment 4: Set Comprehensions
#Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.

### Assignment 5: Filtering Sets
#Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.

### Assignment 6: Set Methods
#Create a set with duplicate elements and remove the duplicates using set methods. Print the modified set.
duplicate_elements = {1,2,3,4,5,5,6,7,8,9,10}
duplicate_elements.remove(5)
# or 
print(duplicate_elements)

### Assignment 7: Subsets and Supersets
#Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.
first_five_positive_numbers={1,2,3,4,5}
first_three_positive_numbers={1,2,3}
is_subset =first_three_positive_numbers.issubset(first_five_positive_numbers)
is_superset = first_five_positive_numbers.issuperset(first_three_positive_numbers)
print(is_subset)
print(is_superset)

### Assignment 8: Frozenset
#Create a frozenset with the first 5 positive integers. Print the frozenset.
first_five_positive_numbers_frozenset = frozenset({1,2,3,4,5})
print(first_five_positive_numbers_frozenset)

### Assignment 9: Set and List Conversion
#Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set.
first_five_positive_numbers={1,2,3,4,5}
first_five_positive_numbers_list = list(first_five_positive_numbers)
first_five_positive_numbers_list.append(6)
print(set(first_five_positive_numbers_list))

### Assignment 10: Set and Dictionary
#Create a dictionary with set keys and integer values. Print the dictionary.

### Assignment 11: Iterating Over Sets
#Create a set and iterate over the elements, printing each element.
first_five_positive_numbers={1,2,3,4,5}
for i in first_five_positive_numbers:
    print(i)

### Assignment 12: Removing Elements from Sets
#Create a set and remove elements from it until it is empty. Print the set after each removal.
first_five_positive_numbers={1,2,3,4,5}
while len(first_five_positive_numbers) > 0:
    first_five_positive_numbers.pop()
    print(first_five_positive_numbers)

### Assignment 13: Set Symmetric Difference Update
#Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.
set1 ={1,2,3,4,5}
set2={2,3,4,5,6,7,8}
set1.symmetric_difference_update(set2)
print(set1)

### Assignment 14: Set Membership Testing
#Create a set and test if certain elements are present in the set. Print the results.
set1 ={1,2,3,4,5}
print(1 in set1)
print(6 in set1)

### Assignment 15: Set of Tuples
set_of_tuples = {(1,2),(3,4),(5,6),(7,8),(9,10)}
print(set_of_tuples)
#Create a set containing tuples, where each tuple contains two elements. Print the set.
