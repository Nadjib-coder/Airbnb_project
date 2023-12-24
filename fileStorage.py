#!/usr/bin/python3

from json import dump

class FileStorage:

    __filePath = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(slef, obj):
        keyFormat = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[keyFormat] = obj

    def save(self):
        dictObj = {}
        
        for key, value in FileStorage.__objects.items():
            dictObj[key] = value.save_to_dict()
        
        with open(FileStorage.__filePath, "w", encoding="utf-8") as jsonFile:
            dump(dictObj, jsonFile)
