from locust import HttpUser, task, between
import random
import json

class ProductTestUser(HttpUser):
    wait_time = between(1, 2)  # Simulate users waiting between 1 and 2 seconds

    # @task(1)
    # def create_product(self):
    #     """Test POST /products (Create Product)"""
    #     product_data = {
    #         "name": f"Product {random.randint(1, 1000)}",
    #         "description": "A random product description",
    #         "price": 100000,
    #         "category": "KEYBOARDs"
    #     }
    #     self.client.post("/products", json=product_data)

    # @task(2)
    # def get_all_products(self):
    #     """Test GET /products (Read All Products)"""
    #     self.client.get("/products")

    # @task(2)
    # def get_single_product(self):
    #     """Test GET /products/:id (Read Single Product)"""
    #     product_id = random.randint(1, 1000)
    #     self.client.get(f"/products/{product_id}")

    @task(1)
    def update_product(self):
        """Test PUT /products/:id (Update Product)"""
        product_id = 1
        updated_data = {
            "name": f"Updated Product {product_id}",
            "description": "Updated description",
            "price": 150000,
            "category": "Updated Category"
        }
        self.client.put(f"/products/{product_id}", json=updated_data)

    # @task(1)
    # def delete_product(self):
    #     """Test DELETE /products/:id (Delete Product)"""
    #     product_id = random.randint(1, 1000)
    #     self.client.delete(f"/products/{product_id}")

    # @task(1)
    # def generate_products(self):
    #     """Test GET /products/generate (Generate 1000 Products)"""
    #     self.client.get("/products/generate")
    #
    # def on_start(self):
    #     """Called when a simulated user starts, generates initial products"""
    #     self.generate_products()


# To run this file, use the following command:
# locust -f locustfile.py --host=http://localhost:4001
