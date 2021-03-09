list1 = ['AI', 'Python', 1234, 2020]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1 : ", list1)
print ("list2 : ", list2)
print ("\nLength of list1 : ",len(list1))
print ("Length of list2 : ",len(list2))
print ("list1[0] : ", list1[0])
print ("list2[1:5] : ", list2[1:5])

print("-"*50)

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'enroll':17017,'name': 'Chirag', 'dept': 'IT'}
print ("Dictionary : ",tinydict) # Prints complete dictionary
print (tinydict.keys()) # Prints all the keys
print (tinydict.values()) # Prints all the values
print ("dict['one'] : ",dict['one']) # Prints value for 'one' key
print ("dict[2] : ",dict[2]) # Prints value for 2 key

print("-"*50)

tuple = ( 'Chitti', 786 , 2.23, 'G1', 70.2 )
tinytuple = (123, 'Chitti')
print (tuple) # Prints complete tuple
print (tuple[0]) # Prints first element of the tuple
print (tuple[1:3]) # Prints elements starting from 2nd till 3rd
print (tuple[2:]) # Prints elements starting from 3rd element
print (tinytuple * 2) # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple