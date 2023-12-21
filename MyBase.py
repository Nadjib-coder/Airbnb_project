#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

class MyBaseClass:

    def __init__:
        # assign a few common default attributes to all instance of this class
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save_update(self):
        self.updated_at = datetime.now()
