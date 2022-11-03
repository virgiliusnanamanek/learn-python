thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisDict)

# Accessing Items
x = thisDict.get("model")
print(x)

y = thisDict.keys()

print(y)

z = thisDict.values()

print(z)

p = thisDict.items()

print(p)

thisDict["year"] = 2016

print(thisDict)

# Adding Items

thisDict["color"] = "red"

print(thisDict)

# Removing Items

thisDict.pop("color")

print(thisDict)

# Loop Dictionaries

# print all the keys

for x in thisDict:
    print(x)

print("===================================")

# print all the values

for x in thisDict:
    print(thisDict[x])

print("===================================")
