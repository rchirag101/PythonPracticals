import re
regex_email = re.compile(r"[^@]+@[^@]+\.[^@]+")
while True:
	email = input("Enter Email : ")
	if not regex_email.match(email):
		print("\nPlease enter Valid Email address ")
	else:
		break
