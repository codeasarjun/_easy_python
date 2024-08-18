import pickle

def serialize_to_pickle(obj, filename):
    """serialize a Python object to a pickle file."""
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)
    print(f"Object serialized to pickle and saved to {filename}")

def deserialize_from_pickle(filename):
    """deserialize a pickle file to a Python object."""
    with open(filename, 'rb') as file:
        obj = pickle.load(file)
    print(f"Object deserialized from pickle file: {filename}")
    return obj

if __name__ == "__main__":
    data = {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles",
        "is_student": True
    }

    # serialize data to pickle
    serialize_to_pickle(data, 'data.pkl')

    # deserialize data from pickle
    loaded_data = deserialize_from_pickle('data.pkl')
    print(loaded_data)
