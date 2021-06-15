# data type: list (mutable)
# create a list
names = ["Chloe", "Victoria", "Jackson"]
# find the index of an item
names.index("Jackson")
# loop through the list
for i, name in enumerate(names):
    pass
    # print(f"{name} is in index {i}")
# adding items: append, insert
names.append("Michael")
names.insert(0, "Jesus")  # adds at a specific index

# removing items: remove, pop, delete
# Remove() deletes the matching element from
# the list whereas the del and pop removes the element present at specified index
names.remove("Michael")
names.pop()  # pop(index) #remove the item but extract the item
# del x[index]  # delete without returning the item

# Extending
names2 = ["cats", "dogs", "birds"]
names.extend(names2)


# Sorting - sort, reverse, will raise error
# if mixed types exist
names.sort()
names.reverse()

# copy
names2 = names.copy()
names3 = names[:][::-1]  # reverse
print(names3)

# clear
names3.clear()
print(names3)
