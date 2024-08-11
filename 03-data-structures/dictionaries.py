
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print("Name:", person["name"])

person["email"] = "test@example.com"
print("Dictionary after adding an email:", person)

del person["city"]
print("Dictionary after removing city:", person)

print("Dictionary keys and values:")
for key, value in person.items():
    print(f"{key}: {value}")

print("Email:", person.get("email", "Not found"))
