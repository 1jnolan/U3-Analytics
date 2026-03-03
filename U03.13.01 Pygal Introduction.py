import pygal #you may need to install this module if it is the 1st time you have used it.

boys_chart = pygal.Bar(#tell pygal to make a bar chart
    title="Most Popular Boys Names in Ireland - 2024", #give it a title
    x_title="Name", #give the x axis a title
        
)

boys_names = ["Jack", "Noah", "Rían", "Cillian", "James"] #a list of names
boys_counts = [490, 486, 432, 352, 336] #the number of boys with those names

boys_chart.x_labels = boys_names #place the names of the boys on the x axis labels
boys_chart.add("Boys", boys_counts) #plot the Boys on the chart
boys_chart.render_to_file("ireland_boys_names_2024.svg") #render the file. It will save to where you save your python file and you can open the file with your browser
