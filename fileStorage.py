#!/usr/bin/python3

class FileStorage:

    __filePath = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(slef, obj):
        keyFormat = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[keyFormat] = obj
