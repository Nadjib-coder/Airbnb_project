import cmd


class MyCmdInterpreter(cmd.Cmd):
    prompt = '>> '  # Set the command prompt

    def do_greet(self, arg):
        """Greet the user."""
        print(f"Hello, {arg}!")

    def do_add(self, arg):
        """Add two numbers."""
        try:
            numbers = [int(x) for x in arg.split()]
            result = sum(numbers)
            print(f"Sum: {result}")
        except ValueError:
            print("Invalid input. Please provide space-separated numbers.")

    def do_quit(self, arg):
        """Exit the command interpreter."""
        print("Quitting.")
        return True


if __name__ == '__main__':
    my_cmd = MyCmdInterpreter()
    my_cmd.cmdloop("Welcome to the command interpreter!")
