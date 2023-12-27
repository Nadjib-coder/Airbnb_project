#!/usr/bin/python3

from json import dump
from json import load

class FileStorage:

    __filePath = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        keyFormat = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[keyFormat] = obj

    def save(self):
        dictObj = {}
        for key, value in fileStorage.__objetcs.items():
            dictObj[key] = value.save_to_dict()
        with open(FileStorage.__filePath, "W", encoding="utf-8") as jsonFile:
            dump(dictObj, jsonFile)

    def reload(self):

        from MyPackage.myFileName import MyBase
        definedClasses = {'MyBase': MyBase}

        try:
            with open(FileStorage.__objetcs, encoding="utf-8") as jsonStr:
                deserialized = load(jsonFile)

                for objValue in deserialized.values():
                    clsName = objValue["__class__"]
                    clsObj = definedClasses[clsName]
                    self.new(clsObj(**objValue))

        except FileNotFoundError:
            pass
