import pytest
from port import app


@pytest.fixture
def client():
    app.config.update(
        TESTING=True
    )

    with app.test_client() as client:
        yield client


# Test 1: Homepage loads successfully
def test_homepage(client):
    response = client.get('/')

    assert response.status_code == 200


# Test 2: Homepage returns HTML
def test_homepage_content_type(client):
    response = client.get('/')

    assert response.content_type.startswith('text/html')


# Test 3: Invalid page returns 404
def test_invalid_page(client):
    response = client.get('/this-page-does-not-exist')

    assert response.status_code == 404

    