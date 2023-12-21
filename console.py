#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
    """simple command processor example."""

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print(f"Hello {person}")
        else:
            print("Hello")

    def do_EOF(self, line):
        return True

if __name__ == "__main__":
    HelloWorld().cmdloop()
