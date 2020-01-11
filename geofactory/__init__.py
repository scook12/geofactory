from random import randint
from random import choice
from geojson import dump
from geojson import Point
from geojson import MultiPoint
from geojson import LineString
from geojson import MultiLineString
from geojson import Polygon
from geojson import MultiPolygon
from geojson import Feature
from geojson import FeatureCollection
from geojson import GeometryCollection
from faker import Faker
from faker.providers.geo import Provider as GeoProvider

class GeoFactory(GeoProvider):
    """
    Faker Provider object for generating valid GeoJSON data
    """

    def __init__(self, factory):
        self.factory = Faker()
        self.factory.add_provider(GeoProvider)
        super().__init__(self.factory)

    def lnglat(self, num=2):
        """
        Returns specific number of random lon/lat pairs
        """
        return [(float(self.factory.longitude()), 
                    float(self.factory.latitude()))  for i in range(num) ]

    def point(self):
        """
        Returns single geojson point object with random coordinates
        """
        return Point(self.lnglat()[0])

    def multipoint(self, count_limit=1000):
        """
        Returns a geojson mutipoint object with a random number of random points
        """
        return MultiPoint([
            self.lnglat() for i in range(randint(0, count_limit))
        ])

    def linestring(self, node_limit=1000):
        """
        Returns a geojson linestring object with a random number of nodes
        """
        return LineString([
            self.lnglat()[0] for i in range(randint(2, node_limit))
        ])

    def multilinestring(self, count_limit=100, node_limit=1000):
        """
        Returns a geojson multilinestring object with a random number of segments
        and a random number of nodes
        """
        return MultiLineString([
            [self.lnglat(num=randint(2, node_limit))][0] for i in range(randint(1, count_limit))
        ])

    def polygon(self, node_limit=3):
        """
        Returns a randomly arranged polygon with a specified number of nodes
        """
        shape = self.lnglat(node_limit)
        shape.append(shape[0])
        return Polygon([shape])

    def multipolygon(self, count_limit=10):
        """
        Returns a specific number of randomly arranged polygons with a random number of nodes
        """
        return MultiPolygon([
            self.polygon(node_limit=randint(3, 11)) for i in range(count_limit)
        ])

    def geometry_collection(self, count_limit=10):
        """
        Returns a specific number of random geojson geometries as a geometry collection
        """
        features = [self.point(), self.multipoint(count_limit=10), self.linestring(node_limit=100), 
                    self.multilinestring(count_limit=10, node_limit=100), self.multipolygon() ]

        return GeometryCollection([
            choice(features) for i in range(count_limit)
        ])

    def feature(self):
        """
        Returns a random geojson feature object
        """
        features = [self.point(), self.multipoint(count_limit=10), self.linestring(node_limit=100), 
                    self.multilinestring(count_limit=10, node_limit=100), self.multipolygon() ]
        
        return Feature(geometry=choice(features))

    def feature_collection(self, count_limit=10):
        """
        Returns a specific number of random features in a feature collection object
        """
        return FeatureCollection([
            self.feature() for i in range(count_limit)
        ])

    @staticmethod
    def to_file(path, data):
        """Writes geojson obj to file"""
        with open(path, 'w') as file:
            dump(data, file)