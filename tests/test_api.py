import pytest


AUTH_DATA = [{"name": "MikeDFG"}]

POST_DATA = [
    {"text": "test_text", "url": "test_url@text.com", "tags": ["TAG1", "TAG2"], "info": {"description": "Test object",
     "policy": "NDA"}}
]

PUT_DATA = [
    {"text": "test_text_UPD", "url": "test_url_upd@text.com", "tags": ["TAG1", "TAG2", "UPD"], "info": {"description":
     "Test object updated", "policy": "NDA UPD", "additional field": 123456789}}
]


@pytest.mark.regression
def test_get_all_memes(get_all_memes_api):
    get_all_memes_api.get_all_memes()
    get_all_memes_api.check_response_code_is_200()
    get_all_memes_api.check_data_key()


@pytest.mark.smoke
@pytest.mark.parametrize('data', POST_DATA)
def test_post_meme(post_meme_api, data):
    post_meme_api.post_meme(payload=data)
    post_meme_api.check_response_code_is_200()
    post_meme_api.check_id_key()
    post_meme_api.check_updated_by_key()


@pytest.mark.smoke
def test_get_meme(get_meme_api, new_obj):
    get_meme_api.get_meme(new_obj)
    get_meme_api.check_response_code_is_200()
    get_meme_api.match_id_key(created_id=new_obj)
    get_meme_api.check_updated_by_key()


@pytest.mark.smoke
@pytest.mark.parametrize('data', PUT_DATA)
def test_put_meme(put_meme_api, new_obj, data):
    put_meme_api.put_meme(new_obj, payload=data)
    put_meme_api.check_response_code_is_200()
    put_meme_api.match_id_key(created_id=new_obj)
    put_meme_api.check_updated_by_key()
    put_meme_api.check_updated_text(updated_text=data['text'])
    put_meme_api.check_updated_url(updated_url=data['url'])
    put_meme_api.check_updated_description(updated_description=data['info']['description'])
    put_meme_api.check_new_tags(expected_tags=data['tags'])


@pytest.mark.smoke
def test_delete_meme(delete_meme_api, new_obj):
    delete_meme_api.delete_meme(new_obj)
    delete_meme_api.check_response_code_is_200()
    delete_meme_api.check_response_message(new_obj)
