from typing import List, Dict
from OSMPythonTools.element import Element
from ..model import Model
from ..view import View

class WindowModel(Model):
    def __init__(self, view: View):
        super().__init__(view)

        self._nodes: List[Element] = []
        self._ways: List[Element] = []
        self._relations: List[Element] = []
        self._areas: List[Element] = []
        self._bounding_box: List[tuple] = []

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, value):
        if self._nodes != value:
            self._nodes = value
            self.notify_update("nodes")

    @property
    def ways(self):
        return self._ways

    @ways.setter
    def ways(self, value):
        if self._ways != value:
            self._ways = value
            self.notify_update("ways")

    @property
    def relations(self):
        return self._relations

    @relations.setter
    def relations(self, value):
        if self._relations != value:
            self._relations = value
            self.notify_update("relations")

    @property
    def areas(self):
        return self._areas

    @areas.setter
    def areas(self, value):
        if self._areas != value:
            self._areas = value
            self.notify_update("areas")

    @property
    def bounding_box(self):
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, value):
        if self._bounding_box != value:
            self._bounding_box = value
            self.notify_update("bounding_box")
