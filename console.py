#!/usr/bin/python3
"""defines consol file"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ command class for console"""
    prompt = "(hbnb) "
    __classes = {"BaseModel",
                 "User",
                 "Review",
                 "Amenity",
                 "City",
                 "State",
                 "Place"}

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_EOF(self, line):
        """ End of file"""
        return True

    def help_EOF(self):
        """ Help for EOF"""
        print("Help for EOF")
        print("Used for exiting command")

    def do_quit(self, line):
        """ Quit command"""
        "Exit"
        return True

    def help_quit(self):
        """ Help for quit"""
        print("Help for quit")
        print("Used for exiting command")

    def do_create(self, line):
        """ Creates new instance of a class, saves it to the JSON file
        Syntax: create <class_name>"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, line):
        """ Prints the string representation of an instance"""
        objdict = storage.all()
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """ Deletes an istance based on the class name and Id
        Usage: destroy <class name> id"""
        objdict = storage.all()
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, line):
        """ Prints all string representation of al instances
        Usage: all <class name> or all"""
        args = line.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(args) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, line):
        """ Usage: update <class name> <id> <attribute name>
        "<attribute value>"""
        args = line.split()
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            if len(args) == 4:
                obj = objdict["{}.{}".format(args[0], args[1])]
                if args[2] in obj.__class__.__dict__.keys():
                    valtype = type(obj.__class__.__dict__[args[2]])
                    obj.__dict__[args[2]] = valtype(args[3])
                else:
                    obj.__dict__[args[2]] = args[3]
            elif type(eval(args[2])) == dict:
                obj = objdict["{}.{}".format(args[0], args[1])]
                for k, v in eval(args[2]).items():
                    if (k in obj.__class__.__dict__.keys() and
                       type(obj.__class__.__dict__[k]) in {str, int, float}):
                        valtype = type(obj.__class__.__dict__[k])
                        obj.__dict__[k] = valtype(v)
            else:
                obj.__dict__[k] = v
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
