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

my_model = MyBaseClass()
my_model.name = "Nadjib"
my_model.save_update()
print(my_model.created_at)
print(my_model.updated_at)
