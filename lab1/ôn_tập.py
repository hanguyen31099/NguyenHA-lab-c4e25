uri="mongodb://admin:admin1@ds133360.mlab.com:33360/c4e25"
# conect to data base (mlab)
from pymongo import MongoClient
client = MongoClient(uri)
# Getting a Database
db = client.get_database()
# Getting a Collection
customers = db['customers']
ev = 0
ad = 0
wom = 0
for customer in customers.find():
    if customer['ref'] == 'events':
        ev += 1
    elif customer['ref'] == 'wom':
        wom += 1
    else:
        ad += 1
    # print(customer['ref'])

import matplotlib.pyplot as plt

# Data to plot
labels = 'Events', 'Advertisements', 'Word of Mouth'
sizes = [ev, ad, wom]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0.1, 0)  # explode 1st slice
for i in range(3):
    print('Number of customer accquire by ',labels[i],': ',sizes[i],sep='')
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()