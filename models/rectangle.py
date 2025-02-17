"""The module for the rectangle class that will inherit from"""
from models.base import Base


class Rectangle(Base):
    """The model that is inheriting from the Base model in order to define a rectangle
    
    Attribute:

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """The function to instantiate the Rectangle object that will be passed
        
        Attr:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
            x(int): The horizontal coordinate of the rectangle in space
            y(int): The vertical coordinate of the rectangle in space
            id(int): The identifier of a particulat Rectangle object created
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The public getter for the width that retrieves the width of the rectangle
        
        returns:
            the width of the rectangle
        """
        return self.__width
    
    @width.setter
    def width(self, width):
        """The public setter for the width that retrieves the width of the rectangle
        
        
        Args:
            width(int): The width of the rectangle as an attribute passes into the class object during creation
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """The public getter for the height that retrieves the height of the rectangle
        
        returns:
            the height of the rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, height):
        """The public setter for the height that retrieves the height of the rectangle
        
        
        Args:
            height(int): The height of the rectangle as an attribute passes into the class object during creation
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """The public getter for the x that retrieves the x of the rectangle
        
        returns:
            the x of the rectangle
        """
        return self.__x
    
    @x.setter
    def x(self, x):
        """The public setter for the x that retrieves the x of the rectangle
        
        
        Args:
            x(int): The x of the rectangle as an attribute passes into the class object during creation
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """The public getter for the y that retrieves the y of the rectangle
        
        returns:
            the y of the rectangle
        """
        return self.__y
    
    @y.setter
    def y(self, y):
        """The public setter for the y that retrieves the y of the rectangle
        
        
        Args:
            y(int): The y of the rectangle as an attribute passes into the class object during creation
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """The method that gets the area of the rectangle of width and height"""
        
        return self.height*self.width
    
    

    def display(self):
        """A method that displays the shape of the rectangle
        
        returns: The print of the rectangle
        """
        shape = ['{}'.format('#'*self.width) for i in range(self.height)]

        return shape



