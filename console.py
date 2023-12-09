#!/usr/bin/python3
"""defines consol file"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ command class for console"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ end of file"""
        return True

    def do_quit(self, line):
        """ quit command"""
        "Exit"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
