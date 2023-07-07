import requests

BASE_URL = 'http://localhost:8080/v1/cleaning-sessions'

def send_post_request(url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response

def assert_response_status(response, expected_status):
    assert response.status_code == expected_status

def assert_response_error(response, expected_error):
    assert response.json()['error'] == expected_error

def test_scenario(url, data, expected_status, expected_error):
    response = send_post_request(url, data)
    assert_response_status(response, expected_status)
    assert_response_error(response, expected_error)

# Invalid Values (Error Handling)
def test_invalid_values_error_handling():
    url = BASE_URL
    data = {
        "roomSize": [3, 3],
        "coords": [1, 2],
        "patches": [[1, 0], [2, 2], [3, 3]],
        "instructions": "NNNNNNESEESWNWW"
    }
    test_scenario(url, data, 400, None)

def test_start_point_outside_room_size_error_handling():
    url = BASE_URL
    data = {
        "roomSize": [3, 3],
        "coords": [1, 3],
        "patches": [[1, 0], [2, 2], [3, 3]],
        "instructions": "NNNNNNESEESWNWW"
    }
    test_scenario(url, data, 400, None)

def test_negative_values_room_size_error_handling():
    url = BASE_URL
    data = {
        "roomSize": [-100, -100],
        "coords": [1, 3],
        "patches": [[1, 0], [2, 2], [3, 3]],
        "instructions": "NNNNNNESEESWNWW"
    }
    test_scenario(url, data, 400, None)

def test_negative_values_start_point_error_handling():
    url = BASE_URL
    data = {
        "roomSize": [3, 3],
        "coords": [-100, -7],
        "patches": [[1, 0], [2, 2], [3, 3]],
        "instructions": "NNNNNNESEESWNWW"
    }
    test_scenario(url, data, 400, None)

# Missing API Fields/Parameters
def test_missing_room_size_error_handling():
    url = BASE_URL
    data = {
        "coords": [-1, -3],
        "patches": [[1, 0], [2, 2], [3, 3]],
        "instructions": "NNNNNNESEESWNWW"
    }
    test_scenario(url, data, 400, None)

def test_missing_coords_error_handling():
    url = BASE_URL
    data = {
        "roomSize": [3, 3],
        "patches": [[1, 0], [2, 2], [3, 3]],
        "instructions": "NNNNNNESEESWNWW"
    }
    test_scenario(url, data, 400, None)

def test_missing_instructions_error_handling():
    url = BASE_URL
    data = {
        "roomSize": [3, 3],
        "coords": [-1, -3],
        "patches": [[1, 0], [2, 2], [3, 3]]
    }
    test_scenario(url, data, 400, None)

def test_missing_patches_error_handling():
    url = BASE_URL
    data = {
        "roomSize": [3, 3],
        "coords": [-1, -3],
        "instructions": "NNNNNNESEESWNWW"
    }
    test_scenario(url, data, 400, None)

# Invalid API Calls to check error messaging/status code
def test_invalid_api_calls_error_handling():
    url = BASE_URL
    data = {
        "roomSize": [3, 3],
        "coords": [1, 2],
        "patches": [[1, 0], [2, 2], [3, 3]],
        "instructions": "NNNNNNESEESWNWW"
    }

    response = send_post_request(url, data)
    assert_response_status(response, 405)
    assert_response_error(response, "Method Not Allowed")

    url = 'http://localhost:8080/v1/nba-basketball'
    response = send_post_request(url, data)
    assert_response_status(response, 404)
    assert_response_error(response, "Not Found")

# Run the tests
# test_invalid_values_error_handling()
# test_start_point_outside_room_size_error_handling()
# test_negative_values_room_size_error_handling()
# test_negative_values_start_point_error_handling()
# test_missing_room_size_error_handling()
# test_missing_coords_error_handling()
# test_missing_instructions_error_handling()
# test_missing_patches_error_handling()
# test_invalid_api_calls_error_handling()
