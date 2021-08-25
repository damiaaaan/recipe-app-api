from django.test import TestCase


class FooTests(TestCase):

    def test_one(self):
        self.assertEqual(1, 1, "Funciona")
