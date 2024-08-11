from ..models import WindowModel
from ..controller import Controller
from ..services import OpenStreetMapsService, ElevationTilesService
import math

class WindowController(Controller):
    def __init__(self, view):
        self._model = WindowModel(view)

    @property
    def model(self) -> WindowModel:
        return self._model

    def load_osm_data(self, area_name: str):
        osm_result = OpenStreetMapsService.request_query(area_name)
        self._model.nodes = osm_result.nodes()
        self._model.ways = osm_result.ways()
        self._model.relations = osm_result.relations()
        self._model.areas = osm_result.areas()

        for relation in self._model.relations:
            tags = relation.tags()
            admin_level = tags.get("admin_level")
            if admin_level:
                geometry = relation.geometry()
                coordinates = geometry.coordinates
                if geometry.type == "Polygon":
                    if len(coordinates) == 1:
                         self._model.bounding_box = self._get_bounding_box(coordinates[0])
                    else:
                        break
                break

    def _get_bounding_box(self, points):
        first_point = points[0]
        min_lat = max_lat = first_point[1]
        min_lon = max_lon = first_point[0]
        for point in points:
            lat = point[1]
            lon = point[0]
            if lat < min_lat:
                min_lat = lat
            elif lat > max_lat:
                max_lat = lat
            if lon < min_lon:
                min_lon = lon
            elif lon > max_lon:
                max_lon = lon

        return [(min_lon, min_lat), (max_lon, max_lat)]