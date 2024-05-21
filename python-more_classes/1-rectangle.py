#!/usr/bin/python3
class Rectangle:
    """Defines a rectangle with a width and height.

    Attributes:
        __width (int): width of the rectangle, private.
        __height (int): height of the rectangle, private.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a Rectangle instance with optional width and height.
        width(self):
            Retrieves the width of the rectangle.
        width(self, value):
            Sets the width of the rectangle.
        height(self):
            Retrieves the height of the rectangle.
        height(self, value):
            Sets the height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with optional width and height.

        Args:
            width (int): The width of the rectangle, defaults to 0.
            height (int): The height of the rectangle, defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Retrieves the height of the rectangle

        Returns:
            int: the height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle

        Args:
            value: height of the rectangle

        Raises:
            TypeError: if value is not an int
            ValueError: if value is >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Retrieves the width of the rectangle.

        Returns
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value: the width of the rectangle.

        Raises:
            TypeError: if value is not an int
            ValueError: if value is >= 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
