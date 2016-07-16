#! python3

# readngCSV.py - How to read a comma-separated-values file


import csv
import pprint as pp

print("Opening csv file...")
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

pp.pprint(exampleData)
#exampleFile.close()
print("Done.")

#---------------------------------------------------------------
# Reading Data from Reader Objects in a for loop

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

exampleFile.close()
print("Done 2.")    

#---------------------------------------------------------------
# Writer Objects

































