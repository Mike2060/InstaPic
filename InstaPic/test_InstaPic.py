#1
import os
import tempfile

import pytest

import InstaPic
app = InstaPic.create_app()

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            InstaPic.db.initDB()
        yield client

def test_login_logout(client):
    """Make sure login and logout works."""

    rv = login(client, 'test', 'test')
    assert b'You were logged in' in rv.data

    rv = logout(client)
    assert b'You were logged out' in rv.data


def login(client, username, password):
    return client.post('InstaPic/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('InstaPic/logout', follow_redirects=True)
