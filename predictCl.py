import arcpy
import pandas as pd
import numpy as np
from tqdm import *
import os
import gdaltokmz
import maskCloud as mc
from arcpy.sa import *
def predictClass(dataPath, modelPath, outputPath):

	#rasterarray = arcpy.RasterToNumPyArray(dataPath)
	masktype = 'Cloud'
	confidence = 'High'
	cummulative = 'false'	
	mc.mask_cloud(dataPath, masktype, confidence, cummulative, os.path.dirname(outputPath))

	rasterarrayband6 = arcpy.RasterToNumPyArray(dataPath + "/" + os.path.basename(dataPath) + "_B6.TIF")
	rasterarrayband5 = arcpy.RasterToNumPyArray(dataPath + "/" + os.path.basename(dataPath) + "_B5.TIF")
	rasterarrayband4 = arcpy.RasterToNumPyArray(dataPath + "/" + os.path.basename(dataPath) + "_B4.TIF")

	print("Change raster format to numpy array")
	data = np.array([rasterarrayband6.ravel(), rasterarrayband5.ravel(), rasterarrayband4.ravel()])
	data = data.transpose()

	import pandas as pd
	print("Change to dataframe format")
	columns = ['band1','band2', 'band3']
	df = pd.DataFrame(data, columns=columns)

	print("Split data to 20 chunks")
	df_arr = np.array_split(df, 20)

	kelasAll = []
	for i in range(len(df_arr)):
	    from sklearn.externals import joblib
	    clf = joblib.load(modelPath) 
	    print ("predicting data chunk-"+str(i))
	    kelas = clf.predict(df_arr[i])
	    dat = pd.DataFrame()
	    dat['kel'] = kelas
	    print ("mapping to integer class")
	    mymap = {'awan':1, 'air':2, 'tanah':3, 'vegetasi':4}
	    dat['kel'] = dat['kel'].map(mymap)

	    band1Array = dat['kel'].values
	    print ("extend to list")
	    kelasAll.extend(band1Array.tolist())

	del df_arr
	del clf
	del kelas
	del dat
	del band1Array
	del data

	print ("change list to np array")
	kelasAllArray = np.array(kelasAll, dtype=np.uint8)

	print ("reshaping np array")
	band1 = np.reshape(kelasAllArray, (-1, rasterarrayband6[0].size))
	band1 = band1.astype(np.uint8)

	raster = arcpy.Raster(dataPath + "/" + os.path.basename(dataPath) + "_B6.TIF")
	inputRaster = dataPath + "/" + os.path.basename(dataPath) + "_B6.TIF"

	spatialref = arcpy.Describe(inputRaster).spatialReference
	cellsize1  = raster.meanCellHeight
	cellsize2  = raster.meanCellWidth
	extent     = arcpy.Describe(inputRaster).Extent
	pnt        = arcpy.Point(extent.XMin,extent.YMin)

	del raster

	# save the raster
	print ("numpy array to raster ..")
	out_ras = arcpy.NumPyArrayToRaster(band1, pnt, cellsize1, cellsize2)
	#out_ras.save(outputPath)
	#arcpy.CheckOutExtension("Spatial")
	print ("define projection ..")
	arcpy.CopyRaster_management(out_ras, outputPath)
	arcpy.DefineProjection_management(outputPath, spatialref)


	del out_ras
	del kelasAllArray

	print("Masing Cloud")
	arcpy.CheckOutExtension("Spatial")
	mask = Raster(dataPath + '/mask_cloud_' + str(os.path.basename(dataPath)) + '.TIF')
	inRas = Raster(outputPath)
	outRas = Con((mask == 0), inRas, 1)

	outRas2 = SetNull(inRas == 1, inRas)
	outRas2.save(dataPath + "/" + os.path.basename(outputPath) + "_maskCloud.TIF")

	print("Masking with shp indonesia")
	arcpy.CheckOutExtension("Spatial")
	inMaskData = os.path.join(os.getcwd(), "INDONESIA_PROP.shp")
	outExtractByMask = ExtractByMask(outRas2, inMaskData)
	outExtractByMask.save(dataPath + "/" + os.path.basename(outputPath) + "_maskShp.TIF")
	# mask = Raster(out+'/mask_cloud_' + str(os.path.basename(path)) + '.TIF')
	# raster = Raster(outputPath)
	# out_mask = Con((mask == 0), raster, 1)
	# print ("convert raster to polygon")
	# fileNameOut = os.path.splitext(outputPath)[0]
	# fileNameOutPolygon = fileNameOut + ".shp"
	# print fileNameOut
	# print fileNameOutPolygon
	# arcpy.RasterToPolygon_conversion(outputPath, fileNameOutPolygon, "NO_SIMPLIFY", "VALUE")

	# print ("convert raster to kml")
	# fileNameOut = os.path.splitext(outputPath)[0]
	# fileNameOutKml = fileNameOut + ".kmz"
	# print fileNameOut
	# print fileNameOutKml
	# #arcpy.LayerToKML_conversion(outputPath, fileNameOutKml)
	# gdaltokmz.convert_gdal_to_kmz(outputPath, fileNameOutKml) 