from database.cities import Products
from table.cell import Cell
from table.row import Row

class TableSeeder:
    def __init__(self) -> None:
        pass


    def generateTable(self):
        products = Products.get_all()
        rows = []

        for product in products:
            cells = []
            for col in products:
                cells.append(Cell(size=100, col, font_size=15))
            rows.append(Row(cells))

        return Table(rows)
        