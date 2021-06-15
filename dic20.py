# dictionary
# indexed by keys, can be any immutable type

d = {"pet": "dog", "age": 5, "name": "kgb"}
print(type(d))
d = dict(pet="dog", age=5, name="spot")
print(d.items())
print(d.keys())
print(d.values())

print(d["pet"])

# add an item
d["add"] = "sit"

# remove an item
del d["add"]  # the value associate with the key is also gone


for key in d.keys():
    print(f"{key} = {d[key]}")
