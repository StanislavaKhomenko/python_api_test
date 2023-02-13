import random
from models import schemas
from models.pathes import URL
from models import project_models
from models.api import PetOperations
from models.api import StoreOperations


class TestStoreOperations:
    def test_place_order(self):
        pet_body = project_models.AddPet.pet_random(None)
        response = PetOperations(url=URL, pet_id=None).add_pet(body=pet_body, schema=schemas.valid_create_pet_schema)
        pet_id = response.response["id"]
        body = project_models.PlaceOrder.place_order(pet_id)
        response = StoreOperations(url=URL, order_id=None).create_order(body=body, schema=schemas.valid_order_schema)
        assert response.status == 200
        return response.response

    # We use order ID in range from 1 to 10 because of API requirements. Order IDs besides this range will raise
    # exceptions. Learn more at https://petstore.swagger.io/#/store/getOrderById
    def test_get_order(self):
        i = random.randint(1, 10)
        response = StoreOperations(url=URL, order_id=i).get_order(schema=schemas.valid_order_schema)
        assert response.status == 200

    # This endpoint allows using real order IDs without raising exceptions
    def test_delete_order(self):
        response_body = TestStoreOperations.test_place_order(self)
        order_id = response_body["id"]
        response = StoreOperations(url=URL, order_id=order_id).delete_order(schema=schemas.valid_schema)
        assert response.status == 200

    def test_get_deleted_order(self):
        response_body = TestStoreOperations.test_place_order(self)
        order_id = response_body["id"]
        response = StoreOperations(url=URL, order_id=order_id).delete_order(schema=schemas.valid_schema)
        assert response.status == 200
        another_response = StoreOperations(url=URL, order_id=order_id).delete_order(schema=schemas.valid_schema)
        assert another_response.status == 404

    def test_get_inventories(self):
        response = StoreOperations(url=URL, order_id=None).get_inventories(schema=schemas.valid_inventories_schema)
        assert response.status == 200
