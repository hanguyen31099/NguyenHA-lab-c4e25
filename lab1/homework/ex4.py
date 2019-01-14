from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_database()

customers = db["customers"]

#use function of data base on documnets mogodb
print("Total:",db.customers.count_documents({}))

events = db.customers.count_documents(({"ref": "events"}))
print("Events:", events)

ads = db.customers.count_documents(({"ref": "ads"}))
print("Ads:", ads)

wom = db.customers.count_documents(({"ref": "wom"}))
print("WOM:", wom)
#use loop and function find()
events=0
wom=0
ads=0
for customer in customers.find():
    if customer['ref'] == 'events':
        events += 1
    elif customer['ref'] == 'wom':
        wom += 1
    else:
        ads += 1

client.close()

#paint pie
from matplotlib import pyplot
machine_count=[events,wom,ads]
machine_name=["events","wom","ads"]
colors=['yellowgreen','gold','lightcoral']
explode=[0,0,0.1]
pyplot.pie(machine_count,labels=machine_name,autopct='%.1f%%',shadow=True,startangle=90,colors=colors,explode=explode)
pyplot.axis("equal")
pyplot.title("Reference")
pyplot.show()


