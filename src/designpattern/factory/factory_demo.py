from src.designpattern.factory.shape_factory import ShapeFactory


shape1 = ShapeFactory().get_shape("circle")
shape2 = ShapeFactory().get_shape("triangle")
shape3 = ShapeFactory().get_shape("rectangle")


shape1.draw()
shape2.draw()
shape3.draw()