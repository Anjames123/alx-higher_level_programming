#!/usr/bin/python3

class Rectangle:
    """
    A class that defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            A string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.height):
                rect += "#" * self.width
                if i != self.height - 1:
                    rect += "\n"
            return rect
