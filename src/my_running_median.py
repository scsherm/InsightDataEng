#Load modules
import os
import copy
import numpy as np
import glob
import sys

median, numline, lines = [], [], [] #Empty lists
os.chdir(sys.argv[1]) #Change to second directory of current

for txtfile in glob.glob("*.txt"): #For all text files
    with open(txtfile) as file:
        for x in file:
            lines = lines + x.splitlines() #List of each line
            
for item in lines: #For each item of the variable lines
    c = len(item.split()) #Count the number of words
    numline.append(c) #Add that value at the end of variable b

fxind = len(numline) + 1 #To fix indexing
for i in range(fxind): 
    if i >= 1:
        med = np.median(numline[0:i]) 
        median.append(med)

os.chdir("..") #Move back directory
newfile = open(sys.argv[2], "w") #Open third directory and write newfile

for val in median:
    newfile.write("%.1f\n" % val) #For each value print and go to next line
newfile.close()

    

