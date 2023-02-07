import random
from faker import Faker
from . import body_content
from datetime import datetime, timezone

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
    def pet_random(pet_id):
        category = random.choice(body_content.category_options)
        name = fake.first_name()
        tag = random.choice(body_content.tag_options)
        status = random.choice(body_content.status_options)
        photo = random.choice(body_content.photo_options)
        return {"id": pet_id, "category": {"name": category}, "name": name, "photoUrls": [photo], "tags": [{"name": tag}],
                "status": status}

    @staticmethod
    def update_pet_random(pet_id):
        name = fake.first_name()
        status = random.choice(body_content.status_options)
        return {"id": pet_id, "name": name, "status": status}


class PlaceOrder:
    @staticmethod
    def place_order(pet_id):
        quantity = 1
        ship_date = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
        status = "placed"
        complete = True
        return {"petId": pet_id, "quantity": quantity, "shipDate": ship_date, "status": status, "complete": complete}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
