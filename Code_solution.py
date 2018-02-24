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

#Excercise 4: Variables And Names
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/ cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#Exercise 5: More Variables and Printing

my_name = 'Zed A.Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = "White"
my_hair = 'Brown'

print " Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height +  my_weight)

#Exercise 6: String and text

x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." %x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
w = "This is a left side of ..."
e = "a string with a right side."

print w + e

#Exercise 7: More sprinting

print " Mary had a little lamb."
print "It's fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." *10 #what's that do ?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch that comma at the end. try removing it to see that happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12


