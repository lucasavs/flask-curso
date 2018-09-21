from flask import url_for
import pytest


@pytest.fixture()
def resp(client):
    response = client.get(url_for('hello'))
    return response


def test_hello_status_code(resp):
    assert resp.status_code == 200


def test_hello_status_msg(resp):
    assert 'madruga' in resp.get_data(as_text=True)
