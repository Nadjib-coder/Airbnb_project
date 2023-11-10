#!/usr/bin/python3
import cmd

class MyConsole(cmd.Cmd):
    prompt = ">>> "

    def do_create(self, args):
        print("this method create", args)
    
    def precmd(self, line):
        # command, other = line.split(" ")
        # line = f"{command} Shoes"
        if "." in line:
           line = line.replace(".", " ").replace("(", "").replace(")", "")
           line = line.split(" ")
           line = f"{line[1]} {line[0]}"
        print(line)
        return cmd.Cmd.precmd(self, line)

    
if __name__ == "__main__":
    MyConsole().cmdloop()