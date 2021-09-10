import ftplib
import shutil
from copernicus_credentials import username, password

#Downloads Chlorophyll netCDF files from the NESDIS STAR FTP Site
ftp = ftplib.FTP('ftp://nrt.cmems-du.eu')
ftp.login(user = username, passwd = password)
ftp.cwd('/Core/GLOBAL_ANALYSIS_FORECAST_WAV_001_027/global-analysis-forecast-wav-001-027/2021/09/')
filenames = ftp.nlst()
fileloc = 'C:/temp'
#fullurl = ftp://nrt.cmems-du.eu/Core/GLOBAL_ANALYSIS_FORECAST_WAV_001_027/global-analysis-forecast-wav-001-027/2021/08/

for filename in filenames:

    with open( filename, 'wb' ) as file :
        print ("Downloading file .......... ", filename)
        ftp.retrbinary('RETR %s' % filename, file.write, 1024)
        file.close()
        shutil.move(filename, fileloc)
        print('Successfully downloaded.......... ', filename)
print("Done Downloading!")
ftp.quit()