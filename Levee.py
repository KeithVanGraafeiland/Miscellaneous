import requests

url = 'https://levees.sec.usace.army.mil/api-local/download/dataset/shapefile.zip?full=true'
myobj = [1905000123]

x = requests.post(url, json = myobj)

#print the response text (the content of the requested file):

print(x.text)
