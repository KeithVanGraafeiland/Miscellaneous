import arcpy
arcpy.management.Clip(r"F:\ArcGIS Pro Projects VOL3\NOAA_SLR\CRF\US_CONUS_GMSL_Scenarios.crf", "-179.231101251 -14.601806016 179.859665729 71.4397857070001",
                      r"C:\temp\US_CONUS_GMSL_Scenarios_Clip_Miami_Dade.crf", "#", "256", "NONE",
                      "NO_MAINTAIN_EXTENT")
