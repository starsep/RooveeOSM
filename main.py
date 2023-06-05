#!/usr/bin/env python
import geojson
import httpx
from pathlib import Path

from geojson import Feature, Point

networks = [
    ("suwalki", "suwalki"),
    ("ostro", "ostroleka"),
]

outputDir = Path("output")
outputDir.mkdir(exist_ok=True)

for tenant, network in networks:
    with (outputDir / f"{network}.geojson").open("w") as output:
        data = httpx.get(
            f"https://api.roovee.eu/public/bikesAndZones?latitude=54&longitude=22&longitudeDelta=30&latitudeDelta=30&tenant={tenant}"
        ).json()
        features = []
        for zone in data["zones"]:
            zoneType = zone["type"]
            if zoneType == "operationsZone":
                continue
            if zoneType != "preferredBikeReturnZone":
                print(f"Unexpected type = {zoneType}")
                continue
            print(zone)
            features.append(
                Feature(
                    geometry=Point(
                        (zone["areaCenter"]["lng"], zone["areaCenter"]["lat"])
                    ),
                    properties=dict(name=zone["name"]),
                )
            )
        geojson.dump(features, output)
