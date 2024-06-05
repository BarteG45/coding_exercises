#DESCRIPTION
'''
Create two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78].

Use the zip function to combine these lists into a list of tuples.

Use list comprehension to create a new list containing strings in the format "Name: score" for each element.'''

#MY SOLUTION
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

combined_list = list(zip(names,scores))

formatted_list = [f"{name}: {score}" for name, score in combined_list]
print(formatted_list)