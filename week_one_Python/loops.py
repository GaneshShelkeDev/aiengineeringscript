# List Comprehension

# range(start, stop, step)

# range() returns a range object, not a list.

# It generates numbers when you iterate over it.

# It is memory-efficient because it doesn't need to store every number like a list.



squers = [n*n for n in range(10)]

print(squers)

evens = [n for n in range(10) if n%2==0 ]
print(f"even numbers: {evens}")

# [ expression    for loop    condition ]
# [expression for item in iterable if condition]

greter = [n for n in range(10) if n>= 5]
print(f"gretter number above 5 in 10 serse is = {greter}")

# Scope (LEGB). Python looks up names in Local, Enclosing, Global, Built-in order. 

def defaultarrgs(gredding, name, surname):
    return( gredding , surname , name)


defaultarrgs()