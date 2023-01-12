from models.api import Register, GetUser, LoginUser, UpdateUser
from models import schemas
from models import project_models

URL = "https://petstore.swagger.io/v2"


class TestUserOperations:
    def test_user_registration(self):
        body = project_models.RegisterUser.user_random()
        response = Register(url=URL).register_user(body=body, schema=schemas.valid_schema)
        assert response.status == 200
        return body

    def test_get_user(self):
        registration_body = TestUserOperations.test_user_registration(self)
        username = registration_body["username"]
        response = GetUser(url=URL, username=username).get_user(schema=schemas.valid_get_user_schema)
        assert response.status == 200
        assert response.response["phone"] == registration_body["phone"]

    def test_login_user(self):
        registration_body = TestUserOperations.test_user_registration(self)
        username = registration_body["username"]
        password = registration_body["password"]
        body = {"username": username, "password": password}
        response = LoginUser(url=URL).login_user(body=body, schema=schemas.valid_schema)
        assert response.status == 200

    def test_update_user(self):
        registration_body = TestUserOperations.test_user_registration(self)
        username = registration_body["username"]
        password = registration_body["password"]
        body = {"username": username, "password": password}
        LoginUser(url=URL).login_user(body=body, schema=schemas.valid_schema)
        new_body = project_models.RegisterUser.user_random()
        response = UpdateUser(url=URL, username=username).update_user(body=new_body, schema=schemas.valid_schema)
        assert response.status == 200
        return new_body

    def test_get_updated_user(self):
        new_body = TestUserOperations.test_update_user(self)
        username = new_body["username"]
        response = GetUser(url=URL, username=username).get_user(schema=schemas.valid_get_user_schema)
        assert response.status == 200
