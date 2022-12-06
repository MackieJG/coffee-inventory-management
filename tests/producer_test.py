import unittest
from models.producer import Producer

class TestProducer(unittest.TestCase):

    def setUp(self):
        
        self.producer1 = Producer('La Palma Importer', 'London', 'Green Bean Importer')
        self.producer2 = Producer('Brewguides', 'London', 'Brewguide distributor')

    def test_producer_has_name(self):
        self.assertEqual('La Palma Importer', self.producer1.name)

    def test_producer_has_location(self):
        self.assertEqual('London', self.producer2.location)

    def test_producer_has_description(self):
        self.assertEqual('Brewguide distributor', self.producer2.description)



