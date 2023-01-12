from faker import Faker

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


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
