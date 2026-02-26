import matplotlib.pyplot as plt

numBS=[1,2.5,4,3,2.5,2] #a list with the data
ages=[17, 18, 16, 18, 17, 17]
names=["Joe Bloggs", "Mary Murphy", "Claire Whelan", "Mike Fahey", "Gillian Marks", "Arya Quille"]

plt.plot(names, numBS) #plot line graph of the mumber of bros&sisters with the names
plt.plot(ages) #another set of data put onto the graph

plt.xlabel("Student")
plt.ylabel("Num Brothers & Sisters")
plt.title("Brothers and Sisters") #Add your title
plt.show() #plot the graph
