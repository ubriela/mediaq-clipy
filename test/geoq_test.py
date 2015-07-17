__author__ = 'ubriela'

import SwaggerMediaq as sm

# Create geoq client api
geoq = sm.GeoqApi(sm.ApiClient("http://mediaq.usc.edu/MediaQ_MVC_V3/api"))

# Returns a set of video locations in GEOJSON format (small sample data)
print geoq.sample_videos()

# Returns a set of video frames (of a particular video) in GEOJSON format (small sample data)
print geoq.sample_fovs()

# Create geoq client with API key 
# Replace KEY_VALUE by actual one
geoq = sm.GeoqApi(sm.ApiClient("http://mediaq.usc.edu/MediaQ_MVC_V3/api", "X-API-KEY", "KEY_VALUE"))

# Returns a set of video locations
print geoq.rectangle_query(swlat=34.019972,swlng=-118.291588,nelat=34.021111,nelng=-118.287125)

# Returns a set of video frames
print geoq.video_metadata("jca1ptaaiz83_2015_1_16_Videotake_1421449431727.mp4")
