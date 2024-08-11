
numbers = {1, 2, 3, 4, 5}

numbers.add(6)
print("Set after adding an element:", numbers)

numbers.remove(3)
print("Set after removing an element:", numbers)

numbers.add(5)
print("Set after adding a duplicate element:", numbers)

print("All numbers in the set:")
for number in numbers:
    print(number)

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union of sets:", set_a | set_b)
print("Intersection of sets:", set_a & set_b)
print("Difference of sets:", set_a - set_b)
