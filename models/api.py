import logging
from . import pathes
from jsonschema import validate
from .project_requests import Client
from .project_models import ResponseModel

logger = logging.getLogger("api")


class UserOperations:
    def __init__(self, url, username):
        self.url = url
        self.client = Client
        self.username = username
        self.path = pathes

    def register_user(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.path.USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def register_users_with_array(self, body: list, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.path.REGISTER_USERS}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_user(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.path.USER_USERNAME}{self.username}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def login_user(self, body: dict, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.path.LOGIN_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def logout_user(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.path.LOGOUT_USER}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def update_user(self, body: dict, schema: dict):
        response = self.client.custom_request("PUT", f"{self.url}{self.path.USER_USERNAME}{self.username}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def delete_user(self, schema: dict):
        response = self.client.custom_request("DELETE", f"{self.url}{self.path.USER_USERNAME}{self.username}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class PetOperations:
    def __init__(self, url, pet_id):
        self.url = url
        self.pet_id = pet_id
        self.client = Client
        self.path = pathes

    def add_pet(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.path.PET}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_pet(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.path.ID_PET}{self.pet_id}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def update_pet(self, body: dict, schema: dict):
        response = self.client.custom_request("PUT", f"{self.url}{self.path.PET}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_pets_by_status(self, body: list, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.path.FIND_PET_BY_STATUS}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def update_pet_with_form_data(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.path.ID_PET}{self.pet_id}", json=body,
                                              headers={"Content-Type": "application/x-www-form-urlencoded"})
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def upload_image(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.path.ID_PET}{self.pet_id}{self.path.UPLOAD_IMAGE}",
                                              files=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class StoreOperations:
    def __init__(self, url, order_id):
        self.url = url
        self.order_id = order_id
        self.client = Client
        self.path = pathes

    def create_order(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.path.ORDER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_order(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.path.ORDER_ID}{self.order_id}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def delete_order(self, schema: dict):
        response = self.client.custom_request("DELETE", f"{self.url}{self.path.ORDER_ID}{self.order_id}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_inventories(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.path.INVENTORY}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())
