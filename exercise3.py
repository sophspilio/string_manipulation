'''
Sophie Spiliotopoulos
Sept 19, 2020
Python 3.6
Extracting the lat and long from a url
'''

# Write code to extract the latitude and longitude from the URL: https://www.google.com/maps/@42.2509428,-71.8249939,17z
# Output should be text that reads:

# Latitude: 42.2509428
# Longitude: -71.8249939

import re

url = 'https://www.google.com/maps/@42.2509428,-71.8249939,17z' #assign given url a variable and make it a string

lat, lon = re.search(r'@(.*?),(.*?),',url).groups() #assign variables lat and lon by searching through the given string, using '@' and  ',' as indicator of where to start 
print('Latitude:',lat) 
print('Longitude:',lon)

