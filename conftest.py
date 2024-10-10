import pytest

from .endpoints.get_all_memes import GetAllMemes
from .endpoints.post_meme import PostMeme
from .endpoints.get_meme import GetMeme
from .endpoints.put_meme import PutMeme
from .endpoints.delete_meme import DeleteMeme
from .tests.test_api import POST_DATA, PUT_DATA


@pytest.fixture()
def get_all_memes_api():
    return GetAllMemes()


@pytest.fixture()
def post_meme_api():
    return PostMeme()


@pytest.fixture()
def get_meme_api():
    return GetMeme()


@pytest.fixture()
def put_meme_api():
    return PutMeme()


@pytest.fixture(scope="session")
def delete_meme_api():
    yield DeleteMeme()


@pytest.fixture()
def new_obj(post_meme_api, delete_meme_api):
    payload = POST_DATA[0]
    post_meme_api.post_meme(payload)
    obj_id = post_meme_api.obj_id
    try:
        PUT_DATA[0]['id'] = obj_id
        yield obj_id
    finally:
        delete_meme_api.delete_meme(obj_id)
