# \\ - backslash
# \' - single-quote
# \" - double-quote
# \a - ASCII Bell
# \b - ASCII Backspace
# \f - ASCII Formfeed
# \n - ASCII Linefeed
# \N(name) - Character named name in the Unicode database (Unicode only)
# \r - Carriage return
# \t - Horizontal tab
# \u - Character with 16-bit hex value xxxx
# \U - Character with 32-bit hex value xxxxxxxx
# \v - ASCII with vertical tab
# \ooo - Character with octal value ooo
# \xhh - Character with hex value hh

tabbby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabbby_cat
print persian_cat
print backslash_cat
print fat_cat

# STUDY DRILLS

drill_one = '''
drill drill drills:
\t> one
\t> two's\n\t> "three's"
\t> "four"\\
\t> five\b\n\t> six \a
\t\f> seven
\v> eight

'''

print "drillz %r" % drill_one # the escape sequences didn't work
print "drillz %s" % drill_one # escape sequences worked
