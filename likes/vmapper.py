# FOR EACH VIDEO, COUNT COMMENTS.
# RAW DATA HAS 1 COMMENT PER LINE.
# 
# STEP 1. MAP each line, output video id and 1 for this comment

# open data.csv for reading as a file stream named i
# open m.csv for writing as a file stream named o
i = open("data.csv","r") 
# o = open("m.csv", "w")
o = open("m.csv", "w")

# for each line in your input file stream
for line in i:
    

  # strip the line, split it by the delimiter into a list named 'data'
    line = line.strip()
    data = line.split(",")

    # if len(data) is equal to 4 (remember the colon)
    if len(data) ==4:

    # assign data to four named variables
      videoID = data[0]
      text = data[1]
      likes = data[2]
      replies= data[3]
    
    # use o.write to output the id comma 1
      o.write("{0},{1}\n".format(videoID, 1))
      # print("{0},{1}\n".format(id, 1))

# close your file streams
i.close()
o.close()
