from models import schemas
from models.pathes import URL
from models import project_models
from models.api import PetOperations


class TestPetOperations:
    def test_pet_create(self):
        body = project_models.AddPet.pet_random()
        response = PetOperations(url=URL, pet_id=None).add_pet(body=body, schema=schemas.valid_create_pet_schema)
        assert response.status == 200
        return body
