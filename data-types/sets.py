thisSet = {"apple", "banana", "cherry", "apple"}  # it not allows duplicated value
print(thisSet)

# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Access Set Items

for data in thisSet:
    print(data)

# Add Set Items

thisSet.add("mango")
thisSet.add("watermelon")  # it would print the value unordered
print(thisSet)
# Remove Set Items
thisSet.remove("mango")
print(thisSet)
