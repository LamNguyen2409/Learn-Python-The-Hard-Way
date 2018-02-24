# Python list function
#https://learnpythonthehardway.org/book/ex2.html

#Exercise 1 : A good First Program
#Typing a file with this following detail -> save to *.py file 

#if you're from  another country, and you get errors about ASCII encodings, then put this at the top of your Python scripts
# It' ll fix them so that you can Unicode UTF-8 in your script without a problem
print "Hello các bạn"
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" to not touch this.'

#If we don't input # -*- coding: utf-8 -*- we get error message :
#SyntaxError: Non-ASCII character '\xc3' in file ex1.py on line 3, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

#Study Drill
#How to hide the line which we need to hide after run your script. We add # before the line. Python ignore detail after #

#Exercise 2: Comments and Pound Characters
#Typing this script, save file name : ex2.py

# A comment, this is so you can read your program later.
# anything after this # iss ignored by python.

#print " i could have code like this." #and the comment after is ignored

# you can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print " This will run."
print " Today #It rains"