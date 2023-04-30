# Deeper Insights Test Code Repo
deeper insights test code

This program lets user pass a textfile path as a arguement to the script.
The script then looks for the search term in the last line of the file and looks for that search item in the other lines of the file.

**USER HELP** - Use the help function by running -h as an arguement to the program

**DEVELOPER HELP** - Please refer to comments and doc strings in the di_testcode.py file

The file should be a txt file

**USAGE**
    
    pip install -r requirements.txt

    py di_testcode.py <<path of the file>>


Assumptions:
The search term is always a alphabetical string. It never has any numbers in it.  As described in the problem statement it is a word
This program runs on python3 not python2.7 as it no longer has support. 
File is a text file as this is a basic program that checks for text files.
The contents of the files are relatively small without any empty lines in between. readlines() function takes time for a larger file size. The complexity of the problem can be reduced by not using .readlines()

I didnt see the need for __init__ function in the class StringMatcher. If you think its necessary please send me an email. 

