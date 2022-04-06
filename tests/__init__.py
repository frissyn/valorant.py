import os
import valorant
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        KEY = os.environ["VALPY_KEY"]

        self.access_key = KEY
        self.client = valorant.Client(KEY, locale=None, load_content=True)

    def tearDown(self):
        self.client.handle.sess.close()

    def assertHasAttr(self, obj: object, attr: str):
        if not hasattr(obj, attr):
            self.fail(f"{obj.__class__} has no attribute '{attr}'.")


from .client import *
git 