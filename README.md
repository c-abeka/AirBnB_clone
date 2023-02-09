# AirBnB Clone - The Console

The console is the first segment of the AirBnB project at ALX Software Engineering Track. This console is a backend interface to manage program data.

The goal of this project is to eventually deploy a simple copy of the AirBnB website to a server. A command interpreter for managing objects for the website is created in this section.

### Functionality of the Command Interpreter

- Create objects.
- Retrieve stored objects.
- Perform operations on objects.
- Update attributes on objects.
Destroy objects.

## Table of Content
---
- [usage](/README.md/#AirBnB_clone/##Usage)
- [Installation](/##Installation)
- [File Descriptions](/README.md/#AirBnB_clone/##"File)
- [Usage](/##Usage)
- [Examples of Use](/##Examples)
- [Bugs](/##Bugs)
- [Authors](/##Authors)

## Usage
---
- Clone this repository.
`https://github.com/c-abeka/AirBnb_clone.git`
- Navigate to this folder: `cd AirBnB_clone`
- Locate console.py and run it interactivery as
`./console`
- Alternatively run the console non-interactively as:
`echo "<command>" | ./console.py`

## File Descriptions
The console contains the entry point of the command interpreter. It supports the following commands.
- `EOF` - End of file character to exit the console
- `quit` - exits the console
- `<emptyline>` - overwrites default empty line method.
- `create` - Creates a new instance of the `BaseModel` and saves the change in a JSON file.
- `destroy` - Deletes instance of a class and saves the change in a JSON file.
- `show` - prints string representation of an instance.
- `all` - prints a string representation of all instances based on or not on the class name.
- `update` - updates an instance on the class and saves the change to a JSON file.

### `models/` directory containing classes used in this project
[base.model.py]() - Model from which future classes are abstracted.
Fields:
- `def __init__(self, *args, **kwargs)` - initializes the base model
- `def __str__(self)` - string representation of the BaseModel class
- `def save(self)` - updates attribute updated_at which is the current date and time
- `def to_dict(self)` - returns a dictionary of the attributes and values of an instance

#### `BaseModel` Classes
- city.py
- place.py
- state.py
- review.py
- amenity.py
- user.py

### `models/engine` Has the file storage class that handles JSON serialization and deserialization
[file_storage.py]() - the serializer and deserializer
- def all(self) - returns a dict of objects
- `def new(self, obj)` - sets in a new obj wity key and id
- `def save(self)` - serializes objects to JSON file
- `def reload(self)` - deserializes JSON files to objects