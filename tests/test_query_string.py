from flask import url_for
import pytest


@pytest.fixture
def resp(client):
    dct = {'name': 'Renzo', 'lastname': 'Nuccitelli'}
    return client.get(url_for('name_lastname'), query_string=dct)


def test_status_code(resp):
    assert resp.status_code == 200
