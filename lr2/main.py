from app.circle import Circle
from app.rectangle import Rectangle
from app.square import Square
import numpy as np



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rectangle = Rectangle('blue', 8, 8)
    circle = Circle('green', 8)
    square = Square('red', 8)
    rectangle.repr()
    circle.repr()
    square.repr()
    v_hor_np = np.array([1, 2])
    print(v_hor_np)





