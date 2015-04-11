from django.db import models

# Create your models here.
#----------Tables-----------#

# database table that contains all the scavenger hunts 
# each hunt has a unique id and name
# and belong to a specific category 

class Hunts(models.Model):
	
	ID			= models.IntegerField(unique = True, primary_key = True)
	Title 		= models.CharField(max_length = 200)
	Category 	= models.CharField(max_length = 200)

	def __str__(self):
		return self.Title

# database table that contains all the items of the Met (to be completed)
# each item has a unique id, belongs to a specific category
# has a specific type (painting, sculpture, instrument, etc.)
# is a part of one or more hunts

class Items(models.Model):
	ID = models.CharField(max_length = 20, unique = True, primary_key = True)
	Category = models.CharField(max_length = 200)
	Type = models.CharField(max_length = 200)
	partof = models.ManyToManyField(Hunts, through = 'Has')

	def __str__(self):
		return self.ID
		
# intermediate model that links Hunts to Items
# each hunt has one or more items
# each item belongs to one or more hunts
# in every hunt there is a clue that leads to the item
class Has(models.Model):
	hunt = models.ForeignKey(Hunts)
	item = models.ForeignKey(Items)
	clue  = models.CharField(max_length = 250)
