class Base:
    """
    This is the Base class.
    """
    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Parameters:
        id (int): The id of the Base object. Defaults to None.
        """
        self.id = id

class Rectangle(Base):
    """
    This is the Rectangle class that inherits from the Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Parameters:
        width (int): The width of the Rectangle object.
        height (int): The height of the Rectangle object.
        x (int): The x-coordinate of the Rectangle object. Defaults to 0.
        y (int): The y-coordinate of the Rectangle object. Defaults to 0.
        id (int): The id of the Rectangle object. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for the width attribute.
        
        Returns:
        int: The width of the Rectangle object.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Parameters:
        value (int): The new width of the Rectangle object.
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        
        Returns:
        int: The height of the Rectangle object.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Parameters:
        value (int): The new height of the Rectangle object.
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.
        
        Returns:
        int: The x-coordinate of the Rectangle object.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Parameters:
        value (int): The new x-coordinate of the Rectangle object.
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.
        
        Returns:
        int: The y-coordinate of the Rectangle object.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Parameters:
        value (int): The new y-coordinate of the Rectangle object.
        """
        self.__y = value

