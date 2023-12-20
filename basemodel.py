#!/usr/bin/python3

# I will create the Basemodel class for th airbnb clone project

from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        self.created_at = datetime.now().isoformat()

        print(f"created at: {self.created_at}")
        """
        if not hasattr(self, 'created_at'):
            self.created_at = datetime.now().isoformat()
            print(f"created_at: {self.created_at}")
        
        if args:
            for values in args:
                print(values)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return "\n".join([f"{key}: {value}" for key, value in self.__dict__.items()])

print("==== outputs of args below ====")
mod_1 = BaseModel("nadjib", "fares", "ali", "abdou")

mod_2 = BaseModel(name="Nadjib", age=21, city="Paris", job="Software Engineer")
print("==== outputs of kwargs below ====")
print(mod_2)
