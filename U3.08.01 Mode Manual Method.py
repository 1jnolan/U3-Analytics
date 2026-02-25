#two lists with the data
colourCounts=[4,2,1]
colourNames=['red', 'blue', 'green']

maxFreq= max(colourCounts) #finds the biggest number in the list.
maxFreqLocation=colourCounts.index(maxFreq) #finds the index where this number is stored
mode=colourNames[maxFreqLocation]#find the item in the colourNames list with the matching location
print("The Mode of this data is:\t", mode)
