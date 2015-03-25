import unittest
from lazyprop import lazyprop


class LazypropClass(object):
    def __init__(self):
        self._counter = 0

    @lazyprop
    def counter(self):
        self._counter += 1
        return self._counter


class LazypropTest(unittest.TestCase):
    def setUp(self):
        self._p = LazypropClass()

    def test_get(self):
        self.assertEqual(1, self._p.counter)

    def test_getattr(self):
        self.assertEqual(1, getattr(self._p, 'counter'))

    def test_lazy(self):
        self.assertEqual(1, self._p.counter)
        self.assertEqual(1, self._p.counter)

    def test_del(self):
        self.assertEqual(1, self._p.counter)
        del self._p.counter
        self.assertEqual(2, self._p.counter)

    def test_delattr(self):
        self.assertEqual(1, self._p.counter)
        delattr(self._p, 'counter')
        self.assertEqual(2, self._p.counter)

    def test_set(self):
        self._p.counter = 10
        self.assertEqual(10, self._p.counter)

    def test_setattr(self):
        setattr(self._p, 'counter', 10)
        self.assertEqual(10, self._p.counter)

    def test_overwrite(self):
        self._p.counter = 10
        self.assertEqual(10, self._p.counter)
        self._p.counter = 11
        self.assertEqual(11, self._p.counter)
