#!/usr/bin/python3
"""defines consol file"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ command class for console"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_EOF(self, line):
        """ End of file"""
        return True

    def help_EOF(self):
        """ Help for EOF"""
        print ("Help for EOF")
        print ("Used for exiting command")

    def do_quit(self, line):
        """ Quit command"""
        "Exit"
        return True

    def help_quit(self):
        """ Help for quit"""
        print ("Help for quit")
        print ("Used for exiting command")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
