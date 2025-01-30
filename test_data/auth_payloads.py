from faker import Faker


fake = Faker()

class AuthPayloads:

    valid_credentials = {"name": fake.name()}
    invalid_credentials = {"name": fake.random_number(fix_len=False)}
    invalid_id = f'{fake.text()}'
    invalid_token = f'{fake.text()}'

    auth_valid_name_string = {"name": "MikeDFG!@#$%^&*()_+{}:\"<>?1234567890"}

    auth_invalid_name_empty = {"name": ""}
    auth_no_name_key = {"TEXT": "TEXT"}
    auth_invalid_name_integer = {"name": 1234567890}
    auth_invalid_name_float = {"name": 123.456}
    auth_invalid_name_boolean = {"name": True}
    auth_invalid_name_none = {"name": None}
    auth_invalid_name_empty_array = {"name": []}
    auth_invalid_name_array = {"name": [1, 'test', False]}
    auth_invalid_name_empty_object = {"name": {}}
    auth_invalid_name_object = {"name": {'name': 'MikeDFG'}}

    auth_message = f"Token is alive. Username is {valid_credentials['name']}"

    title_404_auth = '<title>404 Not Found</title>'
    header_404_auth = '<h1>Not Found</h1>'
    message_404_auth = '<p>Token not found</p>'
