def getMaxof3(no1, no2, no3):
    if(no1 > no2):
        if(no1 > no3):
            return no1
        else:
            return no3
    else:
        if(no2 > no3):
            return no2
        else:
            return no3


def getMinof3(no1, no2, no3):
    if(no1 < no2):
        if(no1 < no3):
            return no1
        else:
            return no3
    else:
        if(no2 < no3):
            return no2
        else:
            return no3

def forloop(len):
	for i in range(1,len+1):
		print(i)
def whileloop(len):
	i = 1
	while i < len+1:
		print(i)
		i += 1

no1 = input('Enter no1 : ')
no2 = input('Enter no2 : ')
no3 = input('Enter no3 : ')
print('{} is maximum'.format(getMaxof3(no1, no2, no3)))
print('{} is minimum'.format(getMinof3(no1, no2, no3)))

no4 = int(input('\nEnter number to print loop : '))
forloop(no4)
no5 = int(input('\nEnter number to print loop : '))
whileloop(no5)
