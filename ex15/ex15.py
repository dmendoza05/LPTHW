from sys import argv # 

script, filename = argv

txt = open(filename)
# we are taking the filename and using the function OPEN to open the file

print "Here's your file %r:" % filename # printing the filename
print txt.read() # here we are reading the contents of the txt file.

print "Type the filename again:" # we ask user to input the filename again
file_again = raw_input("> ") 

txt_again = open(file_again) # open the file 

print txt_again.read() # read the file
 
t xt.close # closes the file
txt_again.close