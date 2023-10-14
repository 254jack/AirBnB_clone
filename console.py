#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = "(hbnb)"
    
    def emptyline(self):
        pass
    def do_quit(self, line):
        exit()
    def help_quit(self):
        print("Quit command to exit the program")
    def help_EOF(self):
        print("The end of file that exits the loop at the end of a file read")
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    