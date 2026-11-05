# Types, strings, lists, tuples, dicts, sets, control flow, functions

# string = "Hello Ganesh"
# print(string)

# a = "5"
# b = 1
# print(a+b)




list = [1,2, 50, 60, 'A', "Ganesh"]
list.append(108)
list.remove(50)
list.insert(2, 100)
list.pop(3)
# list.sort()
list.reverse()
# list.clear()
list.extend([1,2,3,4,5])
list_copy = list.copy()
list_count = list.count(1)

# print(list)
# print(list_copy)
# print(list_count)


a = [1, 2]
b = a
b.append(3)
# print(a, a is b) #([1,2,3], True)

x = [[0] * 3] * 3
# x = [[0, 0, 0]] * 3
# x = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(x)
x[0][0] = 1
# print(x) #[[1,0,0],[0,0,0],[0,0,0]]


nums = [3, 1, 2]
result = nums.sort()
print(result)
print(nums.sort())
