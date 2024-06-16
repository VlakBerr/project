from table.cell import Cell

class Row:
    def __init__(self, cells:list, gap):
        self._cells = cells
        self._gap = gap
    def draw(self, x, y, surface):
        current_x = x
        for cell in self._cells:
            cell.draw(current_x, y, surface)
            current_x += self._gap + cell.size()

        

    def height(self):
        return self._cells[1].size()