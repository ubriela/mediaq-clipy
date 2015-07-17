# Requirements.
Python 2.7 and later.

# Installation
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```
Or you can install from Github via pip:

```sh
pip install git+https://github.com/ubriela/mediaq-clipy.git

# Tutorial
To use the bindings, import the pacakge:

```python
import SwaggerMediaq as sm
```

Create geoq client api
```python
geoq = sm.GeoqApi(sm.ApiClient("http://mediaq.usc.edu/MediaQ_MVC_V3/api"))
```

Returns a set of video locations in GEOJSON format (small sample data)
```python
print geoq.sample_videos()
```
Returns a set of video frames (of a particular video) in GEOJSON format (small sample data)
```python
print geoq.sample_fovs()
```

Create geoq client with API key, replace KEY_VALUE by actual one
```python
geoq = sm.GeoqApi(sm.ApiClient("http://mediaq.usc.edu/MediaQ_MVC_V3/api", "X-API-KEY", "KEY_VALUE"))
```

Returns a set of video locations
```python
print geoq.rectangle_query(swlat=34.019972,swlng=-118.291588,nelat=34.021111,nelng=-118.287125)
```

Returns a set of video frames
```python
print geoq.video_metadata("jca1ptaaiz83_2015_1_16_Videotake_1421449431727.mp4")
```

# Test
You can download test file here ./test/geoq_test.py
