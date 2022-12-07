import unittest

from models.equipment import Equipment
from models.producer import Producer

class TestEquipment(unittest.TestCase):
    
    def setUp(self):
        self.producer = Producer('La Palma Importer', 'London', 'Green Bean Importer')
        self.equipment = Equipment('Coffee Machine', self.producer, 5, 10000, 27000)
        self.equipment1 = Equipment('Coffee Machine', self.producer, 5, 0, 5)

    def test_equipment_has_name(self):
        self.assertEqual('Coffee Machine', self.equipment.name)

    def test_equipment_has_stock(self):
        self.assertEqual(5, self.equipment.stock)

    def test_mark_up_if_buy_price_is_0(self):
        self.assertEqual("Nothing paid for this product", self.equipment1.mark_up())

    def test_mark_up_if_buy_price_is_10000(self):
        self.assertEqual(170, self.equipment.mark_up())