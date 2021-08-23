from ftplib import FTP_TLS as FTP
import os
from pprint import pprint

ftpname = 'ftp.cpc.ncep.noaa.gov'
with FTP(ftpname,'anonymous', 'anonymous@') as ftp:
    files = []
    mostrecent = {}
    for f in ftp.nlst('/GIS/droughtlook/'):
         split1 = (os.path.split(f)[-1].split("_",1))[0].lower()
         mostrecent[split1]="https://ftp.cpc.ncep.noaa.gov" + f
pprint(mostrecent)
mdoURL = mostrecent["mdo"]
sdoURL = mostrecent["sdo"]
doURL = mostrecent["do"]
print(mdoURL + "\n", sdoURL+ "\n", doURL)