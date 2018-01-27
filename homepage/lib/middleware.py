__author__ = 'Daniel'

import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'homepage.settings'
django.setup()


def get_name():
    i = 0
    while True:
        i += 1
        yield i


class generator(object):
    def __init__(self):
        self.gen = get_name()

    def process_request(self, request):
        request.generator = self.gen