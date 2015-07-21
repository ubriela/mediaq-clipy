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
geoq = sm.GeoqApi(sm.ApiClient("http://mediaq.usc.edu/MediaQ_MVC_V3/api", "X-API-KEY", "8b51UFM2SlBltx3s6864eUO1zSoefeK5"))

# Returns a set of video locations
print geoq.rectangle_query(swlat=34.019972,swlng=-118.291588,nelat=34.021111,nelng=-118.287125)

# Returns a set of video locations that are captured within a time interval (from -> to)
print geoq.rectangle_query(swlat=34.019972,swlng=-118.291588,nelat=34.021111,nelng=-118.287125,startdate='2015-01-01 2000:00:00',enddate='2016-01-01 00:00:00')
# http://mediaq.usc.edu/MediaQ_MVC_V3/api/geoq/rectangle_query?swlng=-118.291588&nelat=34.021111&nelng=-118.287125&from=2015-01-01 2000:00:00&to=2016-01-01 00:00:00swlat=34.019972&X-API-KEY=REAL_KEY

# Returns a set of video frames
print geoq.video_metadata("d0a0163e5d852e70f87bdc8718166e42989306a5")
# http://mediaq.usc.edu/MediaQ_MVC_V3/api/geoq/video_metadata?vid=d0a0163e5d852e70f87bdc8718166e42989306a5&X-API-KEY=REAL_KEY
