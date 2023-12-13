import sqlite3

class ProductManager:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            price REAL
        )
        '''
        self.execute_query(query)

    def execute_query(self, query, parameters=None):
        with self.conn:
            cursor = self.conn.cursor()
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            return cursor

    def insert_product(self, product_name, price):
        query = 'INSERT INTO products (product_name, price) VALUES (?, ?)'
        parameters = (product_name, price)
        self.execute_query(query, parameters)
        print(f"Product '{product_name}' inserted successfully.")

    def update_product(self, product_id, new_name, new_price):
        query = 'UPDATE products SET product_name = ?, price = ? WHERE product_id = ?'
        parameters = (new_name, new_price, product_id)
        self.execute_query(query, parameters)
        print(f"Product with ID {product_id} updated successfully.")

    def delete_product(self, product_id):
        query = 'DELETE FROM products WHERE product_id = ?'
        parameters = (product_id,)
        self.execute_query(query, parameters)
        print(f"Product with ID {product_id} deleted successfully.")

    def select_all_products(self):
        query = 'SELECT * FROM products'
        cursor = self.execute_query(query)
        products = cursor.fetchall()
        return products

    def close_connection(self):
        self.conn.close()

# 샘플 데이터 10개 추가
if __name__ == "__main__":
    product_manager = ProductManager()

    # 데이터 삽입
    for i in range(1, 11):
        product_manager.insert_product(f'Product{i}', 10.0 * i)

    # 모든 제품 조회
    all_products = product_manager.select_all_products()
    print("\nAll Products:")
    for product in all_products:
        print(product)

    # 제품 업데이트
    product_manager.update_product(1, 'UpdatedProduct1', 99.99)

    # 모든 제품 재조회
    all_products = product_manager.select_all_products()
    print("\nAll Products after update:")
    for product in all_products:
        print(product)

    # 제품 삭제
    product_manager.delete_product(2)

    # 모든 제품 최종 조회
    all_products = product_manager.select_all_products()
    print("\nAll Products after deletion:")
    for product in all_products:
        print(product)

    # 데이터베이스 연결 종료
    product_manager.close_connection()
