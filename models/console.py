#!/usr/bin/python3

import cmd


class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    FRIENDS = ['Nadjib', 'Fares', 'Abdou', 'Ali']

    def do_greet(self, person):
        if person and person.lower() in [friend.lower() for friend in self.FRIENDS]:
            print(f"Hi {person}")
        elif person:
            print(f"Hello {person}")
        else:
            print("Hello")

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            return self.FRIENDS[:]
        else:
            return [friend for friend in self.FRIENDS
                    if friend.lower().startswith(text.lower())]

    def help_greet(self):
        print("\n".join(["greet [person]", "Greet the named person"]))

    def do_EOF(self, line):
        return True

    def postloop(self):
        print()


if __name__ == '__main__':
    HelloWorld().cmdloop()
