thisTuple = ("orange", "banana", "cherry", "apple", "strawberry", "raspberry")  # immutable => cannot be changed
# after created
print(thisTuple)

# Access Tuple Items
print(thisTuple[1])

# Update Tuples
# To update the tuple, I must convert it first to list

toList = list(thisTuple)
toList[1] = "mango"

updateTuple = tuple(toList)

print(updateTuple)

# Unpack Tuples

(orange, mango, cherry, apple, *rest) = updateTuple

print(orange)
print(mango)
print(cherry)
print(apple)
print(rest)

# Loop Tuples

for x in updateTuple:
    print(x)
