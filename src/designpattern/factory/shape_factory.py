from src.designpattern.factory.circle import Circle
from src.designpattern.factory.shape import Shape
from src.designpattern.factory.triangle import Triangle


class ShapeFactory:

    def get_shape(self,shape_type: str)->Shape:

        if shape_type == "circle":
            return Circle()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError(f"Invalid Shape: {shape_type}")
