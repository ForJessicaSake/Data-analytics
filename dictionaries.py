import json

# Assignment 1: Creating and Accessing Dictionaries
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.
first_postive_integers_squares = {i: i**2 for i in range(1, 11)}
print(first_postive_integers_squares)

# Assignment 2: Accessing Dictionary Elements
# Print the value of the key 5 and the keys of the dictionary created in Assignment 1.

value_5 = first_postive_integers_squares[5]
keys = first_postive_integers_squares.keys()
print(f"Value of key 5: {value_5}")
print(f"Keys of the dictionary: {keys}")

# Assignment 3: Dictionary Methods
# Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.
first_postive_integers_squares[11]= 11**2
del first_postive_integers_squares[1]
print(first_postive_integers_squares)   

# Assignment 4: Iterating Over Dictionaries
# Iterate over the dictionary created in Assignment 1 and print each key-value pair.
for item in first_postive_integers_squares.items():
   print(f"Key: {item[0]}, Value: {item[1]}")


# Assignment 5: Dictionary Comprehensions
# Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.
first_10_positive_integers_cubes ={i:i**3 for i in range(1,11)}
print(first_10_positive_integers_cubes)

# Assignment 6: Merging Dictionaries
# Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.
first_dict = {i:i**2 for i in range(1,6)}
second_dict = {i:i**2 for i in range(6,11)}
merged_dict = first_dict | second_dict
print(merged_dict)

# Assignment 7: Nested Dictionaries
# Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.
student_dict = {
    "name":"John",
    "age":20,
    "grades":{
        "math":90,
        "science":80,
        "english":70
    },    
}
print(student_dict)

# Assignment 8: Dictionary of Lists
# Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.
first_5_postive_integers_multiples ={i: [i*j for j in range(1,6)] for i in range(1,6)}
print(first_5_postive_integers_multiples)

# Assignment 9: Dictionary of Tuples
# Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.
first_5_positive_integers_squares_tuples = {i: (i, i**2) for i in range(1,6)}
print(first_5_positive_integers_squares_tuples)


# ### Assignment 10: Dictionary and List Conversion
# Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.
first_5_positive_integers_squares = {i: i**2 for i in range(1,6)}
tuples_list = [(key, value) for key, value in first_5_positive_integers_squares.items()]

#  Assignment 11: Dictionary Filtering
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.
dict_1 = {i : i**2 for i in range(1,11)}
dict_2 = {i : i**2 for i in range(1,11) if i %2 ==0}
print(dict_1)
print(dict_2)

# Assignment 12: Dictionary Key and Value Transformation
# Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary.
dict_3 = {i:i**2 for i in range(1,6)}
dict_4 = {value:key for key,value in dict_3.items()}
print(dict_3)
print(dict_4)

# Assignment 13: Default Dictionary
# Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.
default_dict = {
    "name": [],
    "age": [],
    "city": []
}
default_dict["name"].append("John")
print(default_dict)

# Assignment 14: Counting with Dictionaries
# Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.
def count_character(character):
    count_dict ={i: character.count(i) for i in character}
    return count_dict

result = count_character("hello")
print(result)

# Assignment 15: Dictionary and JSON
# Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.
book={
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "genre": "Tragedy"
}

json_string = json.dumps(book)
print(json_string)