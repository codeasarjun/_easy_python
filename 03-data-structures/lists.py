fruits = ["apple", "banana", "cherry"]

print("First fruit:", fruits[0])

fruits.append("date")
print("List after adding a fruit:", fruits)

fruits.remove("banana")
print("List after removing a fruit:", fruits)

print("All fruits in the list:")
for fruit in fruits:
    print(fruit)


print("First two fruits:", fruits[:2])
