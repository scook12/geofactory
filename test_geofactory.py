import os
import geojson
import geofactory
import faker

factory = faker.Faker()
factory.add_provider(geofactory.GeoFactory)

def test_point():
    result = factory.point()
    assert (result.is_valid)
    assert (type(result['coordinates'][0]) == float )

def test_multipoint():
    result = factory.multipoint(count_limit=800)
    assert (result.is_valid)
    assert (len(result['coordinates']) <= 800)
    assert (type(result['coordinates'][0][0][0]) == float)

def test_linestring():
    result = factory.linestring(node_limit=90)
    assert (result.is_valid)
    assert(len(result['coordinates']) <= 90)
    assert (type(result['coordinates'][0][0]) == float)

def test_multilinestring():
    result = factory.multilinestring(count_limit=10, node_limit=10)
    assert (result.is_valid)
    assert (len(result['coordinates']) <= 10)
    assert (len(result['coordinates'][0]) <= 10)
    
def test_polygon():
    result = factory.polygon(node_limit=10)
    assert (result.is_valid)
    #assert (len(result['coordinates'][0]) <= 10)

def test_multipolygon():
    result = factory.multipolygon(count_limit=5)
    assert (result.is_valid)
    assert (len(result['coordinates']) <= 5)

def test_geometrycollection():
    result = factory.geometry_collection()
    assert (result.is_valid)
    assert (len(result['geometries']) <= 10)

def test_feature():
    result = factory.feature()
    assert (result.is_valid)
    
def test_featurecollection():
    result = factory.feature_collection(count_limit=5)
    assert (result.is_valid)

def test_to_file():
    data = factory.multipoint(count_limit=10000)
    path = os.path.join(os.getcwd(), "file.json")
    assert (data.is_valid)
    factory.to_file(path, data)
    with open(path, 'r') as read:
        filedata = geojson.load(read)
    assert (filedata.is_valid)