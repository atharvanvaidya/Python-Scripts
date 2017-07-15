#Requires an input.txt file which contains a Paragraph
from random import *

ip = open("input.txt", 'r')
tempIp = ip.read()
ip.close()
op = open("output.txt", 'w')
for line in tempIp.splitlines():                            #Traverse a Line
    tempLine = line.split()
    for word in range(0,len(tempLine)):                     #Traverse a Word from the Line
        if len(tempLine[word]) <= 3:                        #If Length of Word is <= 3
            op.write(tempLine[word])
            op.write(" ")
        else:
            tempList = list(tempLine[word])
            op.write(tempList[0])                           #Write First Character
            temp = sample(tempList[1:-1], len(tempList)-2)
            str1 = ''.join(temp)
            op.write(str1)                                  #Write Middle Jumbled Characters
            op.write(tempList[len(tempList)-1])             #Write Last Character
            op.write(" ")
    op.write('\n')
