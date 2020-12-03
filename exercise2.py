#The multi-line string was scraped from the National Weather Service Website.
#Edit this exercise to produce the output below using string manipulation techniques:
'''
Sophie Spiliotopoulos
Sept. 18,2020
Python 3.6
Using string manipulation to organize and display web scraped National Weather Service forecast data


#The multi-line string was scraped from the National Weather Service Website.
#Edit this exercise to produce the output below using string manipulation techniques:

#Tonight: Clear, Low: 55 F
#Thursday: Sunny then Chance Showers, High: 77 F
#Friday: Sunny, High: 73 F
#Saturday: Mostly Sunny, High: 77 F
#Sunday: Mostly Sunny, High: 71 F

#Note: Copy the below code in the edit mode to retain the multi-line string formatting. There should be 39 lines of code when pasted in Python IDLE.
'''
# -*- coding: utf-8 -*-
# Scraped multi-line String

forecast = ''' 

Tonight
ClearLow: 55 F

Thursday
Sunny thenChanceShowersHigh: 77 F

Friday
SunnyHigh: 73 F

Saturday
Mostly SunnyHigh: 77 F

Sunday
Mostly SunnyHigh: 71 F
'''
import re #import regular expressions operations library 

forecast_list = forecast.split('\n\n') #split multi line string into list, splitting at '\n\n'
del forecast_list[0] #delete empty space in first line 
for day in forecast_list: #loop through list
  i = 0 #counter for indexes
  while i < len(forecast_list): 
    day = day.replace(forecast_list[i], re.sub('([A-Z])', r' \1', forecast_list[i])) #replace string in list with new string that adds spaces before capitalized words
    i = i + 1 # continue index counter to cycle through each string within list
  day = day.replace('\n',':') #replace newlines with colon 
  day = day.replace('  ', ' ') #replace any double spaces with a single space 
  day = day.replace('Clear','Clear,') #add comma after 'clear'
  day = day.replace('Sunny','Sunny,') #add comma after 'sunny'
  day = day.replace('Showers','Showers,') #add comma after 'showers' in line 2 
  day = day.replace('F:', 'F') #fix final line, originally there was a : after F
  print(day)
