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
