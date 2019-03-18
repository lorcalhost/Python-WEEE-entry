#First assignment for WEEE entry test - Lorenzo Callegari
a = input('Enter the first value: ')
b = input('Enter the second value: ')

print("BEFORE SWAP:\nA = {}\nB = {}".format(a, b))

a,b = b,a

print("\nAFTER SWAP:\nA = {}\nB = {}".format(a, b))
