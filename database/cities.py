from database.database import Database


class Products:

    @staticmethod
    def get_by_id(products_id: int):
        stmt = "SELECT * FROM products WHERE id=%s;"
        Database.cursor().execute(stmt, [products_id])
        return Database.cursor().fetchone()

    @staticmethod
    def get_all():
        stmt = "SELECT * FROM products"
        Database.cursor().execute(stmt, [])
        return Database.cursor().fetchall()

    @staticmethod
    def get_by_manufacture(manufacture: str):
        stmt = "SELECT * FROM products WHERE manufacture=%s;"
        Database.cursor().execute(stmt, [manufacture])
        return Database.cursor().fetchall()

