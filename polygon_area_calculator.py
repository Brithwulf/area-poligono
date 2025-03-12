class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        if self.__class__ == Rectangle:
            string = f'{self.__class__.__name__}(width={self.width}, height={self.height})'
        elif self.__class__ == Square:
            string = f'{self.__class__.__name__}(side={self.side})'
        return string
    def set_width(self, new_width):
        self.width = new_width
        if isinstance(self, Square):
            self.side = new_width

    def set_height(self, new_height):
        self.height = new_height
        if isinstance(self, Square):
            self.side = new_height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        for _ in range(self.height):
            picture += '*'*self.width + '\n'
        return picture
    
    def get_amount_inside(self, another_shape):
        quantity = self.get_area()//another_shape.get_area()
        return quantity


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
        self.height = self.width = self.side

    def set_side(self, new_side):
        self.height = self.width = self.side = new_side