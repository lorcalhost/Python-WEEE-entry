#Third assignment for WEEE entry test - Lorenzo Callegari
import json

#Read disks.json file and load in disks dictionary
f = open("./disks.json").read()
disks = json.loads(f)

#Sorting with sorted()
disks = sorted(disks, key=lambda d: d['code'], reverse=False)

text_file = open("./orderedWorkingHHDList.txt", "w")

#Loop through the ordered list and write in the file the codes of the working hard disks
for x in disks:
    if x['working'] == 'YES':
        text_file.write(x['code'] + '\n')

text_file.close()
