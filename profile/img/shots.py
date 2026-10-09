"""Render a preview of each guelph-maps raster layer over a greyed OSM basemap."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

# name: (lat, lon, zoom)
LAYERS = {
    "guelph-parks-layer": (43.5530, -80.2440, 15),
    "guelph-address-layer": (43.5512, -80.2598, 18),
    "guelph-buildings-layer": (43.5448, -80.2500, 17),
    "guelph-bus-stops-layer": (43.5452, -80.2468, 16),
}
only = sys.argv[2:] or list(LAYERS)

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
<style>html,body,#m{margin:0;height:100%;background:#f2f2f0}
.base{filter:grayscale(1) brightness(1.06) contrast(.8)}
.leaflet-control-attribution{font:10px system-ui;background:rgba(255,255,255,.75)!important}</style>
</head><body><div id="m"></div><script>
const m = L.map('m', {zoomControl:false}).setView([@LAT@, @LON@], @Z@);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',
  {maxZoom:21, maxNativeZoom:19, className:'base', attribution:'&copy; OpenStreetMap contributors'}).addTo(m);
L.tileLayer('https://guelph-maps.github.io/@NAME@/tiles/raster/{z}/{x}/{y}.png',
  {maxZoom:21, attribution:'City of Guelph, OGL'}).addTo(m);
</script></body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    for name in only:
        lat, lon, z = LAYERS[name]
        html = (PAGE.replace("@LAT@", str(lat)).replace("@LON@", str(lon))
                .replace("@Z@", str(z)).replace("@NAME@", name))
        pg = b.new_page(viewport={"width": 640, "height": 360}, device_scale_factor=2)
        pg.on("requestfailed", lambda r: print("FAIL", r.url, r.failure))
        url = f"https://guelph-maps.github.io/{name}/__preview.html"
        def serve(body):
            return lambda route: route.fulfill(body=body, content_type="text/html")
        pg.route(url, serve(html))
        pg.goto(url, wait_until="load")
        pg.wait_for_timeout(6000)
        f = OUT / f"{name}.jpg"
        pg.screenshot(path=str(f), type="jpeg", quality=82)
        print(f.name, f.stat().st_size)
        pg.close()
    b.close()
