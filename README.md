# AirBnB clone - The console
## Welcome to the AirBnB clone project!
### First step: Write a command interpreter to manage your AirBnB objects.
In this project I'm building the first step full web application: the AirBnB clone which is The command interpreter part.
In this project different tasks are covered:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
Using Command interpreter we will be able to manage objects of a project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### How to start the command interpreter?
python3 console.py


### How to use it?
By writing the command we want which are executed.

Example:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit

