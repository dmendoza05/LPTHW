formatter = '%s %s %s %s'

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing", # double quotes marks the beggining and end of the string and the single quote inside is just an apostrophe as a string
    "So I said goodnight." 
  )