#Load modules
import re
import os
import glob
import sys

count, wd, words = [], [], [] #Create 3 Empty lists
os.chdir(sys.argv[1]) #Change directory to location of 2nd arg in run.sh (wc_input) 

for txtfile in glob.glob("*.txt"): #For loop of all text files
    with open(txtfile) as file:
        for word in file:
            nospchar = re.sub('[^a-zA-Z]+', ' ', word).strip() #Remove non-alphanumeric characters
            lwrcase = nospchar.lower() #Turn to lowercase
            words = words + lwrcase.split() #Add to list of words
            
uniqueset = set(words) #Get unique values by turning list into set
uniquelist = list(uniqueset) #Turn unique values back to list

for eachwd in uniquelist: #For each word in the list of uniques
    count.append(words.count(eachwd)) #Count number of words in original list; add integer to count list
    wd.append(eachwd) #Add word to wd list  
    
zwdcount = zip(wd, count) #Combine count and wd as tuples
wdcount = list(zwdcount) #Turn back to list 

os.chdir("..") #Change directory for sys.argv[2]
newfile = open(sys.argv[2], "w") #Open a new file for write in run.sh arg 3
for (word, val) in wdcount: #For each word in the final list
    newfile.write("%s:  %s\n" % (word, val)) #Print word and value, go to next line
newfile.close() #Close file