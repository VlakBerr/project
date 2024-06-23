from database.database import Database


class Products:

    @staticmethod
    def get_by_id(products_id: int):
        stmt = "SELECT * FROM products WHERE id=%s;"
        Database.cursor().execute(stmt, [products_id])
        return Database.cursor().fetchone()

    @staticmethod
    def get_all(order_col: str = "", order_ascending: bool = True):
        order = "ASC" if order_ascending is True else "DESC"
        stmt = f"SELECT * FROM products ORDER BY {order_col} {order}"
        Database.cursor().execute(stmt, [])
        return Database.cursor().fetchall()

    @staticmethod
    def get_by_manufacture(manufacture: str):
        stmt = "SELECT * FROM products WHERE manufacture=%s;"
        Database.cursor().execute(stmt, [manufacture])
        return Database.cursor().fetchall()

    @staticmethod
    def get_column_name():
        stmt = "SHOW COLUMNS FROM products;"
        Database.cursor().execute(stmt, [])
        names = []
        for row in Database.cursor().fetchall():
            names.append(row[0])
        return names