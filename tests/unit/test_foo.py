from django.test import TestCase


class DummyTestCase(TestCase):
    def test_foo_bar_baz(self):
        foo = "Foo"
        bar = "Bar"
        baz = "Baz"

        self.assertEqual(foo, "Foo")
        self.assertEqual(bar, "Bar")
        self.assertEqual(baz, "Baz")
