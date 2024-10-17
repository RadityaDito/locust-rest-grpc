from locust import User, task, between
import grpc
import product_pb2
import product_pb2_grpc
import time


class GrpcProductUser(User):
    wait_time = between(1, 2)

    def on_start(self):
        # Establish a connection to the gRPC server
        self.channel = grpc.insecure_channel('localhost:4000')
        self.stub = product_pb2_grpc.ProductStub(self.channel)

        # Store the product ID created for testing
        self.test_product_id = 1

    # @task
    # def create_product(self):
    #     # Record the start time
    #     start_time = time.time() * 1000  # Convert to milliseconds
    
    #     try:
    #         # Example product data to create
    #         new_product = product_pb2.ProductItem(
    #             name="LoadTest Product",
    #             description="Test Product Description",
    #             price=100.0,
    #             category=product_pb2.Category.KEYBOARDs
    #         )
    
    #         # Make the gRPC request
    #         response = self.stub.CreateProduct(new_product)
    #         self.test_product_id = response.id  # Store the product ID for future operations
    #         total_time = (time.time() * 1000) - start_time
    
    #         # Log success manually
    #         self.environment.events.request.fire(
    #             request_type="grpc",
    #             name="CreateProduct",
    #             response_time=total_time,
    #             response_length=len(response.name),
    #             exception=None
    #         )
    
    #     except grpc.RpcError as e:
    #         total_time = (time.time() * 1000) - start_time
    
    #         # Log failure manually
    #         self.environment.events.request.fire(
    #             request_type="grpc",
    #             name="CreateProduct",
    #             response_time=total_time,
    #             response_length=0,
    #             exception=e
    #         )

    # @task
    # def read_product(self):
    #     if not self.test_product_id:
    #         return
    #
    #     start_time = time.time() * 1000  # Convert to milliseconds
    #
    #     try:
    #         # Make the gRPC request to read the created product
    #         product_id = product_pb2.ProductId(id=self.test_product_id)
    #         response = self.stub.ReadProduct(product_id)
    #         total_time = (time.time() * 1000) - start_time
    #
    #         # Log success manually
    #         self.environment.events.request.fire(
    #             request_type="grpc",
    #             name="ReadProduct",
    #             response_time=total_time,
    #             response_length=len(response.name),
    #             exception=None
    #         )
    #
    #     except grpc.RpcError as e:
    #         total_time = (time.time() * 1000) - start_time
    #
    #         # Log failure manually
    #         self.environment.events.request.fire(
    #             request_type="grpc",
    #             name="ReadProduct",
    #             response_time=total_time,
    #             response_length=0,
    #             exception=e
    #         )

    # @task
    # def read_all_products(self):
    #     start_time = time.time() * 1000  # Convert to milliseconds

    #     try:
    #         # Make the gRPC request to read all products
    #         response = self.stub.ReadProducts(product_pb2.VoidParam())
    #         total_time = (time.time() * 1000) - start_time

    #         # Log success manually
    #         self.environment.events.request.fire(
    #             request_type="grpc",
    #             name="ReadProducts",
    #             response_time=total_time,
    #             response_length=len(response.products),
    #             exception=None
    #         )

    #     except grpc.RpcError as e:
    #         total_time = (time.time() * 1000) - start_time

    #         # Log failure manually
    #         self.environment.events.request.fire(
    #             request_type="grpc",
    #             name="ReadProducts",
    #             response_time=total_time,
    #             response_length=0,
    #             exception=e
    #         )

    @task
    def update_product(self):
        if not self.test_product_id:
            return
    
        start_time = time.time() * 1000  # Convert to milliseconds
    
        try:
            # Updated product data
            updated_product = product_pb2.ProductItem(
                id=self.test_product_id,
                name="Updated Product",
                description="Updated Description",
                price=150.0,
                category=product_pb2.Category.KEYBOARDs
            )
    
            # Make the gRPC request
            response = self.stub.UpdateProduct(updated_product)
            total_time = (time.time() * 1000) - start_time
    
            # Log success manually
            self.environment.events.request.fire(
                request_type="grpc",
                name="UpdateProduct",
                response_time=total_time,
                response_length=len(response.name),
                exception=None
            )
    
        except grpc.RpcError as e:
            total_time = (time.time() * 1000) - start_time
    
            # Log failure manually
            self.environment.events.request.fire(
                request_type="grpc",
                name="UpdateProduct",
                response_time=total_time,
                response_length=0,
                exception=e
            )

    # @task
    # def delete_product(self):
    #     if not self.test_product_id:
    #         return
    #
    #     start_time = time.time() * 1000  # Convert to milliseconds
    #
    #     try:
    #         # Make the gRPC request to delete the created product
    #         product_id = product_pb2.ProductId(id=self.test_product_id)
    #         response = self.stub.DeleteProduct(product_id)
    #         total_time = (time.time() * 1000) - start_time
    #
    #         # Log success manually
    #         self.environment.events.request.fire(
    #             request_type="grpc",
    #             name="DeleteProduct",
    #             response_time=total_time,
    #             response_length=0,
    #             exception=None
    #         )
    #
    #         # Reset the product ID after deletion
    #         self.test_product_id = None
    #
    #     except grpc.RpcError as e:
    #         total_time = (time.time() * 1000) - start_time
    #
    #         # Log failure manually
    #         self.environment.events.request.fire(
    #             request_type="grpc",
    #             name="DeleteProduct",
    #             response_time=total_time,
    #             response_length=0,
    #             exception=e
    #         )

    def on_stop(self):
        # Close the gRPC channel when the user stops
        self.channel.close()
