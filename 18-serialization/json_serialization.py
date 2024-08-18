import json

def serialize_to_json(obj, filename):
    """serialize a Python object to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(obj, file, indent=4)
    print(f"Object serialized to JSON and saved to {filename}")

def deserialize_from_json(filename):
    """deserialize a JSON file to a Python object."""
    with open(filename, 'r') as file:
        obj = json.load(file)
    print(f"Object deserialized from JSON file: {filename}")
    return obj

if __name__ == "__main__":
    data = {
        "name": "Bob",
        "age": 30,
        "city": "New York",
        "is_student": False
    }

    # serialize data to JSON
    serialize_to_json(data, 'data.json')

    # deserialize data from JSON
    loaded_data = deserialize_from_json('data.json')
    print(loaded_data)
