#!/usr/bin/env python
"""Python module that serve as a blueprint for other models"""
import json

class Base:
    """The basic model for every other model
    
    Attr:
        __nb_objects(int): COunts the number of Objects that is created
    """
    __nb_objects = 0

    def __init__(self, id = None):
        """Instantiating the attributes of the object created out of the Base class
        
        Args:
            id(int): The id of the object as it's created
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A method that returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries == []:
            return '[]'
        else:
            json_string = json.dumps(list_dictionaries)

        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A method that saves list object to a file

        Args:
            list_objs(list): The list of objects of a particular class cls.__name__ that are to be saved into a json file
        """
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w', encoding='utf_8') as the_file:
            if not list_objs:
                my_file = []
            else:
                my_file = [obj.to_dictionary() for obj in list_objs]
            the_file.write(cls.to_json_string(my_file))


    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by the JSON string.
    
        Args:
            json_string (str): A JSON string representation of a list of dictionaries.

        Returns:
            list: The Python list obtained from the JSON string. If json_string is None or empty, returns an empty list.
        """
        if not json_string or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)



