pip install wget
import wget

url = 'https://coast.noaa.gov/htdata/Inundation/SLR/SLRdata/AL/AL_dem.zip'
#filename = url.split('/')[-1:]
print(filename)
# context = ssl._create_unverified_context()
filename = wget.download(url)
filename
# open('AL_dem.zip', 'wb').write(r.content)