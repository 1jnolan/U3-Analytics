import matplotlib.pyplot as plt

numBS=[1,2.5,4,3,2.5,2] #a list with the data
plt.plot(numBS, "rs") #Change the style using the second argument

plt.title("Brothers and Sisters") #Add your title
plt.xlabel("List Index") #Add the x label
plt.ylabel("Number of Brothers & Sisters") #Add the y label
plt.show() #plot the graph
