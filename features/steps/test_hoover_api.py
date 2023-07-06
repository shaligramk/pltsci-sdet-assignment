import requests
from behave import given, when, then
from hamcrest import assert_that, equal_to

@given('url "{url}"')
def step_given_url(context, url):
    context.url = url

@given('request {request}')
def step_given_request(context, request):
    context.request = request

@when('method {method}')
def step_when_method(context, method):
    context.method = method
    if method == 'POST':
        context.response = requests.post(context.url, json=context.request)
    elif method == 'GET':
        context.response = requests.get(context.url, json=context.request)

@then('status {status_code}')
def step_then_status(context, status_code):
    assert_that(context.response.status_code, equal_to(int(status_code)))

@then('match $.{field} == {expected_value}')
def step_then_match_field(context, field, expected_value):
    response_json = context.response.json()
    assert_that(response_json[field], equal_to(eval(expected_value)))
