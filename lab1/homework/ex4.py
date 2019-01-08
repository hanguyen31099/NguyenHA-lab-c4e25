from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()
customers = db["customers"]

print("Total:",db.customers.count_documents({}))

events = db.customers.count_documents(({"ref": "events"}))
print("Events:", events)

ads = db.customers.count_documents(({"ref": "ads"}))
print("Ads:", ads)

wom = db.customers.count_documents(({"ref": "wom"}))
print("WOM:", wom)

client.close()

from matplotlib import pyplot
machine_count=[events,wom,ads]
machine_name=["events","wom","ads"]
pyplot.pie(machine_count,labels=machine_name,autopct='%.1f%%',shadow=True,startangle=90)
pyplot.axis("equal")
pyplot.title("Reference")
pyplot.show()


