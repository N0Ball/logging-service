from .conftest import client

def test_health(client):
    response = client.get("/health")
    print(response)