from suds.client import Client

soapClient = Client("http://cdmo.baruch.sc.edu/webservices2/requests.cfc?wsdl", timeout=90, retxml=True)

#Get the station codes SOAP request example.
station_codes = soapClient.service.exportStationCodesXML()
print(station_codes)

#Get all parameters from the station NIWOLMET for the date range of 2014-12-30 to 2014-12-31
params = soapClient.service.exportAllParamsDateRangeXML('niwolmet', '2014-12-30', '2014-12-31', '*')
print(params)