import requests
from requests.utils import quote
from typing import List, Dict, Any
from OSMPythonTools.overpass import Overpass, OverpassResult

class OpenStreetMapsService():
    @classmethod
    def request_query(cls, area) -> OverpassResult:
        overpass = Overpass()
        result = overpass.query(
            f"""
                area[name="{area}"]->.searchArea;
                (
                    node["amenity"](area.searchArea);
                    node["name"](area.searchArea);
                    node["shop"](area.searchArea);
                    node["tourism"](area.searchArea);
                    node["place"](area.searchArea);
                    way["highway"](area.searchArea);
                    way["landuse"](area.searchArea);
                    way["building"](area.searchArea);
                    way["waterway"](area.searchArea);
                    way["railway"](area.searchArea);
                    way["natural"](area.searchArea);
                    way["boundary"](area.searchArea);
                    relation["admin_level"](area.searchArea);
                    relation["boundary"](area.searchArea);
                );
                out body;
            """
        )
        return result
