x = "There are %d types of people." % 10 # 10 is inserted into 'x'
binary = 'binary' # set binary into a string 'binary' 
do_not = "don't" # set do_not into a sring 'don't'
y = "Those who know %s and those who %s" % (binary, do_not) # insert binary and don't into y

print x # prints x
print y # prints y

print "I said: %r." % x # prints x with appostrophes
print "I also said: '%s'." % y # prints y 

hilarious = False # set hilarious to false
joke_evaluation = "Isn't that joke funny?! %s" # set joke_evaluation into string but get the '%s'

print joke_evaluation % hilarious # print joke evaluation and use hilarious 

w = "This is  the left side of..." # set w 
e = "a string with a right side." # set e 

print w + e # print w and e together