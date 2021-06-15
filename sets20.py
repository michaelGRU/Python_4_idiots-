# set
# unordered, unique, immutable

num = {1, 2, 2, 3, 4, 5}
l = [1, 2, 2, 3, 4, 5]
s = set(l)

# add item
s.add("hi")
s.update([8, 9, 10])
# print(s)

# remove item
s.discard("hi")  # wil not throw error
s.remove(1)  # will throw error if not exist

x = set("abcd")
y = set("cdefg")
s = x.union(y)  # all the elements that are in either set

s = x.intersection(y)  # all the elements that are in both sets

s = x.difference(y)  # all in x but not in y

s = x.symmetric_difference(y)  # all the elements in one of the sets


set1 = {1, 2, 4}
set2 = {4, 5, 6}
print(len(set1 & set2))
