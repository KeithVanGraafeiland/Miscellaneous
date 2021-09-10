from osgeo import gdal

hdfFile = r'C:\Users\keit8223\Documents\ArcGIS\Projects\HDF\npp_sabpm_202001.hdf'
TIF = r'C:\Users\keit8223\Documents\ArcGIS\Projects\HDF\test.tif'

info = gdal.Info(hdfFile, deserialize=True)
print(info)

raster = gdal.Open(hdfFile)
gt =raster.GetGeoTransform()
print(gt)
pixelSizeX = gt[1]
pixelSizeY = gt[5]
print(pixelSizeX)
print(pixelSizeY)

ds_out = gdal.Warp(TIF, hdfFile,
                   format = 'GTiff',
                   dstSRS = 'EPSG:4236',
                   outputBounds = [-180, -90, 180, 90],
                   outputBoundsSRS = 'EPSG:4326')
# if you want to check the result
print(gdal.Info(ds_out))