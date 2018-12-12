# FOR EACH VIDEO, COUNT COMMENTS.
# MAPPER OUTPUT HAS ID, 1
# 
# STEP 2. Mimic sort-and-shuffle in MR

# open m.csv for reading as a file stream named m
# open s.csv for writing as a file stream named s
m = open( "m.csv", "r")
s = open("s.csv", "w")


# use readlines method of the file stream object to create a list called lines
lines = m.readlines()


# call the list sort method on your lines to sort in place (do not reassign to another variable)
lines.sort()

# for every line in lines (remember the colon)
for line in lines:
  # use s.write to output the line
	s.write(line)

# close file streams
m.close()
s.close()
