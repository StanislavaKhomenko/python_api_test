from models import schemas
from models.pathes import URL
from models import project_models
from models.api import PetOperations
from models.body_content import status_options


class TestPetOperations:
    def test_pet_create(self):
        body = project_models.AddPet.pet_random(None)
        response = PetOperations(url=URL, pet_id=None).add_pet(body=body, schema=schemas.valid_create_pet_schema)
        assert response.status == 200
        return response.response

    def test_get_pet(self):
        response_body = TestPetOperations.test_pet_create(self)
        pet_id = response_body["id"]
        response = PetOperations(url=URL, pet_id=pet_id).get_pet(schema=schemas.valid_create_pet_schema)
        assert response.status == 200
        assert response.response["name"] == response_body["name"]

    def test_update_pet(self):
        response_body = TestPetOperations.test_pet_create(self)
        pet_id = response_body["id"]
        body = project_models.AddPet.pet_random(pet_id)
        response = PetOperations(url=URL, pet_id=pet_id).update_pet(body=body, schema=schemas.valid_create_pet_schema)
        assert response.status == 200
        return pet_id, body

    def test_get_updated_pet(self):
        pet_id, body = TestPetOperations.test_update_pet(self)
        response = PetOperations(url=URL, pet_id=pet_id).get_pet(schema=schemas.valid_create_pet_schema)
        assert response.status == 200
        assert body["name"] == response.response["name"]

    def test_get_pets_by_status(self):
        body = status_options[0:1]
        response = PetOperations(url=URL, pet_id=None).get_pets_by_status(body=body,
                                                                          schema=schemas.valid_create_pet_schema)
        assert response.status == 200

    def test_update_pet_with_form_data(self):
        response_body = TestPetOperations.test_pet_create(self)
        pet_id = response_body["id"]
        body = project_models.AddPet.update_pet_random(pet_id=pet_id)
        response = PetOperations(url=URL, pet_id=pet_id).update_pet_with_form_data(body=body, schema=schemas.valid_schema)
        assert response.status == 200
        return pet_id, body

    def test_get_pet_updated_with_form_data(self):
        pet_id, body = TestPetOperations.test_update_pet_with_form_data(self)
        response = PetOperations(url=URL, pet_id=pet_id).get_pet(schema=schemas.valid_create_pet_schema)
        assert response.status == 200
        assert body["name"] == response.response["name"]

    def test_upload_image(self):
        response_body = TestPetOperations.test_pet_create(self)
        pet_id = response_body["id"]
        image = open("/Users/stanisavva/Desktop/2023-01-30 13.30.56.jpg", "rb")
        body = {"additionalMetadata": "Cat with a bottle", "file": image}
        response = PetOperations(url=URL, pet_id=pet_id).upload_image(body=body, schema=schemas.valid_schema)
        assert response.status == 200
