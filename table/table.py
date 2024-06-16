import pygame as pg
from table.row import Row

class Table:
    def __init__(self, rows, gap):
        self._rows = rows
        self._gap = gap
    def draw(self, x, y, surface):
        current_y = y
        for row in self._rows:
            row.draw(x, current_y, surface)
            current_y += self._gap + row.height()