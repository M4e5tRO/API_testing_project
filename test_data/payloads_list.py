# ------------------------------------------General--------------------------------------------------------------------
# =========================================VALID DATA==================================================================
valid_credentials = {"name": "valid_user"}
# =========================================INVALID DATA================================================================
invalid_credentials = {"name": 123}
invalid_id = 'invalid_id'

# ---------------------------------------Authorization-----------------------------------------------------------------
# =========================================VALID DATA==================================================================
auth_valid_name_string = {"name": "MikeDFG!@#$%^&*()_+{}:\"<>?1234567890"}
# =========================================INVALID DATA================================================================
auth_invalid_name_empty = {"name": ""}
auth_invalid_name_only_spaces = {"name": "          "}
auth_additional_key_value = {"name": "MikeDFG", "TEXT": "TEXT"}
auth_no_name_key = {"TEXT": "TEXT"}
auth_invalid_name_single_quotes = {"name": ''}
auth_invalid_name_integer = {"name": 1234567890}
auth_invalid_name_float = {"name": 123.456}
auth_invalid_name_boolean = {"name": True}
auth_invalid_name_none = {"name": None}
auth_invalid_name_empty_array = {"name": []}
auth_invalid_name_array = {"name": [1, 'test', False]}
auth_invalid_name_empty_object = {"name": {}}
auth_invalid_name_object = {"name": {'name': 'MikeDFG'}}

# -----------------------------------------POST------------------------------------------------------------------------
# =========================================VALID DATA==================================================================
post_valid_object = {"text": "test_text", "url": "test_url@text.com", "tags": ["TAG1", "TAG2"], "info": {"description":
                     "Test object", "policy": "NDA"}}
# =========================================INVALID DATA================================================================
post_invalid_object_no_text = {"url": "test_url@text.com", "tags": ["TAG1", "TAG2"], "info": {"description":
                               "Test object", "policy": "NDA"}}
post_invalid_object_no_url = {"text": "test_text", "tags": ["TAG1", "TAG2"], "info": {"description": "Test object",
                              "policy": "NDA"}}
post_invalid_object_no_tags = {"text": "test_text", "url": "test_url@text.com", "info": {"description": "Test object",
                               "policy": "NDA"}}
post_invalid_object_no_info = {"text": "test_text", "url": "test_url@text.com", "tags": ["TAG1", "TAG2"]}
post_add_any_key_value_pair = {"text": "test_text", "url": "test_url@text.com", "tags": ["TAG1", "TAG2"], "info":
                               {"description": "Test object", "policy": "NDA"}, "colour": "red"}
post_invalid_object_text_is_number = {"text": 987, "url": "test_url@text.com", "tags": ["TAG1", "TAG2"], "info":
                                      {"description": "Test object", "policy": "NDA"}}
post_invalid_object_url_is_boolean = {"text": "test_text", "url": False, "tags": ["TAG1", "TAG2"], "info":
                                      {"description": "Test object", "policy": "NDA"}}
post_invalid_object_tags_is_object = {"text": "test_text", "url": "test_url@text.com", "tags": {"TAG1": "value1",
                                      "TAG2": "value2"}, "info": {"description": "Test object", "policy": "NDA"}}
post_invalid_object_info_is_array = {"text": "test_text", "url": "test_url@text.com", "tags": ["TAG1", "TAG2"], "info":
                                     ["description", "Test object", "policy", "NDA"]}

# ------------------------------------------PUT------------------------------------------------------------------------
# =========================================VALID DATA==================================================================
put_valid_object = {"id": "", "text": "test_text_UPD", "url": "test_url_upd@text.com", "tags": ["TAG1", "TAG2", "UPD"],
                    "info": {"description": "Test object updated", "policy": "NDA UPD"}}
# =========================================INVALID DATA================================================================
put_send_like_path_method = {"id": "", "text": "test_text_UPD"}
put_object_no_text = {"id": "", "url": "test_url_upd@text.com", "tags": ["TAG1", "TAG2", "UPD"], "info": {"description":
                      "Test object updated", "policy": "NDA UPD"}}
put_object_no_url = {"id": "", "text": "test_text_UPD", "tags": ["TAG1", "TAG2", "UPD"], "info": {"description":
                     "Test object updated", "policy": "NDA UPD"}}
put_object_no_tags = {"id": "", "text": "test_text_UPD", "url": "test_url_upd@text.com", "info": {"description":
                      "Test object updated", "policy": "NDA UPD"}}
put_object_no_info = {"id": "", "text": "test_text_UPD", "url": "test_url_upd@text.com", "tags": ["TAG1", "TAG2",
                      "UPD"]}
put_add_any_key_value_pair = {"id": "", "country_upd": "Germany_UPD", "text": "test_text_UPD", "url":
                              "test_url_upd@text.com", "tags": ["TAG1", "TAG2", "UPD"], "info":
                              {"description": "Test object updated", "policy": "NDA UPD"}}
put_invalid_type_text_is_object = {"id": "", "text": {"key": "value"}, "url": "test_url_upd@text.com", "tags":
                                   ["TAG1", "TAG2", "UPD"], "info": {"description": "Test object updated", "policy":
                                   "NDA UPD"}}
put_invalid_type_url_is_array = {"id": "", "text": "test_text_UPD", "url": ["test_url_upd@text.com", 2, 3], "tags":
                                 ["TAG1", "TAG2", "UPD"], "info": {"description": "Test object updated", "policy":
                                 "NDA UPD"}}
put_invalid_type_tags_is_none = {"id": "", "text": "test_text_UPD", "url": "test_url_upd@text.com", "tags": None,
                                 "info": {"description": "Test object updated", "policy": "NDA UPD"}}
put_invalid_type_info_is_string = {"id": "", "text": "test_text_UPD", "url": "test_url_upd@text.com", "tags": ["TAG1",
                                   "TAG2", "UPD"], "info": "description"}
