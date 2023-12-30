#!/usr/bin/pyhton3
# this module instantiates an objects from a class FileStorage
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
