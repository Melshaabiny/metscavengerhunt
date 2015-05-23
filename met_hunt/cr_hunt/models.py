"""
        The models for create hunt feature are implemented in this file.
        This feature allows the users to 
"""
from django.db import models
from hunts.models import Items

global TEMP
class cr_Hunts(models.Model):
    """
        Database table that contains all the scavenger hunts.
        Each hunt has a unique id and title,
        where each belongs to a specific category and have a starting location
    """
    # Unique identification number for each hunt
    ID = models.CharField(max_length=25, unique=True, primary_key=True)
    # Title of the Hunt. For now, same as category.
    Title = models.CharField(max_length=200)
    # Category of the Hunt
    Category = models.CharField(max_length=200)
    # Starting point of each Scavenger Hunt
    Start = models.CharField(max_length=400)
    CreatedBy = models.CharField(max_length=25, default='MetHunt Dev Team')
    def __str__(self):
        return self.Title

class cr_Has(models.Model):
    """
        Intermediate model that links Hunts to Items
        each hunt has one or more items and each item belongs to one or more hunts.
        In every hunt there is a clue that leads to the item and every item has an order number
    """
    hunt = models.ForeignKey(cr_Hunts)
    item = models.ForeignKey(Items)
    number = models.IntegerField(default=1)
    clue = models.CharField(max_length=250)


def add_hunt_its(id_hunt, title, start, uname):
    """
        :param: IntegerId, pythonString, pythonString, pythonString
        :rtype: None      
        Takes in 4 parameters and creates a new hunt tuple
    """
    hunt = cr_Hunts.objects.create(ID = id_hunt)
    hunt.Title = title
    hunt.Start = start
    #hunt.Category = cat
    hunt.CreatedBy = uname
    hunt.save()

def add_hunt_has(id_hunt, nitem, nnum, nclue):
    """
        :param: IntegerId, pythonString, pythonString, pythonString
        :rtype: None   
        * Takes in 4 parameters and creates a new has tuple
    """
    huntobj = cr_Hunts.objects.get(ID = id_hunt)
    itemobj = Items.objects.get(ID = nitem)
    has = cr_Has.objects.create(hunt=huntobj, item=itemobj)
    has.number = nnum
    has.clue = nclue
    has.save()

def gen_hunt_id(uname):
    """
        :param: pythonString
        :rtype: IntegerId
        This function generates a unique hunt id for the created hunt. 
    """
    num_of_hunts = cr_Hunts.objects.filter(CreatedBy=uname).count()
    #num_2 = Hunts.objects.filter(CreatedBy = uname).count()
    #num_of_hunts = num_of_hunts + num_2
    new_id = ''
    new_id += str(uname) + str(num_of_hunts)
    return new_id

def get_cur_count(id_hunt):
    """
        :param: pythonString
        :rtype: IntegerId
        This function returns the number of items that the user added to the hunt being created.
    """ 
    huntobj = cr_Hunts.objects.filter(ID = id_hunt)
    if huntobj.first():
        cur_count = cr_Has.objects.filter(hunt=huntobj.first()).count()
        return cur_count
    else:
        return 0
