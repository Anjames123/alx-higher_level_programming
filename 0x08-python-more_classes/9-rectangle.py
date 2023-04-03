#!/usr/bin/python3

class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes the area of the rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of the rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        else:
            symbol = str(Rectangle.print_symbol)
            rectangle = ""
            for i in range(self.height):
                rectangle += (symbol * self.width) + "\n"
            return rectangle[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle that can be used to recreate a new instance"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes a rectangle"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""

        return cls(size, size)
