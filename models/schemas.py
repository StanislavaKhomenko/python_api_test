valid_schema = {
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"]
}

valid_get_user_schema = {
    "properties": {
        "username": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"},
        "phone": {"type": "string"}
    },
    "required": ["id", "userStatus"]
}

valid_create_pet_schema = {
    "properties": {
        "category": {"name": "string"},
        "name": {"type": "string"},
        "photoUrls": {"type": "array"},
        "tags": {"type": "array"},
        "status": {"type": "string"}
    },
    "required": ["id"]
}
