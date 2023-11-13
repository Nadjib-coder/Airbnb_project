import json

# reading from a json file
with open("example.json", "r") as json_file:
    data_read = json.load(json_file)

# Now 'data_read' contains the python dictionary read from the json file
print("Data read from 'example.json':", data_read)
print("the type of this data is:", type(data_read))