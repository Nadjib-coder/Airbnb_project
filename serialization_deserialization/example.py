import json

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the class
obj = MyClass(name="John", age=25)

# Serialize the object to a JSON-formatted string
json_str = json.dumps(obj.__dict__)

# Save the JSON string to a file
with open("serialized_data.json", "w") as file:
    file.write(json_str)

# Read the JSON string from the file
with open("serialized_data.json", "r") as file:
    loaded_json_str = file.read()

# Deserialize the JSON string back into an object
loaded_obj = MyClass(**json.loads(loaded_json_str))

# Now, 'loaded_obj' is an instance of MyClass
print(loaded_obj.name)  # Output: John
print(loaded_obj.age)   # Output: 25
