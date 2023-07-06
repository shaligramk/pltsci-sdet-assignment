import os

def before_all(context):
    context.url = None
    context.request = None
    context.method = None
    context.response = None

def after_scenario(context, scenario):
    context.url = None
    context.request = None
    context.method = None
    context.response = None
