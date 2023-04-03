#!/usr/bin/python3

class Rectangle:
    """This class defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor method that initialize the width and height of rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns string representation of rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") * self.height).rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor method that prints a message when instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter method for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of rectangle"""

        return (self.width + self.height) * 2 if (self.width and self.height) != 0 else 0
