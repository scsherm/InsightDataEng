#Load modules
import re
import os
import copy
import numpy as np
import glob
import sys
count, wd, words = [], [], []
os.chdir(sys.argv[1]) #Change to second directory of current

for txtfile in glob.glob("*.txt"): #For all text files
    with open(txtfile) as file:
        for word in file:
            nospchar = re.sub('[^a-zA-Z]+', ' ', word).strip() #Remove non-alphanumeric
            lwrcase = nospchar.lower() #Make Lowercase
            words = words + lwrcase.split() #List of each word
uniqueset = set(words) #Get unique values by turning list into set
uniquelist = list(uniqueset) #Turn unique values back to list
for eachwd in uniquelist:
    count.append(words.count(eachwd))
    wd.append(eachwd)
zwdcount = zip(wd, count) #Combine count and wd 
wdcount = list(zwdcount) #Turn back to list if Py3
#print wdcount[0]

os.chdir("..") #Move back directory
newfile = open(sys.argv[2], "w") #Open third directory and write newfile

for (word, val) in wdcount:
    newfile.write("%s:  %s\n" % (word, val)) #For each word and value print and go to next line
newfile.close()
