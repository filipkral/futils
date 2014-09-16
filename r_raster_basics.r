# This is how you can get going with raster data handling in R

# The Swiss Army knife for spatial infromation
require(rgdal)

# Large raster handling and analysis
require(raster)

# You can even read and write NetCDF files if you really want to
require(ncdf)

# Work with projections like pro
require(proj4)


# Open
r <- raster("C:\\temp\\eu_dir_15s_sample.tif")

# you can check various properties like
# projection, resolution, dimensions, etc.
print(r)
# or access individual properties
projection(r)
res(r)
nrow(r)
ncol(r)
dim(r)
bbox(r)
xmax(r)
filename(r)
plot(r)
vals <- getValues(r, 100:110, 150:180)

# create a new raster from a matrix
m<-raster(matrix(runif(100000), 1000, 1000))
# defining projection is a breeze with proj4 and EPSG codes
# WGS84 is 4326, British National Grid is 27700,... (see http://epsg.io)
projection(m)<-CRS("+init=EPSG:27700")

# rgdal allows you to save in variety of formats, just a basic geotiff example:
rtf <- writeRaster(m, filename="c:\\temp\\my.tif", format="GTiff", overwrite=TRUE)

# if you have netcdf library and ncdf package, you can go wild and save it as NetCDF
rnc <- writeRaster(m, filename="c:\\temp\\yours.nc", format="CDF", overwrite=TRUE)   

# You can do various calculations and analyses with rasters too.
# See way more at http://cran.r-project.org/web/packages/raster/vignettes/Raster.pdf

