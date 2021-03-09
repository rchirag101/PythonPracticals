import random
hashTable = {}
while True:
	new_data = input("Enter a data to generate Hash(Type break to exit and print hash table) : ")
	if 'break' in new_data.lower():
		break
	new_key = len(new_data)
	new_key = ( random.randrange(1000) + new_key ) + new_key * new_key
	hashTable[str(new_key)] = new_data
print(hashTable)