import pdb

from models.producer import Producer
from models.coffee import Coffee
from models.equipment import Equipment


import repositories.producer_repository as producer_repository
import repositories.coffee_repository as coffee_repository
import repositories.equipment_repository as equipment_repository

producer_repository.delete_all()
coffee_repository.delete_all()
equipment_repository.delete_all()

producer1 = Producer('Carribean Goods', 'Glasgow', 'green bean importer with a focus on Guatemala')
producer2 = Producer('Nordic Approach', 'Oslo', 'green bean importer')
producer3 = Producer('DRWakefield', 'London', 'green bean importer')
producer4 = Producer('Mercanta', 'Glasgow', 'green bean importer')
producer5 = Producer('Falcon Speciality', 'East Sussex', 'green bean importer')
producer_repository.save(producer1)
producer_repository.save(producer2)
producer_repository.save(producer3)
producer_repository.save(producer4)
producer_repository.save(producer5)

producer6 = Producer('La Marzorcco', 'Milan', 'varied coffee associated equipment')
producer7 = Producer('Slayer', 'Seattle', 'coffee machinery')
producer8 = Producer('Mavam', 'Seattle', 'coffee machinery')
producer9 = Producer('Kees van der Westen', 'Amsterdam', 'coffee machinery')
producer10 = Producer('Synesso', 'Seattle', 'coffee machinery')
producer_repository.save(producer6)
producer_repository.save(producer7)
producer_repository.save(producer8)
producer_repository.save(producer9)
producer_repository.save(producer10)


coffee1 = Coffee('Paraiso','Brazil', 'Mundo Novo / Yellow Catuai / Red Catuai - Pulp Natural', producer2, 50, 650, 7.50)
coffee2 = Coffee('Suarez','Colombia', 'Caturra / Typica / Colombia - Washed', producer3, 100, 1100, 8.10)
coffee3 = Coffee('Yermy Pedraza','Colombia', 'Colombia - Natural Anaerobic', producer3, 30, 550, 10.50)
coffee4 = Coffee('Blue Mountain AA','Kenya', 'Bourbon / Kent / SL28 - Washed', producer5, 120, 1200, 9.50)
coffee5 = Coffee('Finca Medina','Guatemala', 'Marsellesa / Bourbon / Caturra - Natural', producer1, 50, 650, 7.50)
coffee6 = Coffee('Daterra Masterpiece','Brazil', 'Geisha - Natural', producer4, 70, 1800, 23.50)
coffee_repository.save(coffee1)
coffee_repository.save(coffee2)
coffee_repository.save(coffee3)
coffee_repository.save(coffee4)
coffee_repository.save(coffee5)
coffee_repository.save(coffee6)



equipment1 = Equipment('Spirit Coffee Machine', producer9, 3, 10000, 17000)
equipment2 = Equipment('Water for Coffee', producer6, 10, 6, 9)
equipment3 = Equipment('250g coffee bags', producer7, 150, 0.4, 0.6)
equipment4 = Equipment('moccamaster', producer10, 30, 100, 180)
equipment5 = Equipment('6oz cups', producer8, 200, 3, 7)
equipment_repository.save(equipment1)
equipment_repository.save(equipment2)
equipment_repository.save(equipment3)
equipment_repository.save(equipment4)
equipment_repository.save(equipment5)




