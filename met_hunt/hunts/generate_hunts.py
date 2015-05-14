from hunts.models import Hunts

medieval = Hunts.objects.get(Category="Medieval Art")
ancient = Hunts.objects.get(Category="Ancient Art")


# medieval = sorted(medieval, key=lambda x : -x.ID)
# ancient = sorted(ancient, key=lambda x : -x.ID)

# m_max = medieval[0].ID
# a_max = medieval[0].ID
# if m_max > a_max:
# 	m = m_max+1
# else:
# 	m = a_max+1
m = 3
for i  in range(5):
	if m >= 10:
		hunt_id = '0' + str(m)
	else:
		hunt_id = '00' + str(m)
	Hunts.objects.create(ID=hunt_id, Title=str(i+1) + "th Medieval Hunt", Category="Medieval Art")
	m = m+i+1

for i in range(5):
	if m >= 10:
		hunt_id = '0' + str(m)
	else:
		hunt_id = '00' + str(m)
	Hunts.objects.create(ID=m, Title=str(i+1) + "th Ancient Hunt", Category="Ancient Art")
	m = m + i + 1