#First assignment for WEEE entry test - Lorenzo Callegari
print("Enter the first value: ")
a = input()
print("Enter the second value: ")
b = input()

print("\n\nBEFORE SWAP\nA = " + a + "\nB = " + b)

a,b = b,a

print("\n\nAFTER SWAP:\nA = " + a + "\nB = " + b)