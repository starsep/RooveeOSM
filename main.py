#!/usr/bin/env python
import shutil
from pathlib import Path

from jinja2 import Environment, PackageLoader
from slugify import slugify

from roovee_comparator import run
from roovee_parser import Network, RooveeParser

networks = [
    Network(tenant="bikes", name="Szczecin"),
    Network(tenant="brom", name="Bolesławiec"),
    Network(tenant="chromek", name="Chodzież"),
    Network(tenant="czeladz", name="Czeladź"),
    Network(tenant="duszniki", name="Duszniki-Zdrój"),
    Network(tenant="gliwice", name="Gliwice"),
    Network(tenant="gniezno", name="Gniezno"),
    # Network(tenant="grom", name="Giżycko"),
    Network(tenant="kielce", name="Kielce"),
    Network(tenant="krotower", name="Krotoszyn"),
    Network(tenant="naklo", name="Nakło nad Notecią"),
    Network(tenant="ndm", name="Nowy Dwór Mazowiecki"),
    Network(tenant="olesnica", name="Oleśnica"),
    Network(tenant="ostro", name="Ostrołęka"),
    # Network(tenant="polkowice", name="Polkowice"),
    Network(tenant="rawicz", name="Rawicz"),
    Network(tenant="skarzysko", name="Skarżysko-Kamienna"),
    Network(tenant="srm", name="Ścinawa"),
    Network(tenant="suwalki", name="Suwałki"),
    Network(tenant="swmr", name="Stalowa Wola"),
    Network(tenant="suchylas", name="Suchy Las"),
    Network(tenant="srem", name="Śrem"),
    Network(tenant="wagrowiec", name="Wągrowiec"),
    Network(tenant="zabrze", name="Zabrze"),
    Network(tenant="zary", name="Żary"),
    Network(tenant="zmigrod", name="Żmigród"),
]

# TODO: GeoJSON output
if __name__ == "__main__":
    templatesDirectory = Path("templates")
    libsDirectory = Path("libs")
    outputDirectory = Path("output")
    outputDirectory.mkdir(exist_ok=True)
    rooveeParser = RooveeParser()
    for network in networks:
        slug = slugify(network.name)
        run(
            network=network,
            outputPath=outputDirectory / f"{slug}.html",
            mapPath=outputDirectory / f"map-{slug}.html",
            rooveeParser=rooveeParser,
        )

    environment = Environment(loader=PackageLoader("main", "templates"))
    template = environment.get_template("index.html")
    cities = sorted(
        [(network.name, slugify(network.name)) for network in networks],
        key=lambda x: x[0],
    )
    with (outputDirectory / "index.html").open("w", encoding="utf-8") as f:
        f.write(template.render(dict(cities=cities)))
    shutil.copy(templatesDirectory / "index.js", outputDirectory / "index.js")
    shutil.copy(libsDirectory / "sorttable.js", outputDirectory / "sorttable.js")
