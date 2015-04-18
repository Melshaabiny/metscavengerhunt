import json
from hunts.models import Hunts, Items, Has

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

