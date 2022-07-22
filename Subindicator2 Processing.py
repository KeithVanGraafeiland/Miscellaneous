import arcpy
arcpy.env.overwriteOutput = True

arcpy.env.workspace = "E:/ChlorA_Sub2/"
filelist = arcpy.ListFiles("V2020001*.tif")
eez_raster_dissolve = "D:/ProProject/ChlorA P90/Subindicator2/TIF/EEZ_Raster_Dissolve.tif"

for name in filelist:
    in_raster = name
    name_split = name.split(".")[0]
    times_raster = name_split + "_01times.tif"
    times_raster_full = "E:/ChlorA_Sub2/" + times_raster
    zStats_table = name_split + "_02zStats"
    zStats_table_full = "E:/ChlorA_Sub2/" + zStats_table
    print("Processing " + name_split)
    print(zStats_table_full)
    # with arcpy.EnvManager(snapRaster=eez_raster_dissolve, cellSize=eez_raster_dissolve,
    #                       mask=eez_raster_dissolve):
    #     out_raster = arcpy.sa.Times(in_raster, eez_raster_dissolve);
    #     out_raster.save(times_raster)
    # arcpy.ia.ZonalStatisticsAsTable(eez_raster_dissolve, "Value", times_raster_full,
    #                                 zStats_table_full, "DATA", "ALL",
    #                                 "CURRENT_SLICE", [90, 95, 99], "AUTO_DETECT", "ARITHMETIC", 360)

    # arcpy.ia.ZonalStatisticsAsTable(eez_raster_dissolve, "Value", "E:/ChlorA_Sub2/V2018001_D1_WW00_chlorapdif_con.tif",
    #                                 zStats_table, "DATA", "ALL",
    #                                 "CURRENT_SLICE", [90, 95, 99], "AUTO_DETECT", "ARITHMETIC", 360)
    # arcpy.ia.ZonalStatisticsAsTable("EEZ_Raster_Dissolve.tif", "Value", "V2018001_D1_WW00_chlorapdif_con.tif",
    #                                 r"D:\ProProject\ChlorA P90\Subindicator2\Processing\test", "DATA", "ALL",
    #                                 "CURRENT_SLICE", [90, 95, 99], "AUTO_DETECT", "ARITHMETIC", 360)
    print("Done Processing " + name_split)
