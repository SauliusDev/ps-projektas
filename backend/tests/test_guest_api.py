from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_deals_returns_list():
    response = client.get('/api/guest/deals')
    assert response.status_code == 200
    assert isinstance(response.json()['items'], list)
