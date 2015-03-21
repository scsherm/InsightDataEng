#Load modules
import os
import numpy as np
import glob
import sys

median, numline, lines = [], [], [] #Create 3 Empty lists
os.chdir(sys.argv[1]) #Change directory to location of 2nd arg in run.sh (wc_input) 

for txtfile in glob.glob("*.txt"): #For all text files
    with open(txtfile) as file:
        for echline in file: #For each line
            lines = lines + echline.splitlines() #Store txt line as str in lines
            
for item in lines: #For each str in lines variable
    c = len(item.split()) #Count the number of words
    numline.append(c) #Add integer to numline list

fxind = len(numline) + 1 #To fix indexing
for i in range(fxind): #For i from 0 to length of lines +1
    if i >= 1: #Skip 0 so indexing starts at 0:1
        med = np.median(numline[0:i]) #Median of all lines up to iteration 
        median.append(med) #Add median value to median list

os.chdir("..") #Change directory for sys.argv[2]
newfile = open(sys.argv[2], "w") #Open a new file for write in run.sh arg 3
for val in median:
    newfile.write("%.1f\n" % val) #For each value print (1 sigfig) and go to next line
newfile.close() #Close file