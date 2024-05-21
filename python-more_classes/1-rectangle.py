#!/usr/bin/python3
class Rectangle:
    """Defines a rectangle with a width and height.

    Attributes:
        _width: width of the rectangle
        _height: height of the rectangle

    Methods:
    width(self): retrieves the width of the rectangle
    width(self, value): sets the width of the rectangle
    height(self): retrieves the height of the rectangle
    height(self, value): sets the height of the rectangle
    __str__(self): Returns a string representation of the rectangle.
    __repr__(self): Returns a string representation of the rectangle.

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle

        Args:
            value: height of the rectangle

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value: the width of the rectangle.

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value


    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] ({self.width})/{self.height}"

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return f"Rectangle(_width={self._width}, _height={self._height})"
