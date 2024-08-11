from ..models import TerrainModel
from ..controller import Controller
from ..services import OpenStreetMapsService, ElevationTilesService
import math
from typing import List

class TerrainController(Controller):
    def __init__(self, view):
        self._model = TerrainModel(view)

    def load_terrain(self, bounding_box: List[tuple]):
        min_lat = bounding_box[0][1]
        max_lat = bounding_box[1][1]
        min_lon = bounding_box[0][0]
        max_lon = bounding_box[1][0]
        self._model.lat_intervals = tuple(reversed(self._get_hgt_intervals(min_lat, max_lat)))
        self._model.lon_intervals = self._get_hgt_intervals(min_lon, max_lon)

        hgt_files = []
        for lat_interval in self._model.lat_intervals:
            # latitude of the lower-left corner of the .hgt tile
            lat = math.floor(lat_interval[0])
            for lon_interval in self._model.lon_intervals:
                # longitude of the lower-left corner of the .hgt tile
                lon = math.floor(lon_interval[0])
                hgt_file = self._get_hgt_file_name(lat, lon)
                hgt_files.append(hgt_file)


        hgt_data = {}
        for file in hgt_files:
            data = ElevationTilesService.request_hgt_data(file)
            hgt_data[file] = data

        self._model.hgt_data = hgt_data


    def _get_hgt_intervals(self, x1, x2):
        """
        Split (x1, x2) into .hgt intervals. Examples:
        (31.2, 32.7) => [ (31.2, 32), (32, 32.7) ]
        (31.2, 32) => [ (31.2, 32) ]
        """
        _x1 = x1
        intervals = []
        while True:
            _x2 = math.floor(_x1 + 1)
            if (_x2>=x2):
                intervals.append((_x1, x2))
                break
            else:
                intervals.append((_x1, _x2))
                _x1 = _x2
        return intervals

    def _get_hgt_file_name(self, lat, lon):
        prefix_lat = "N" if lat>= 0 else "S"
        prefix_lon = "E" if lon>= 0 else "W"
        return "{}{:02d}{}{:03d}.hgt.gz".format(prefix_lat, abs(lat), prefix_lon, abs(lon))