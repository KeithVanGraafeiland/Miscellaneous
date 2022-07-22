import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\keit8223\Documents\ArcGIS\Projects\USCG Light List\input\v1d01WeeklyChanges.xml')
root = tree.getroot()

print(root)
