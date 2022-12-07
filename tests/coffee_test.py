import unittest

from models.coffee import Coffee
from models.producer import Producer

class TestCoffee(unittest.TestCase):

    def setUp(self):
        self.producer = Producer('La Palma Importer', 'London', 'Green Bean Importer')
        self.coffee = Coffee('La Palma', 'Colombia', 'Geisha', self.producer, 5, 10, 25, )

    def test_coffee_has_name(self):
        self.assertEqual('La Palma', self.coffee.name)

    def test_coffee_has_origin(self):
        self.assertEqual('Colombia', self.coffee.origin)

    