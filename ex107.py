from jproperties import Properties
# Write a Python program to retrieve file properties.


config = Properties()
with open('test.txt', 'rb') as read_properties:
	config.load(read_properties)

for item in config.items():
	print(item)
