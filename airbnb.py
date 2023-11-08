#!/usr/bin/python3
import cmd

class MyConsole(cmd.Cmd):
    prompt = ">>>"

    def do_create(self, args):
        print("this method create ", args)

    
if __name__ == "__main__":
    MyConsole().cmdloop()