import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    return client.get(reverse('base:home'))


def test_home_status_code(resp):
    assert resp.status_code == 200
