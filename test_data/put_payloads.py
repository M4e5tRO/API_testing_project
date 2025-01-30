from faker import Faker


fake = Faker()


class PutPayloads:

    valid_object = {
        "id": "",
        "text": "UPD: " + fake.text(),
        "url": "upd_" + fake.url(),
        "tags": ["UPD", fake.state_abbr()],
        "info": {
            "description": "UPD: " + fake.text(),
            "policy": "UPD_NDA"
        }
    }

    send_like_patch_method = {
        "id": "",
        "text": "UPD: " + fake.text()
    }

    object_no_text = {
        "id": "",
        "url": "upd_" + fake.url(),
        "tags": ["UPD", fake.state_abbr()],
        "info": {
            "description": "UPD: " + fake.text(),
            "policy": "UPD_NDA"
        }
    }

    object_no_url = {
        "id": "",
        "text": "UPD: " + fake.text(),
        "tags": ["UPD", fake.state_abbr()],
        "info": {
            "description": "UPD: " + fake.text(),
            "policy": "UPD_NDA"
        }
    }

    object_no_tags = {
        "id": "",
        "text": "UPD: " + fake.text(),
        "url": "upd_" + fake.url(),
        "info": {
            "description": "UPD: " + fake.text(),
            "policy": "UPD_NDA"
        }
    }

    object_no_info = {
        "id": "",
        "text": "UPD: " + fake.text(),
        "url": "upd_" + fake.url(),
        "tags": ["UPD", fake.state_abbr()],
    }

    invalid_type_text_is_object = {
        "id": "",
        "text": {"key": "value"},
        "url": "upd_" + fake.url(),
        "tags": ["UPD", fake.state_abbr()],
        "info": {
            "description": "UPD: " + fake.text(),
            "policy": "UPD_NDA"
        }
    }

    invalid_type_url_is_array = {
        "id": "",
        "text": "UPD: " + fake.text(),
        "url": ["upd_" + fake.url(), 2, 3],
        "tags": ["UPD", fake.state_abbr()],
        "info": {
            "description": "UPD: " + fake.text(),
            "policy": "UPD_NDA"
        }
    }

    invalid_type_tags_is_none = {
        "id": "",
        "text": "UPD: " + fake.text(),
        "url": "upd_" + fake.url(),
        "tags": None,
        "info": {
            "description": "UPD: " + fake.text(),
            "policy": "UPD_NDA"
        }
    }

    invalid_type_info_is_string = {
        "id": "",
        "text": "UPD: " + fake.text(),
        "url": "upd_" + fake.url(),
        "tags": ["UPD", fake.state_abbr()],
        "info": fake.word()
    }
