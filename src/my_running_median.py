#Load modules
import os
import numpy as np
import glob
import sys

median, numline, lines = [], [], [] #Create 3 Empty lists
os.chdir(sys.argv[1]) #Change directory to location of 2nd arg in run.sh (wc_input) 

for txtfile in glob.glob("*.txt"): #For all text files
    with open(txtfile) as file:
        for echline in file:
            lines = lines + echline.splitlines() #List each line
            
for item in lines: #For each item of the variable lines
    c = len(item.split()) #Count the number of words
    numline.append(c) #Add that value at the end of variable b

fxind = len(numline) + 1 #To fix indexing
for i in range(fxind): 
    if i >= 1:
        med = np.median(numline[0:i]) 
        median.append(med)

os.chdir("..") #Change directory for sys.argv[2]
newfile = open(sys.argv[2], "w") #Open a new file for write in run.sh arg 3

for val in median:
    newfile.write("%.1f\n" % val) #For each value print (1 sigfig) and go to next line
newfile.close() #Close file

    

