import os
import valorant
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        KEY = os.environ["valorantpy-token"]

        self.access_key = KEY
        self.client = valorant.Client(KEY)

    def tearDown(self):
        self.client.handle.sess.close()


from .client import *