import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\ProProject\ChlorA P90\Deviation_Anomaly\09_Anomaly"
import csv

with open ('D:\ProProject\ChlorA P90\Deviation_Anomaly\p90_Monthly_Raster\Anomaly_Date_and_p90_Values.csv','r') as csv_file:
    reader =csv.reader(csv_file)
    next(reader) # skip first row
    for row in reader:
        anomaly_raster = row[0]
        p90_value = float(row[1])
        p90_raster = r"D:\ProProject\ChlorA P90\Deviation_Anomaly\p90_Monthly_Raster" + "\\" + row[2]
        out_raster = arcpy.sa.Times(anomaly_raster, p90_value);
        out_raster.save(p90_raster)
        print(p90_raster + " done")

