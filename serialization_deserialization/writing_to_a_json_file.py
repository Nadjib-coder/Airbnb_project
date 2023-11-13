import json

# Sample data to be written to a JSON file
data_to_write = {
    "name": "John Doe",
    "age": 30,
    "city": "Example City"
}

# writing to a json file
with open("example.json", "w") as json_file:
    json.dump(data_to_write, json_file)

print("Data written to 'example.json'")