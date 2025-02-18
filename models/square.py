"""Module for the square class"""
import unittest
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from the rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of the attribute for the square class
        
        Args:
            size(int): size of the square
            x(int): horizontal coordinate of the square
            y(int): vertical coordinate of the square
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """The size getter method, for retrieving the value of the square"""

        return self.width
    

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError('square must be > 0')
        else:
            self.width = value
            self.height = value
        

    def __str__(self):
        """The string formated method for printing the square"""
        
        return '[Square] {} {}/{} - {}'.format(self.id, self.x, self.y, self.size)
    

    def update(self, *args, **kwargs):
        """The following method updates the rectangle with new values
        
        
        Args:
            args: Takes in variable number of arguments
        """
        if args:
            my_list = ['id', 'size', 'x', 'y']  # List all the attributes that might be entered as args

            attr_dict = {}  # Empty for dictionary attribute formation

            new_list = [i for i in args]

            for i in range(len(args)):
                attr_dict[my_list[i]] = new_list[i]

            for key, value in attr_dict.items():
                self.__setattr__(key, value)
        else:
            if kwargs:
                for key, value in kwargs.items():
                    self.__setattr__(key, value)


    def to_dictionary(self):
        """
        Gets the dictionary representation of the rectangle object

        Returns:
            a dictionary of attributes and values
        """
        return {
            'id' : self.id,
            'size' : self.width,
            'x' : self.x,
            'y' : self.y
        }
