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
            for col in ci