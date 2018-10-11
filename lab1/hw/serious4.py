from pymongo import MongoClient
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = MongoClient(uri)

customers = db["customers"]
db = client.get_default_database()
#customer_list = customers.find()

count_events = customers.find({"ref":"events"}).count()
count_wom = customers.find({"ref":"wom"}).count()
count_ads = customers.find({"ref":"ads"}).count()

print("Events: {}".format(count_events))
print("Word of mouth: {}".format(count_wom))
print("Advertisements: {}".format(count_ads))


labels = ["Events","Wom","Ads"]
sizes = [count_events,count_wom,count_ads]
explode = (0.1,0,0)
colors = ["yellow","red","blue"]

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%.1f%%', shadow=True)
 
plt.axis('equal')
plt.title("Even , Wom , Ads")
plt.show()

