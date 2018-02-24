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

#Exercise 3: Numbers and Math
#Print into screen this sentence for notify news "I will now count my chickens:"
print "I will now count my chickens:"

#Print amount of Hens and Roosters 
print "Hens",25+30/6 # print text in "" and result of operation -> Hens 30
print "Roosters", 100-25*3%4 

#Print a sentence to screen
print "Now I will count the eggs:"

# % modulo function 4%2=2, 
print 3+2+1-5+4%2-1/4+6

print "Is it true that 3+2<5-7?"

print 3+2 < 5-7

print "What is 3+2?", 3+2
print "What is 5-7?",5-7

#7%4=3 Modulo function
print 7%4
print "What is 17%4", 17%4
print "What is 1/4?", 1/4 #if number1, number2 are interger type, result is interger
print "What is 1.0/4?", 1.0/4 # if one of all is decimal number, result is decimal number

print "Oh, that's why it's False."

print "how about some more."

# Compare 2 numbers, if 5>-2, get TRUE, if 5 <=-2 get FALSE
print "Is it greater?",5>-2
print "Is it greater or equal?", 5>=-2
print "Is it less or equal?", 5<=-2


