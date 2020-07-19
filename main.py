# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(5, 10)



sq = shape_calculator.Square(9)
sq.set_side(2)
print(sq.get_picture())
