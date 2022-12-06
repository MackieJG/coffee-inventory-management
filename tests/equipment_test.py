import unittest

from models.equipment import Equipment
from models.producer import Producer

class TestEquipment(unittest.TestCase):
    
    def setUp(self):
        self.producer = Producer('La Palma Importer', 'London', 'Green Bean Importer')
        self.equipment = Equipment('Coffee Machine', self.producer, 5, 10000, 27000)
    
    def test_equipment_has_name(self):
        self.assertEqual('Coffee Machine', self.equipment.name)

    def test_equipment_has_stock(self):
        self.assertEqual(5, self.equipment.stock)

    def test_mark_up_if_buy_price_is_0(self):
        buy_price = 0
        sell_price = 5
        
        self.assertEqual("Nothing paid for this product", self.equipment.mark_up(buy_price, sell_price))

    def test_mark_up_if_buy_price_is_5(self):
        buy_price = 5
        sell_price = 10
        self.equipment.mark_up(buy_price, sell_price)
        self.assertEqual(50, self.equipment.mark_up(buy_price, sell_price))