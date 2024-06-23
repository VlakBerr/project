from database.cities import Products
from table.cell import Cell
from table.row import Row
from table.table import Table

class TableSeeder:
    def __init__(self):
        pass
    @staticmethod
    def generateTable(order_col:str, ascending = True):
        products = Products.get_all(order_col, ascending)
        rows = []
        names = []

        for name in Products.get_column_name():
            names.append(Cell(size=100,text= name, font_size=15))
        rows.append(Row(names, 15))


        for product in products:
            cells = []
            for col in product:
                cells.append(Cell(size=100,text= col, font_size=15))
            rows.append(Row(cells, 15))

        return Table(rows, 15)
    
