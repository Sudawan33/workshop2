# EXAMPLE 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # Ouput: ['apple', 'cherry']

# EXAMPLE 2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # Ouput: ['apple', 'cherry']

# EXAMPLE 3
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # Ouput: ['apple', 'banana']

# EXAMPLE 4
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # Ouput: ['banana', 'cherry']

# EXAMPLE 5
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # Ouput: []
