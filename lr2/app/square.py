from app.rectangle import Rectangle

class Square(Rectangle):

    figure_type = "Square"

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, color, side):
        super().__init__(color, side, side)

    def side(self):
        return self._Rectangle__height
    
    def side(self, side):
        if side > 0:
            self.__height = side
            self.__width = side
        else:
            raise ValueError
    
    def repr(self):
        print('FigureType: {}, side: {}, color: {}, square: {}'.format(self.get_figure_type(), self._Rectangle__height, self.color.color, self.area()))
    