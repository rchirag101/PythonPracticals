a = 5
b = 0 
try:
	assert b != 0, "Cannot divide by Zero"
	print(a,'/',b,'=',a//b)
except AssertionError as error:
	print(error)

def KelvinToFahrenheit(temp):
 assert (temp >= 0),"Colder than absolute zero!"
 return ((temp-273)*1.8)+32
print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))

