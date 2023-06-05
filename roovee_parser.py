from dataclasses import dataclass
from typing import List

import httpx

from distance import GeoPoint


@dataclass
class Place(GeoPoint):
    name: str


@dataclass
class Network:
    tenant: str
    name: str


class RooveeParser:
    def downloadNetwork(self, network: Network) -> List[Place]:
        data = httpx.get(
            f"https://api.roovee.eu/public/bikesAndZones?latitude=54&longitude=22&longitudeDelta=30&latitudeDelta=30&tenant={network.tenant}"
        ).json()
        places: List[Place] = []
        for zone in data["zones"]:
            zoneType = zone["type"]
            if zoneType == "operationsZone":
                continue
            if zoneType != "preferredBikeReturnZone":
                print(f"Unexpected type = {zoneType}")
                continue
            places.append(
                Place(
                    name=zone["name"],
                    lat=zone["areaCenter"]["lat"],
                    lon=zone["areaCenter"]["lng"],
                )
            )
        return places
