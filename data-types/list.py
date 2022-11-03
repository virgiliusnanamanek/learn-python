mylist = ["apple", "banana", "cherry"]
print(mylist)

# Access List Items
print("The second list: ", mylist[1])
print("The minus order (last)", mylist[-1])

if "apple" in mylist:
    print("Yes, it exists!")

# Change List Item

mylist[1] = "Coconut"  # Change one of the lists
print(mylist)

mylist[1:2] = ["blackcurrant", "watermelon"]  # Change a Range of Item Values
print(mylist)

mylist.insert(2, "Banana")
print(mylist)

# Add List Items

mylist.append("orange")
print(mylist)

otherList = ["mango", "pineapple", "papaya"]

mylist.extend(otherList)
print(mylist)

tupleList = ("kiwi", "orange")
mylist.extend(tupleList)
print(mylist)

# Remove List Items

mylist.remove("orange")
print(mylist)

mylist.pop(2)
print(mylist)

del mylist[3]
print(mylist)

# Loop Lists

# for x in mylist:
#     print(x)

[print(x) for x in mylist]

# List Comprehension

newList = []

for x in mylist:
    if 'a' in x:
        newList.append(x)
print(newList)

# Sort Lists

mylist.sort()

print(mylist)

mylist.sort(reverse=True)
print(mylist)
