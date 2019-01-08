
from matplotlib import pyplot

#1 prepare data
machine_count=[18,4,2]
#2 prepare table
machine_name=["PC","Mac","linus"]
#3 draw pie
pyplot.pie(machine_count,labels=machine_name,autopct='%1.1f%%',shadow=True, startangle=90,explode=[0,0.1,0])
pyplot.axis("equal")
#4 show
pyplot.show()