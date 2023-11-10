#!/usr/bin/python3
import cmd

class MyConsole(cmd.Cmd):
    prompt = ">>> "

    def do_create(self, args):
        print("this method create ", args)
    
    def precmd(self, line):
        command, other = line.split(" ")
        line = f"{command} Shoes"
        print(line)
        return cmd.Cmd.precmd(self, line)

    
if __name__ == "__main__":
    MyConsole().cmdloop()