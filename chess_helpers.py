import numpy as np

class piece():
    def __init__(self, name, val, color) -> None:
        self.name = name
        self.value = val
	self.color = color
    def moves(self, board) -> list:
        valid_moves = []
