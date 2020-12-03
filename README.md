# Lab 4 – String Manipulation
Note: I've added my Colab Notebooks for reference, as well as edited the original `.py` files in this repo. 
## Summary of Code 1
The first exercise created a function that would capitalize the first and fourth letter of a given word. I chose to use the indexes to identify the first `word[0]` and fourth `word[3]` words to be capitalized (using `.capitalize()`) and to join them  all together simply using + to concatenate. 
### Errors? 
I did not encounter any issues on this part of the lab! 

## Summary of Code 2
This code used string maniuplation to clean up weather data scarped from the National Weather Service. I used a for loop to run through each string in the list, as well as `.replace()` to remove extra spaces, new lines, etc. within the code. 
### Errors? 
I struggled with how to split up the parts of the string that were multiple words joined together (e.g. `ClearLow`). I ended up doing a lot of googling and founda few helpful Stack Overflow articles that used `import re` and `re.sub`. The most useful one I found is [here](https://stackoverflow.com/questions/37505224/add-a-space-between-each-word-in-the-string). 
I also used a lot of simple `.replace()` and I'm not sure if there was a more efficient way of cleaning up the code then simply replacing. 

## Summary of Code 3
This code parsed a given url and identified the latitude and longitude. I used `re.search` to search the string and used the characters around the latitude and longtiude as guides for where I wanted my code to select from. I used a Stack Overflow post as a guide, which created a tuple for the latitutde and longitude. 
### Errors? 
As I said above, I used a Stack Overflow [post](https://stackoverflow.com/questions/56999390/how-to-extract-longitude-and-latitude-from-a-link) to help guide me, as I felt a bit lost on how to pull a chunk of numbers from a long string. This post really helped me, and I was able to edit it for my own needs. 
