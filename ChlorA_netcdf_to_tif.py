import arcpy
arcpy.env.workspace = r"C:\Users\keit8223\Documents\ArcGIS\Projects\CHL_A SDG\Data\OceanColor\netcdf\4.0\Monthly"
filelist = arcpy.ListFiles("*.nc")
arcpy.env.overwriteOutput = True

for name in filelist:
    ras = "in_memory/ras"
    print("Processing: " + name)
    arcpy.md.MakeNetCDFRasterLayer(name, "chlor_a", "lon", "lat", ras, '', '', "BY_VALUE", "CENTER")
    arcpy.Raster( ras).save( name.split("-")[-2] + ".tif")

print("Done")
