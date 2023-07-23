Compares data of Roovee and OpenStreetMap.

Code based on [NextbikeOSM](https://github.com/starsep/NextbikeOSM)

Website at https://starsep.com/RooveeOSM/

## Docker
```
docker build -t rooveeosm .
docker run --rm \
    -v "$(pwd)/cache:/app/cache" \
    --env GITHUB_USERNAME=example \
    --env GITHUB_TOKEN=12345 \
    --env TZ=Europe/Warsaw \
    -t rooveeosm
```
