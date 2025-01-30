

class Headers:

    def_headers = {
        "Content-Type": "application/json"
    }

    auth_headers = {
        "Content-Type": "application/json",
        "Authorization": ""
    }

    invalid_token = {
        "Content-Type": "application/json",
        "Authorization": "invalid_token"
    }
