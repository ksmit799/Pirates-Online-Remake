# File: P (Python 2.4)

from direct.distributed.DistributedObject import DistributedObject
from pirates.uberdog.DistributedInventory import DistributedInventory
from direct.directnotify.DirectNotifyGlobal import directNotify

class PirateInventory(DistributedInventory):
    notify = directNotify.newCategory('Inventory')
    
    def __init__(self, repository):
        DistributedInventory.__init__(self, repository)


