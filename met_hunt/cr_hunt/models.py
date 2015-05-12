from django.db import models
from hunts.models import Items
"""
		* Create your models here.
		* ----------Tables----------
		##Copy of models from hunts subapp
"""
global TEMP
class cr_Hunts(models.Model):
	"""
		* database table that contains all the scavenger hunts 
		* each hunt has a unique id and title
		* each belongs to a specific category and have a starting location
	"""
	# Unique identification number for each hunt
	ID = models.CharField(max_length = 25, unique = True, primary_key = True)
	# Title of the Hunt. For now, same as category.
	Title = models.CharField(max_length = 200)
	# Category of the Hunt
	Category = models.CharField(max_length = 200)
	# Starting point of each Scavenger Hunt 
	Start = models.CharField(max_length = 400)
	CreatedBy = models.CharField(max_length = 25)
	def __str__(self):
		return self.Title

#items should not be needed in this app, just in case
#class cr_Items(models.Model):
#	"""
#		* database table that contains all the items of the Met (to be completed)
#		* each item has a unique id, belongs to a specific category
#		* has a specific type (painting, sculpture, instrument, etc.)
#		* is a part of one or more hunts
#	"""
#	# Official Met issued ID for each item
#	ID = models.CharField(max_length = 20, unique = True, primary_key = True)
	# Item category is a subset of the Hunt category according to our design
	# e.g. Hunt category "Ancient Art" contains items from "Egyptian Art",
	# "Greek and Roman Art", and "Ancient Near Eastern Art"
#	Category = models.CharField(max_length = 200)
	# Type 		= models.CharField(max_length = 200)
#	partof = models.ManyToManyField(Hunts, through = 'Has')
#	def __str__(self):
#		return self.ID

class cr_Has(models.Model):
	"""		
		* intermediate model that links Hunts to Items
		* each hunt has one or more items
		* each item belongs to one or more hunts
		* in every hunt there is a clue that leads to the item and every item has an order number
	"""
	hunt = models.ForeignKey(cr_Hunts)
	item = models.ForeignKey(Items)
	number = models.IntegerField() 
	clue = models.CharField(max_length = 250)


def add_hunt_its(id_hunt,title,start):
	"""
		* Takes in 3 parameters and creates a new hunt tuple
	"""
	hunt = cr_Hunts.objects.create(ID = id_hunt)
	hunt.Title = title
	hunt.Start = start
	#hunt.Category = cat
	hunt.save()

def add_hunt_has(id_hunt,nitem,nnum,nclue):
        """
                * Takes in 4 parameters and creates a new has tuple
        """
	has = cr_Has.objects.create(hunt = id_hunt, item = nitem)
	has.number = nnum
	has.clue = nclue
	has.save()

