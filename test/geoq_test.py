__author__ = 'ubriela'

import SwaggerMediaq as sm

# Create client
geoq = sm.GeoqApi(sm.ApiClient("http://mediaq.usc.edu/MediaQ_MVC_V3/api"))

# Returns a set of video locations
print geoq.metadata_video()

# Returns a set of video frames
#print geoq.metadata_fov("jca1ptaaiz83_2015_1_16_Videotake_1421449431727.mp4")