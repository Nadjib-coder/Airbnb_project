#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

class MyBaseClass:

    def __init__(self, *args, **kwargs):
        if kwargs:
            del kwargs['__class__']
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dtime_obj = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dtime_obj)
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save_update(self):
        self.updated_at = datetime.now()

    def save_to_dict(self):
        dict_format = {}
        dict_format["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_format[key] = value.isoformat()
            else:
                dict_format[key] = value
        
        return dict_format

    def __str__(self):
        return f"{[self.__class__.__name__]} {self.id} {self.__dict__}"

# creating a class instance and update it with a few attributes
my_model = MyBaseClass()
my_model.name = "Nadjib Mouhoun"
my_model.age = 21
print(my_model.id)
print(my_model)
print(my_model.created_at)
print("\n------- Serialized to dictionary below -------\n")
my_model_json = my_model.save_to_dict()
print(my_model_json)
print("\n------ JSON of <'my_model'> below ------\n")
for key, value in my_model_json.items():
    print("\t{}: ({}) - {}".format(key, type(value), value))
print("\n ------ deserialized to an instance below ------\n")
#parse in the dictionary to the class constructor for deserialization
new_model = MyBaseClass(**my_model_json)
print(new_model.id)
print(new_model)
print(new_model.created_at)
print("\n------ the two instanceses compared below -----\n")
print(new_model is my_model)
