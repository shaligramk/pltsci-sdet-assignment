import requests
import json
from behave import given, when, then

# Assuming the API endpoint URL
API_URL = "http://example.com/hoover"

@given('a room size of {room_size_x:d}, {room_size_y:d}')
def set_room_size(context, room_size_x, room_size_y):
    context.room_size = [room_size_x, room_size_y]

@given('the hoover is initially placed at {initial_coord_x:d}, {initial_coord_y:d}')
def set_initial_coord(context, initial_coord_x, initial_coord_y):
    context.initial_coord = [initial_coord_x, initial_coord_y]

@given('there are patches of dirt at the following locations:')
def set_dirt_patches(context, table):
    context.dirt_patches = [list(map(int, row)) for row in table.rows]

@given('the driving instructions are "{instructions}"')
def set_instructions(context, instructions):
    context.instructions = instructions

@when('the hoover service is invoked')
def invoke_hoover_service(context):
    request_payload = {
        "roomSize": context.room_size,
        "coords": context.initial_coord,
        "patches": context.dirt_patches,
        "instructions": context.instructions
    }
    response = requests.post(API_URL, json=request_payload)
    context.response = response.json()

@then('the final hoover position should be {final_coord_x:d}, {final_coord_y:d}')
def check_final_position(context, final_coord_x, final_coord_y):
    expected_coords = [final_coord_x, final_coord_y]
    assert context.response["coords"] == expected_coords

@then('the number of cleaned patches should be {cleaned_patches:d}')
def check_cleaned_patches(context, cleaned_patches):
    assert context.response["patches"] == cleaned_patches
