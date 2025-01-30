import pytest

from .endpoints.post_meme import PostMeme
from .endpoints.delete_meme import DeleteMeme


@pytest.fixture()
def new_obj():
    post_meme_api = PostMeme()
    post_meme_api.post_meme()
    obj_id = post_meme_api.id
    try:
        yield obj_id
    finally:
        delete_meme_api = DeleteMeme()
        delete_meme_api.delete_meme(obj_id)
