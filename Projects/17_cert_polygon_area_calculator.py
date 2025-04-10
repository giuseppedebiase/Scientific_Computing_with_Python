class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height*self.width

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ['*' * self.width for i in range(self.height)]
        # + '\n' is required
        picture = '\n'.join(picture) + '\n'
        return picture

    def get_amount_inside(self, other):
        fit_width = self.width // other.width
        fit_height = self.height // other.height
        return fit_width * fit_height

class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width = width, height = width)

    def __repr__(self):
        return f'{self.__class__.__name__}(side={vars(self)["width"]})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side


rectangle = Rectangle(3, 3)
print(rectangle.width)
rectangle.set_width(40)
print(rectangle.get_picture())
square = Square(2)
square.set_side(6)
print(square.__repr__)