from typing import List, Dict
from OSMPythonTools.element import Element
from ..model import Model
from ..view import View

class TerrainModel(Model):
    def __init__(self, view: View):
        super().__init__(view)

        self._lat_intervals: List = []
        self._lon_intervals: List = []
        self._hgt_data: Dict = {}

    @property
    def lat_intervals(self):
        return self._lat_intervals

    @lat_intervals.setter
    def lat_intervals(self, value):
        if self._lat_intervals != value:
            self._lat_intervals = value
            self.notify_update("lat_intervals")

    @property
    def lon_intervals(self):
        return self._lon_intervals

    @lon_intervals.setter
    def lon_intervals(self, value):
        if self._lon_intervals != value:
            self._lon_intervals = value
            self.notify_update("lon_intervals")

    @property
    def hgt_data(self):
        return self._hgt_data

    @hgt_data.setter
    def hgt_data(self, value):
        if self._hgt_data != value:
            self._hgt_data = value
            self.notify_update("hgt_data")
