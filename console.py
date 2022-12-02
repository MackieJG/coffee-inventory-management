import pdb

from models.producer import Producer

import repositories.producer_repository as producer_repository

producer_repository.delete_all()

producer1 = Producer('Coffee Imports', 'London', 'green been importer')
producer_repository.save(producer1)


producer2 = Producer('Equipment Imports', 'London', 'coffee guide distributor')
producer_repository.save(producer2)

