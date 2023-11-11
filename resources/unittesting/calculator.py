#!/usr/bin/python3

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multipy(self, a, b):
        return a * b

    def devid(self, a, b):
        if b == 0:
            raise ValueError("Cannot devide by zero.")
        return a / b
