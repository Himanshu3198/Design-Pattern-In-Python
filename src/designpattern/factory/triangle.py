from abc import  ABC

from src.designpattern.factory.shape import Shape


class Triangle(Shape):
      def draw(self):
          print("this is a triangle")