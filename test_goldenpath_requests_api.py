import requests
import pytest

@pytest.mark.parametrize("room_size", [[5, 5], [6, 6], [7, 7]])
def test_hoover_navigation_validation(room_size):
    url = 'http://localhost:8080/v1/cleaning-sessions'
    request_body = {
        "roomSize": room_size,
        "coords": [2, 1],
        "patches": [[1, 0], [2, 2], [2, 3]],
        "instructions": "NNESEESWNWW"
    }

    response = requests.post(url, json=request_body)

    assert response.status_code == 200
    assert response.json()["coords"] == [1, 3]
    assert response.json()["patches"] == 1
