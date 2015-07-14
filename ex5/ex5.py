# -*- coding: utf-8 -*-

name = 'Daniel Mendoza'
age = 22
height = 74.0
weight = 160.0
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

in_centimeters = height * 2.54
in_kilograms = weight * 0.4536

print "Lets talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy" % weight
print "Actually he's not that heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)

print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)
print "My height in centimeters is %.2fcm" % in_centimeters
print "My weight in in kilograms is %.2fkg" % in_kilograms 

# d - signed integer decimal
# i - signed integer decimal
# o - signed octal value
# u - obsolete type - it is idetical to d
# x - signed hexadecimal (lowercase)
# X - signed hexadecimal (uppercase)
# e - floating point exponential form (lowercase)
# E - floating point exponential form (uppercase)
# g - floating point format (lowercase)
# G - floating point format (uppercase)
# c - single character 
# r - string (converts any Python object using repr())
# s - string (converts any Python object using str())
# % - no arguement is converted, results in a '%' character  in the result