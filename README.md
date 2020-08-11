# GeoFactory

This is a faker provider that generates fake geojson data. It simulates all the different types of features and geometries in the geojson specification. There is also a test suite for the class and it's methods run with pytest.

Note: I wrote this as a tiny side project I built while developing an app that ingested geojson. The geojson library has a utility for generating random values, so if you're here looking for a way to generate random geojson data and you don't already use faker, you should prefer the `geojson.utilities.generate_random`

## Setup

Install with pip:

`pip install geofactory`

## Use

GeoFactory is a Faker provider for geojson. 

An example might look like this:

```
from faker import Faker
from geofactory import GeoFactory

factory = Faker()
factory.add_provider(GeoFactory)

pt = factory.point() # valid geojson Point feature - all methods follow this pattern
```
## Methods

`lnglat`

Returns a given number of random longitude/latitude pairs.

`point`

Returns a single geojson point object with random coordinates

`multipoint`

Returns a multipoint geojson object with a random number of random points
:param: count_limit - determines the maxiumum number of points generated

`linestring`

Returns a linestring geojson object with a random number of nodes
:param: node_limit - determines the maxiumum number of nodes generated

`multilinestring`

Returns a multilinestring with a random number of segments with a random number of nodes
:param: node_limit - determines maximum number of nodes for a given linestring
:param: count_limit - determines the maximum number of line segments generated

`polygon`

Returns a randomly arranged polygon with a specific number of nodes
:param: node_limit - determines how many nodes will be in the return polygon

`multipolygon`

Returns a geojson multipolygon with a specific number of randomly arranged polygons
:param: count_limit - determines how many polygons will be created

`geometry_collection`

Note: use of geometry collections is discouraged by the geojson spec.

Returns a specific number of random geojson geometries as a collection
:param: count_limit - determines how many geometries will be generated

`feature`

Returns a random geojson feature object

`feature_collection`

Returns a specific number of random features in a feature collection object
:param: count_limit - determines how many features will be generated

`to_file`

Writes geojson object to file
:param: path - full path and filename for data to be written to
:param: data - valid geojson object to dump in path

## Contribute

Feel free to open an issue, fork the repo, submit a PR, etc.

If you make changes to existing methods, run `pytest` to make sure they all 
are still passing and include coverage for your new methods/classes.
