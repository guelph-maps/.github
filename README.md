# .github

Org-level files for [@guelph-maps](https://github.com/guelph-maps).
`profile/README.md` renders on the organisation page.

The layer previews in `profile/img/` are each layer's live raster tiles over a greyed
OSM basemap; the bike parking map and plaza page are shots of the pages themselves. To
redraw them after one changes its look:

```
python profile/img/shots.py profile/img                     # all of them
python profile/img/shots.py profile/img guelph-parks-layer  # just one
```

Needs `pip install playwright` and `playwright install chromium`. The view for each
layer (centre and zoom) is the `LAYERS` table at the top of the script, and the pages are
in `PAGES` below it.
