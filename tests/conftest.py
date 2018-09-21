import pytest

from app import app


@pytest.fixture()
def client():
    # app.testing = True
    client = app.test_client()
    context = app.test_request_context()
    context.push()
    return client
