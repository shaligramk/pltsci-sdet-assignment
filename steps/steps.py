import requests
from behave import given, when, then

@given('url "{url}"')
def step_given_url(context, url):
    context.url = url

@given('request {request_body}')
def step_given_request(context, request_body):
    context.request_body = request_body

@when('method {http_method}')
def step_when_method(context, http_method):
    context.http_method = http_method.upper()

    if context.http_method == 'GET':
        context.response = requests.get(context.url, json=context.request_body)
    elif context.http_method == 'POST':
        context.response = requests.post(context.url, json=context.request_body)
    else:
        raise ValueError(f"Unsupported HTTP method: {context.http_method}")

@then('status {expected_status}')
def step_then_status(context, expected_status):
    expected_status = int(expected_status)
    assert context.response.status_code == expected_status

@then('match {json_path} == "{expected_value}"')
def step_then_match(context, json_path, expected_value):
    json_data = context.response.json()
    actual_value = json_data.get(json_path)
    assert actual_value == expected_value
