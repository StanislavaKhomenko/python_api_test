import random
from faker import Faker
from . import body_content

fake = Faker()


class RegisterUser:
    @staticmethod
    def user_random():
        username = fake.name()
        firstname = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()
        password = fake.password()
        phone = fake.phone_number()
        return {"username": username, "firstName": firstname, "lastName": lastname, "email": email,
                "password": password, "phone": phone}


class AddPet:
    @staticmethod
    def pet_random():
        category = random.choice(body_content.category_options)
        name = fake.first_name()
        tag = random.choice(body_content.tag_options)
        status = random.choice(body_content.status_options)
        photo = random.choice(body_content.photo_options)
        return {"category": {"name": category}, "name": name, "photoUrls": [photo], "tags": [{"name": tag}],
                "status": status}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
