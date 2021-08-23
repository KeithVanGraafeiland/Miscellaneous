import arcgis
import arcpy
import pandas
from arcgis.gis import GIS
from arcgis.geoanalytics import summarize_data
from arcgis.mapping import WebMap
from pprint import pprint

arcpy.GetInstallInfo()['Version']

item = gis.content.get("f75efa43b3b0403097121cee6f6a8877")
item

tracks = item.layers[1]
tracks

for field in tracks.properties.fields:
    print(field['name'], end="\n")

Stakeholder_item = gis.content.get("a215b571448e41d78ba2e9b7a20daaa1")
Stakeholder_item

Stakeholders = Stakeholder_item.layers[0]
Stakeholders