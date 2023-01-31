# https://developers.arcgis.com/python/guide/accessing-and-creating-content/

import time
from arcgis.gis import GIS
from AGOL_Credentials import AGOLusername, AGOLpassword
import csv
import pandas as pd


URL = 'https://esrioceans.maps.arcgis.com/home'
gis = GIS(url=URL, username=AGOLusername, password=AGOLpassword)
me = gis.users.me
excel_report = r'C:\temp\GitHub List Services\user_report.xlsx'
me

# add_sheet is used to create sheet.
print(me)

import time
# convert Unix epoch time to local time
created_time = time.localtime(me.created/1000)
#print("Created: {}/{}/{}".format(created_time[0], created_time[1], created_time[2]))
#print(time.asctime(created_time))
last_accessed = time.localtime(me.lastLogin/1000)
#print("Last active: {}/{}/{}".format(last_accessed[0], last_accessed[1], last_accessed[2]))


quota = me.storageQuota
used = me.storageUsage
pc_usage = round((used / quota)*100, 2)
#print("Usage: " + str(pc_usage) + "%")

d = {'Username': [me], 'Storage Quota (GB)': [(me.storageQuota/1000000000)], "Storage Usage (GB)":[(me.storageUsage/1000000000)],'Usage %': [str(pc_usage) + "%"], 'User Created':[time.strftime("%d %b %Y",(created_time))], 'Last Log-in' :[time.strftime("%d %b %Y",(last_accessed))] }
df_user = pd.DataFrame(data=d)
df_user

user_groups = me.groups
print("Member of " + str(len(user_groups)) + " groups")
# groups are returned as a dictionary. Lets print the first dict as a sample
for item in user_groups:
     print(item)
print(user_groups)
df_group = pd.DataFrame(user_groups)

folder_list = me.folders
#for item in folder_list:
     #print(item)
df_folder = pd.DataFrame(folder_list)
# print(folder_list)

# search and list all feature layers in my contents
#user_item = open(r"C:\temp\GitHub List Services\user_items.csv", 'w', encoding='UTF8')
#writer = csv.writer(user_item)
search_result = gis.content.search(query='owner:'+ AGOLusername, item_type="Feature Layer",sort_field="numViews" ,sort_order="desc", max_items = 100)
#for item in search_result:
    #display(item)
    #last_udpated = time.localtime(item.modified / 1000)
    #print(f"{item.itemid} {item.title:<40} {time.asctime(last_udpated)} {item.numViews:<40} {item.type:25} {item.tags} {item.owner}")
    #print(item)
    #writer.writerow(f"{item.itemid} {item.title:<40} {time.asctime(last_udpated)} {item.numViews:<40} {item.type:25} {item.tags} {item.owner}")
#user_item.close()
df_item = pd.DataFrame(search_result)
tagList_list =[]

for tag in search_result:
    tagList_list.append(tag.tags)

all_tags = []
for tgs in tagList_list:
    for t in tgs:
        all_tags.append(t)

all_tags.sort()
unique_tags = set(all_tags)
sorted(unique_tags)
df_tags = pd.DataFrame(unique_tags)

# counting unique values
n = len(pd.unique(df['height']))

print("No.of.unique values :",
      n)

#print(df_item)

with pd.ExcelWriter(excel_report) as writer:
    df_user.to_excel(writer, sheet_name='User Info')
    df_group.to_excel(writer, sheet_name='Groups')
    df_folder.to_excel(writer, sheet_name='Folders')
    df_item.to_excel(writer, sheet_name='Top 100 Items')
    df_tags.to_excel(writer, sheet_name='Tags')