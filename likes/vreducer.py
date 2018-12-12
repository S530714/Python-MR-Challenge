# FOR EACH VIDEO, COUNT COMMENTS.
# SORTED DATA HAS 1 COMMENT PER LINE, ALL VIDEOIDS TOGETHER
# 
# STEP 3. REDUCE videoID and counts by summing the counts into 1 record per video

# open s.csv for reading as a file stream named s
# open r.csv for writing as a file stream named r
s = open("s.csv", "r")
r = open("r.csv", "w")

# instantiating variables for later use
oldKey = None
thisKey = ""
thisValue = 0
max = 0
maxvalue = 0

# output column headers
r.write('videoID,comments\n')

# for loop to iterate through each line
for line in s:
    # seperates each value with a tab
    data = line.strip().split(',')
    # if statement to ignore a bad input line
    if len(data) != 2:
        continue
    # read in our variables and set them equal to data
    videoID, comments = data

    # make sure videoID is not null
    if videoID != thisKey:
        if thisKey:
            # output the last key value pair result
            r.write(thisKey + '\t' + str(thisValue) + '\n')
            print(thisKey + '\t' + str(thisValue) + '\n')
            thisValue += int(comments)
            if thisValue > max:
              max = thisValue
              maxvalue = thisValue
              r.write(thisKey + '\t' + str(max) +'\n')
              print(thisKey + '\t' + str(max) +'\n')

        # start over when changing keys
        thisKey = videoID
        thisValue = 0
        # max = comments

    # apply the sum function
    thisValue += int(comments)
    if thisValue > max:
      max = thisValue

# output the final key and value
r.write(thisKey + '\t' + str(thisValue) + '\n')
print(thisKey + '\t' + str(thisValue) + '\n')
r.write(thisKey + '\t' + str(max) +'\n')
print(thisKey + '\t' + str(max) +'\n')

# close the files
s.close()
r.close()
