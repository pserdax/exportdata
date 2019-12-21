import requests
import csv
from datetime import datetime



#starttime = datetime(2019, 12, 1)
#endtime = datetime.datetime.now()

r = requests.get('https://www.popads.net/api/<API key>').json()

c=csv.writer(open("sonky.csv", "w"), lineterminator = '\n')

for item in r['campaigns']:
   
    c.writerow([item ['id'], item['status'], item['aux_status'], item['group_id'], item['name'], item['budget'], item['url'], item['created']])
    
  