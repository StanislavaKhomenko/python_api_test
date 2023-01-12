import logging
from jsonschema import validate
from .project_requests import Client
from .project_models import ResponseModel

logger = logging.getLogger("api")


class Register:
    def __init__(self, url):
        self.url = url
        self.client = Client

    REGISTER_USER = "/user"

    def register_user(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.REGISTER_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class GetUser:
    def __init__(self, url, username):
        self.url = url
        self.client = Client
        self.username = username

    GET_USER = "/user/"

    def get_user(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.GET_USER}{self.username}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class LoginUser:
    def __init__(self, url):
        self.url = url
        self.client = Client

    LOGIN_USER = "/user/login"

    def login_user(self, body: dict, schema: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.LOGIN_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class UpdateUser:
    def __init__(self, url, username):
        self.url = url
        self.client = Client
        self.username = username

    UPDATE_USER = "/user/"

    def update_user(self, body: dict, schema: dict):
        response = self.client.custom_request("PUT", f"{self.url}{self.UPDATE_USER}{self.username}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())
