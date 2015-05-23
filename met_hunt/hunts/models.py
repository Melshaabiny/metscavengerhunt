"""
        The models for Hunts and Items and their relationship,
        add functions that set each Hunt's data and the data of Items that belong to it.
"""
from django.db import models

global TEMP
class Hunts(models.Model):
    """        
        This database table contains all the scavenger hunts,
        each hunt has a unique id and title, and each belongs to 
        a specific category and have a starting location
    """
    # Unique identification number for each hunt
    ID = models.CharField(unique=True, primary_key=True, max_length=50)
    # Title of the Hunt. For now, same as category.
    Title = models.CharField(max_length=200)
    # Category of the Hunt
    Category = models.CharField(max_length=200)
    # Starting point of each Scavenger Hunt
    Start = models.CharField(max_length=400)
    #CreatedBy = models.CharField(max_length = 25, default = 'MetHunt Dev Team')
    def __str__(self):
        return self.Title

class Items(models.Model):
    """
        The Items database table contains all the items of the Met (to be completed)
        each item has a unique id, belongs to a specific category,
        and is a part of one or more hunts
    """
    # Official Met issued ID for each item
    ID = models.CharField(max_length=20, unique=True, primary_key=True)
    # Item category is a subset of the Hunt category according to our design
    # e.g. Hunt category "Ancient Art" contains items from "Egyptian Art",
    # "Greek and Roman Art", and "Ancient Near Eastern Art"
    Category = models.CharField(max_length=200)
    # Type      = models.CharField(max_length = 200)
    partof = models.ManyToManyField(Hunts, through='Has')
    def __str__(self):
        return self.ID

class Has(models.Model):
    """
        I intermediate model that links Hunts to Items, each hunt has one or more items,
        and each item belongs to one or more hunts.
        In every hunt there is a clue that leads to the item and every item has an order number
    """
    hunt = models.ForeignKey(Hunts)
    item = models.ForeignKey(Items)
    number = models.IntegerField()
    clue = models.CharField(max_length=250)
    hint = models.CharField(max_length=200, default="No hint available")
    hintcrop = models.CharField(max_length=200, default="No hintcrop available")
    image = models.CharField(max_length=250, default="No image available")
    fact = models.CharField(max_length=250, default="No fact available")

class HuntProg(models.Model):
    """
        Intermediate model that is linked to hunts and has to keep track of progress for the users
    """
    hunt = models.ForeignKey(Hunts)
    user = models.CharField(max_length=30)
    cur_item_num = models.IntegerField(default = 0)
    completed = models.BooleanField(default = False)

    class Meta:
        unique_together = (("hunt","user"),)

def set_HuntsData(id_hunt):
    """
        Based on the hunt id, set_HuntsData returns a python dictionary
        containing all the Hunt's title and starting location
    """
    hunt = Hunts.objects.get(ID=id_hunt)
    hunt_title = str(hunt.Title)
    hunt_start = str(hunt.Start)
    hunt_dict = {'hunt title': hunt_title, 'hunt start': hunt_start}
    return hunt_dict

def set_ItemsData(id_hunt):
    """
        :param: IntegerId
        :rtype: pythonList        
        Based on the hunt id, set_ItemsData creates a list of tuples
        containing all the items in that hunt and their respective database
        returns TEMP[(id, clue, number), ...]
    """
    hunt_items = Has.objects.filter(hunt_id=id_hunt)
    tuples = ()
    for obj in range(0, hunt_items.count()):
        item_id = hunt_items[obj].item.ID
        item_clue = hunt_items[obj].clue
        item_number = hunt_items[obj].number
        item_hint = hunt_items[obj].hint
        item_hint_crop = hunt_items[obj].hintcrop
        item_image = hunt_items[obj].image
        item_fact = hunt_items[obj].fact
        tuples = tuples + ((item_id, item_clue, item_number, item_hint, item_image, item_fact, item_hint_crop), )
    global TEMP
    TEMP = sorted(list(tuples), key=lambda element: element[2])
    return TEMP

def pop_item(lst):
    """
        :param: pyhtonList
        :rtype: pythonList        
        Pops an item from the global list of items,
        once a user moves on the next item in the hunt.
    """
    del lst[0]
    return lst

def verify_id(usr_input):
    """
        :param: pythonString
        :rtype: Boolean        
        Checks the user input against the item id and returns a boolean result.
    """
    global TEMP
    if usr_input == TEMP[0][0]:
        return True
    else:
        return False

def init_huntprog(h_id, uname):
    """
        :param: IntegerId, pythonString
        :rtype: None     
        Records the user's hunt progress and saves it in the database.
    """
    e_hunt = Hunts.objects.filter(ID = h_id)
    hprog_check = HuntProg.objects.filter(hunt_id = h_id, user = uname).count()
    if hprog_check == 0:
        hprog = HuntProg.objects.create(hunt = e_hunt[0], user = uname)
        hprog.save()
    else:
        pass

def update_cur_item(h_id, uname, newnum):
    """
        :param: IntegerId, pythonString, IntegerNum     
        Updates the current item (where the user left of in a hunt).
    """
    hprog = HuntProg.objects.get(hunt_id = h_id, user = uname)
    hprog.cur_item_num = newnum
    hprog.save()
    
