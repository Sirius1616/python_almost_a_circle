"""Python module that serve as a blueprint for other models"""


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
            self.__nb_objects += 1
            self.id = self.__nb_objects

    
