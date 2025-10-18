from abc import ABC

from src.designpattern.factory.shape import Shape


class Circle(Shape):

    def draw(self):
        print("this is a circle")
