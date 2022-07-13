list1 = [1, 2, 3]
list2 = (1, 2, 3,)

print(id(list1))

list1[2] = 3

print(id(list1))
print(id([1, 2, 3]))

print(id(list2))
print(id((1, 2, 3)))

print(id(list1[1]))
print(id(list2[1]))

print(id(list1[2]))
print(id(list2[2]))
