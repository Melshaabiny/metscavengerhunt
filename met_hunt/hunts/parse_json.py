import json
from hunts.models import Hunts, Items, Has
from random import randrange

with open('data.json') as file:
	data = json.load(file)

# save the first hunt.
hunt = Hunts(ID=1,Title=str(data[0]['fields']['Title']), 
			Category=str(data[0]['fields']['Category']),
			Start=str(data[0]['fields']['Start']))
# save it.
hunt.save()


# save items.
for i in xrange(1, 11):
	print str(data[i]['pk']),str(data[i]['fields']['Category'])
	item = Items(ID=str(data[i]['pk']),Category=str(data[i]['fields']['Category']))
	# save it
	item.save()

for i in xrange(11, len(data)):
	# get item data.
	item = Items.objects.get(ID=str(data[i]['fields']['item']))

	# create has entry.
	has = Has(hunt=hunt,
				item=item,
				number=int(str(data[i]['fields']['number'])),
				clue=str(data[i]['fields']['clue']))
	has.save()

rnd_str = "ABCDEFGHIJKLMNabcdefghijklmn123456789"
def make_str(source):
	s = randrange(2,10)
	st = ""
	for i in xrange(0,s):
		st += rnd_str[randrange(0,len(rnd_str))]

	return st

for i in xrange(2,20):
	hunt = Hunts(ID=i,Title=make_str(rnd_str), 
			Category=make_str(rnd_str),
			Start = make_str(rnd_str))
	# save it.
	hunt.save()
