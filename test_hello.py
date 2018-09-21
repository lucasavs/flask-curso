from app import app
from flask import url_for
import pytest

@pytest.fixture(scope='session')
def resp():
    print('executando fixture')
    client=app.test_client()
    context = app.test_request_context()
    context.push()
    response=client.get(url_for('hello'))
    return response

def test_hello_status_code(resp):
    assert resp.status_code == 200


def test_hello_status_msg(resp):
    client=app.test_client()
    resp=client.get('/')
    assert 'madruga' in resp.get_data(as_text=True)