from models import schemas
from models.pathes import URL
from models import project_models
from models.api import UserOperations


class TestUserOperations:
    def test_user_registration(self):
        body = project_models.RegisterUser.user_random()
        response = UserOperations(url=URL, username=None).register_user(body=body, schema=schemas.valid_schema)
        assert response.status == 200
        return body

    def test_users_registration_with_array(self):
        body = []

        for i in range(3):
            i = project_models.RegisterUser.user_random()
            body.append(i)

        response = UserOperations(url=URL, username=None).register_users_with_array(body=body,
                                                                                    schema=schemas.valid_schema)
        assert response.status == 200
        return body

    def test_get_user(self):
        registration_body = TestUserOperations.test_user_registration(self)
        username = registration_body["username"]
        response = UserOperations(url=URL, username=username).get_user(schema=schemas.valid_get_user_schema)
        assert response.status == 200
        assert response.response["phone"] == registration_body["phone"]

    def test_get_user_created_with_array(self):
        registration_bodies = TestUserOperations.test_users_registration_with_array(self)
        username = registration_bodies[1]["username"]
        response = UserOperations(url=URL, username=username).get_user(schema=schemas.valid_get_user_schema)
        assert response.status == 200
        assert response.response["phone"] == registration_bodies[1]["phone"]

    def test_login_user(self):
        registration_body = TestUserOperations.test_user_registration(self)
        username = registration_body["username"]
        password = registration_body["password"]
        body = {"username": username, "password": password}
        response = UserOperations(url=URL, username=None).login_user(body=body, schema=schemas.valid_schema)
        assert response.status == 200
        return registration_body

    def test_logout_user(self):
        TestUserOperations.test_login_user(self)
        response = UserOperations(url=URL, username=None).logout_user(schema=schemas.valid_schema)
        assert response.status == 200

    def test_update_user(self):
        registration_body = TestUserOperations.test_user_registration(self)
        username = registration_body["username"]
        password = registration_body["password"]
        body = {"username": username, "password": password}
        UserOperations(url=URL, username=None).login_user(body=body, schema=schemas.valid_schema)
        new_body = project_models.RegisterUser.user_random()
        response = UserOperations(url=URL, username=username).update_user(body=new_body, schema=schemas.valid_schema)
        assert response.status == 200
        return new_body

    def test_get_updated_user(self):
        new_body = TestUserOperations.test_update_user(self)
        username = new_body["username"]
        response = UserOperations(url=URL, username=username).get_user(schema=schemas.valid_get_user_schema)
        assert response.status == 200

    def test_delete_user(self):
        registration_body = TestUserOperations.test_user_registration(self)
        username = registration_body["username"]
        response = UserOperations(url=URL, username=username).delete_user(schema=schemas.valid_schema)
        assert response.status == 200
        return username

    def test_get_deleted_user(self):
        username = TestUserOperations.test_delete_user(self)
        response = UserOperations(url=URL, username=username).get_user(schema=schemas.valid_schema)
        assert response.status == 404
