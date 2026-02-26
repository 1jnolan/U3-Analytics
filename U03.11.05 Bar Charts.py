import matplotlib.pyplot as plt

numBS=[1,2.5,4,3,2.5,2] #a list with the data
names=["Joe Bloggs", "Mary Murphy", "Claire Whelan", "Mike Fahey", "Gillian Marks", "Arya Quille"]

plt.bar(names, numBS,) #change the code to plot using a barchart

plt.title("Brothers and Sisters") #Add your title
plt.xlabel("Student") #Add the x label
plt.ylabel("Number of Brothers & Sisters") #Add the y label
plt.show() #plot the graph
