from faker import Faker


fake = Faker()


class PostPayloads:

    valid_object = {
        "text": fake.text(),
        "url": fake.url(),
        "tags": [fake.state_abbr(), fake.state_abbr()],
        "info": {
            "description": fake.text(),
            "policy": "NDA"
        }
    }

    invalid_object_no_text = {
        "url": fake.url(),
        "tags": [fake.state_abbr(), fake.state_abbr()],
        "info": {
            "description": fake.text(),
            "policy": "NDA"
        }
    }

    invalid_object_no_url = {
        "text": fake.text(),
        "tags": [fake.state_abbr(), fake.state_abbr()],
        "info": {
            "description": fake.text(),
            "policy": "NDA"
        }
    }

    invalid_object_no_tags = {
        "text": fake.text(),
        "url": fake.url(),
        "info": {
            "description": fake.text(),
            "policy": "NDA"
        }
    }

    invalid_object_no_info = {
        "text": fake.text(),
        "url": fake.url(),
        "tags": [fake.state_abbr(), fake.state_abbr()]
    }

    invalid_object_text_is_number = {
        "text": fake.random_int(1, 999),
        "url": fake.url(),
        "tags": [fake.state_abbr(), fake.state_abbr()],
        "info": {
            "description": fake.text(),
            "policy": "NDA"
        }
    }

    invalid_object_url_is_boolean = {
        "text": fake.text(),
        "url": fake.boolean(),
        "tags": [fake.state_abbr(), fake.state_abbr()],
        "info": {
            "description": fake.text(),
            "policy": "NDA"
        }
    }

    invalid_object_tags_is_object = {
        "text": fake.text(),
        "url": fake.url(),
        "tags": {
            fake.state_abbr(): fake.word(),
            fake.state_abbr(): fake.word()
        },
        "info": {
            "description": fake.text(),
            "policy": "NDA"
        }
    }

    invalid_object_info_is_array = {
        "text": fake.text(),
        "url": fake.url(),
        "tags": [fake.state_abbr(), fake.state_abbr()],
        "info": ["description", fake.text(), "policy", "NDA"]
    }
