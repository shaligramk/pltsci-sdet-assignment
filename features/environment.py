from yaml import load


def before_all(context):
    context.api_endpoints = {}
    context.request_headers = {}
    context.response_codes = {}
    context.request_bodies = {}
    context.response_texts = {}
    context.verify_ssl = True