# 1. Connect to database
from pymongo import MongoClient
from matplotlib import pyplot
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e' # DÙng uri để connect
client = MongoClient(uri)
db = client.get_default_database()

#2. Select collection
customers = db["customers"]

#3. Read với điều kiện là events, ads, wom # Tim kiem voi cac dieu kien 
# events
cond1 = {"ref": 'events'}
customers_list1 = customers.find(cond1)
count1 = 0
for items in customers_list1:
    count1 += 1
print('Số người dự events',count1)

#Ads
cond2 = {"ref":"ads"}
customers_list2 = customers.find(cond2)
count2 = 0
for item in customers_list2:
    count2 += 1
print('Số người dự ads',count2)

#wom
cond3 = {"ref":'wom'}
customers_list3 = customers.find(cond3)
count3 = 0
for item in customers_list3:
    count3 += 1
print('Số người dự wom',count3)

#---------------------------------------------------------
#Ve do thi
# Prepare data
people_counts = [count1,count2,count3]
# Prepare lables
event_name = ['events','ads','wom']
# Draw pie chart
pyplot.pie(people_counts, labels = event_name,autopct="%.1f%%",shadow = True,explode = [0,0,0.2])
pyplot.axis('equal')
pyplot.title('Percentage')
#Show
pyplot.show()