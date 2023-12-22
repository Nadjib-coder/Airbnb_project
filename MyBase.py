#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

class MyBaseClass:

    def __init__(self):
        # assign a few common default attributes to all instance of this class
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save_update(self):
        self.updated_at = datetime.now()

    def save_to_dict(self):
        dict_format =  self.__dict__
        dict_format["__class__"] = self.__class__.__name__
        return dict_format

print("=== start check save_update() method ===") 
obj_1 = MyBaseClass()
obj_1.name = "Nadjib"
obj_1.save_update()
print(obj_1.created_at)
print(obj_1.updated_at)
print("=== start check save_to_dict() method ===")
my_instance_1 = MyBaseClass()
serialized_data = my_instance_1.save_to_dict()
my_new_instance = MyBaseClass()
my_new_instance.__dict__.update(serialized_data)
print("my_instance_1 info:")
print(my_instance_1.id)
print(my_instance_1.created_at)
print("my_new_instance info:")
print(my_new_instance.id)
print(my_new_instance.created_at)
print(my_new_instance.__class__)
