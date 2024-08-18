
This repository contains two Python scripts demonstrating how to serialize and deserialize Python objects using different methods.

## What is Serialization?

Serialization is the process of converting a Python object (like a dictionary, list, or custom object) into a format that can be easily stored in a file or transmitted over a network. This format can be easily converted back to the original Python object later. 

**Why Use Serialization?**
- **Data Storage**: You can save complex data structures to a file and reload them later. For example, you might save user preferences or application state so that they can be restored when the program runs again.
- **Data Exchange**: You can send data between different programs or services over a network. For example, a web service might send data to a client in JSON format.
- **Persistence**: Serialization helps in maintaining the state of an object between program runs.



## Files

- `json_serialization.py`: Shows how to serialize and deserialize Python objects using JSON.
- `pickle_serialization.py`: Shows how to serialize and deserialize Python objects using `pickle`.

## Usage

1. **`json_serialization.py`**

   - **Serialize to JSON**: This script `serialize_to_json` serializes a Python object to a JSON file (`data.json`).
   - **Deserialize from JSON**: It `deserialize_from_json` then deserializes the JSON file back into a Python object.

   Run the script with:
   ```bash
   python json_serialization.py
   ```
2. **`pickle_serialization.py`**

   - **Serialize to pickle**: This section `serialize_to_pickle` of the script serializes a Python object to a pickle file (`data.pkl`).
   - **Deserialize from pickle**: This section `deserialize_from_pickle` deserializes the pickle file (data.pkl) back into a Python object.

   Run the script with:
   ```bash
   python pickle_serialization.py
   ```



