#!/usr/bin/python3

from datetime import datetime

class BaseModel:
    def __init__(self):
        self.created_at = datetime.now()

    def __str__(self):
        return "BaseModel object created at {}".format(self.created_at)

mod_1 = BaseModel()
print(mod_1)
