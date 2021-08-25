class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):

        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        line = '*' * self.width + '\n'
        shape = ''

        for _ in range(self.height):
            shape += line
        return shape
    
    def get_amount_inside(self, other):

        if other.width > self.width or other.height > self.height:
            return 0

        fit_x = int(max(other.width, self.width)/min(other.width,self.width))
        fit_y = int(max(other.height, self.height)/min(other.height,self.height))

        return fit_x * fit_y

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):

    def __init__(self,side):
        self.set_side(side)
    
    def set_side(self, side):
        self.width = side
        self.side = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def picture(self):
        return self.get_picture()
        
    def __str__(self):
        return f'Square(side={self.side})'