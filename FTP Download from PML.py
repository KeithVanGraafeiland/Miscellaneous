import ftplib
import shutil

#Downloads Chlorophyll netCDF files from the Plymouth Marine Lab FTP site
ftp = ftplib.FTP('ftp.rsg.pml.ac.uk')
ftp.login(user='oc-cci-data', passwd = 'ELaiWai8ae')
suburl = '/occci-v4.2/geographic/netcdf/monthly/chlor_a/'
yeardownload = '2015'
ftp.cwd(suburl + yeardownload)
filenames = ftp.nlst()
fileloc = 'E:/Data/ChlorA/PML/4.2'
#fullurl = 'ftp://ftp.rsg.pml.ac.uk/occci-v4.2/geographic/netcdf/monthly/chlor_a/'

for filename in filenames:

    with open( filename, 'wb' ) as file :
        print ("Downloading file .......... ", filename)
        ftp.retrbinary('RETR %s' % filename, file.write, 1024)
        file.close()
        shutil.move(filename, fileloc)
        print('Successfully downloaded.......... ', filename)
print("Done Downloading!")
ftp.quit()