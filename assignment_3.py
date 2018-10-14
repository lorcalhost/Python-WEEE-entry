#Third assignment for WEEE entry test - Lorenzo Callegari
import json

#QuickSort
def partition(A, low, high):
    i = low - 1
    pivot = int(A[high]['code'][3:9]) #defining pivot value to be the last value of the dictionary

    for j in range(low, high):
        if int(A[j]['code'][3:9]) <= pivot:
            i = i+1
            A[i]['code'], A[j]['code'] = A[j]['code'], A[i]['code']
            A[i]['capacity'], A[j]['capacity'] = A[j]['capacity'], A[i]['capacity']
            A[i]['working'], A[j]['working'] = A[j]['working'], A[i]['working']

    A[i+1]['code'], A[high]['code'] = A[high]['code'], A[i+1]['code']
    A[i+1]['capacity'], A[high]['capacity'] = A[high]['capacity'], A[i+1]['capacity']
    A[i+1]['working'], A[high]['working'] = A[high]['working'], A[i+1]['working']
    return(i+1)


def quickSort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quickSort(A, low, pi-1)
        quickSort(A, pi+1, high)

#Read disks.json file and load in disks dictionary
f = open("disks.json").read()
disks = json.loads(f)

jsonLen = len(disks)
quickSort(disks, 0, jsonLen-1)

text_file = open("orderedWorkingHHDList.txt", "w")

#Loop through the ordered list and write in the file the codes of the working hard disks
for x in range(len(disks)):
    if disks[x]['working'] == 'YES':
        j = str(disks[x]['code'])
        text_file.write(j + "\n")

text_file.close()
