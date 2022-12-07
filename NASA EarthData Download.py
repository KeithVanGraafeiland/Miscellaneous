# #!/usr/bin/python
# import requests # get the requsts library from https://github.com/requests/requests
#
# # overriding requests.Session.rebuild_auth to mantain headers when redirected
# class SessionWithHeaderRedirection(requests.Session):
#     AUTH_HOST = 'urs.earthdata.nasa.gov'
#     def __init__(self, username, password):
#         super().__init__()
#         self.auth = (username, password)
#
#    # Overrides from the library to keep headers when redirected to or from
#    # the NASA auth host.
#
#     def rebuild_auth(self, prepared_request, response):
#         headers = prepared_request.headers
#         url = prepared_request.url
#         if 'Authorization' in headers:
#             original_parsed = requests.utils.urlparse(response.request.url)
#             redirect_parsed = requests.utils.urlparse(url)
#             if (original_parsed.hostname != redirect_parsed.hostname) and \
#                     redirect_parsed.hostname != self.AUTH_HOST and \
#                     original_parsed.hostname != self.AUTH_HOST:
#                 del headers['Authorization']
#         return
# # create session with the user credentials that will be used to authenticate access to the data
# username = "USERNAME"
# password= "PASSWORD"
# session = SessionWithHeaderRedirection(username, password)
# # the url of the file we wish to retrieve
# url = "http://e4ftl01.cr.usgs.gov/MOLA/MYD17A3H.006/2009.01.01/MYD17A3H.A2009001.h12v05.006.2015198130546.hdf.xml"
#
# # extract the filename from the url to be used when saving the file
# filename = url[url.rfind('/')+1:]
#
# try:
#     # submit the request using the session
#     response = session.get(url, stream=True)
#     print(response.status_code)
#     # raise an exception in case of http errors
#     response.raise_for_status()
#     # save the file
#     with open(filename, 'wb') as fd:
#         for chunk in response.iter_content(chunk_size=1024*1024):
#             fd.write(chunk)
#
# except requests.exceptions.HTTPError as e:
#
#     # handle any errors here
#     print(e)

import requests # get the requsts library from https://github.com/requests/requests
# overriding requests.Session.rebuild_auth to mantain headers when redirected

class SessionWithHeaderRedirection(requests.Session):
    AUTH_HOST = 'urs.earthdata.nasa.gov'
    def __init__(self, username, password):
        super().__init__()
        self.auth = (username, password)

   # Overrides from the library to keep headers when redirected to or from
   # the NASA auth host.
    def rebuild_auth(self, prepared_request, response):
        headers = prepared_request.headers
        url = prepared_request.url
        if 'Authorization' in headers:
            original_parsed = requests.utils.urlparse(response.request.url)
            redirect_parsed = requests.utils.urlparse(url)
            if (original_parsed.hostname != redirect_parsed.hostname) and redirect_parsed.hostname != self.AUTH_HOST and original_parsed.hostname != self.AUTH_HOST:
                del headers['Authorization']
        return

# create session with the user credentials that will be used to authenticate access to the data
username = "xxxxx" #TODO replace with your Username
password= "xxxxx" #TODO Replace with your password
session = SessionWithHeaderRedirection(username, password)
# the url of the file we wish to retrieve

d_list = ["20000101",	"20000102",	"20000103",	"20000104",	"20000105",	"20000106",	"20000107",	"20000108",	"20000109",	"20000110",	"20000111",	"20000112",	"20000113",	"20000114",	"20000115",	"20000116",	"20000117",	"20000118",	"20000119",	"20000120",	"20000121",	"20000122",	"20000123",	"20000124",	"20000125",	"20000126",	"20000127",	"20000128",	"20000129",	"20000130",	"20000131"] #TODO Load list of dates to iterate through
output_path = "C:/temp/oscar/" # TODO Replace with the path on your computer to write the data to

for d in d_list:
    #url = "https://opendap.earthdata.nasa.gov/collections/C2098858642-POCLOUD/granules/oscar_currents_final_{date_string}.dap.nc4?dap4.ce=/lon[0:1:1439];/time[0:1:0];/vg[0:1:0][0:1:1439][0:1:718];/u[0:1:0][0:1:1439][0:1:718];/lat[0:1:718];/ug[0:1:0][0:1:1439][0:1:718];/v[0:1:0][0:1:1439][0:1:718]".format(date_string=d)
    url = "https://opendap.earthdata.nasa.gov/collections/C2098858642-POCLOUD/granules/oscar_currents_final_{date_string}.dap.nc4".format(date_string=d)
    # extract the filename from the url to be used when saving the file
    filename = url[url.rfind('/')+1:]
    print(filename)

    try:
        # submit the request using the session
        response = session.get(url, stream=True)
        print(response.status_code)
        # raise an exception in case of http errors
        response.raise_for_status()
        # save the file
        with open(output_path + filename, "wb") as file:
            print("Downloading File" + filename)
            file.write(response.content)
            print("Downloaded")
    except requests.exceptions.HTTPError as e:
        # handle any errors here
        print(e)