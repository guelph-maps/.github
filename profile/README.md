<h3>Guelph · open city data, in OpenStreetMap</h3>

<p><sub>
Tools that compare what the City of Guelph publishes against what OpenStreetMap
already knows — and hand mappers the difference, in the editor, where the work
actually happens.
</sub></p>

<p><sub><i>Guelph is not a blank map. The gap is rarely the features; it is
almost always the attributes.</i></sub></p>

<h3>Reference layers</h3>

<p><sub>Tile layers you add to <b>iD</b> or <b>JOSM</b> as a background, each
with a gap page listing what OSM is missing, misnaming, or leaving
unnamed.</sub></p>

<table>
<tr>
<td valign="top" width="50%">
<b><a href="https://guelph-maps.github.io/guelph-parks-layer/">guelph-parks-layer</a></b><br>
<sub>126 City parks against OSM · <a href="https://guelph-maps.github.io/guelph-parks-layer/gaps/">gaps</a> · <a href="https://github.com/guelph-maps/guelph-parks-layer"><code>code</code></a></sub><br>
<sub>100 match cleanly · 16 missing · 7 named differently · 3 unnamed in OSM</sub>
</td>
<td valign="top" width="50%">
<b><a href="https://guelph-maps.github.io/guelph-address-layer/">guelph-address-layer</a></b><br>
<sub>53,847 City address points, drawn as house numbers · <a href="https://github.com/guelph-maps/guelph-address-layer"><code>code</code></a></sub><br>
<sub>40,634 civic addresses · 6.2% still missing from OSM · units on a quarter of rows · rebuilt daily</sub>
</td>
</tr>
</table>

<p><sub><i>More in progress:</i> pitches, transit stops, stormwater basins, bike
facilities, truck routes, trails, community gardens.</sub></p>

<h3>Watchers</h3>

<p><sub>Where the City data itself needs judgment — placeholder points, stale
rows, records that were never real — a layer is not enough. These keep a
per-record history and somewhere to write down what a human decided.</sub></p>

<p><sub>
<a href="https://github.com/guelph-maps/guelph-address-import">guelph-address-import</a> — continuous gap-fill and QA over Guelph's completed 2025 address import, the watcher behind the address layer ·
<a href="https://github.com/guelph-maps/guelph-pitches-beholder">guelph-pitches-beholder</a> — 191 courts and sports fields, 162 of them unnamed in OSM
</sub></p>

<h3>Groundwork</h3>

<p><sub>
<a href="https://github.com/guelph-maps/guelph-boundaries">guelph-boundaries</a> — BIA and neighbourhood boundaries, with the Overpass queries behind them
</sub></p>

<h3>How this works</h3>

<p><sub>
Nothing here is bulk-imported. Every layer is compared against OSM first, and
where OSM already has the object, the City data is a <i>reference</i> — it goes
in front of a mapper, not into the database. Edits are made by people, one at a
time, under the OSM
<a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">import guidelines</a>
and <a href="https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct">automated edits code of conduct</a>.
</sub></p>

<p><sub>
Not affiliated with the City of Guelph. Source data is the City's open data,
used under its licence:
</sub></p>

<p><sub>
Contains information licensed under the
<a href="https://gismaps.guelph.ca/Images/OpenDataLicenceVersion2.pdf">Open Government Licence – City of Guelph</a>.
</sub></p>

<p><sub>Maintained by <a href="https://github.com/skfd">@skfd</a> · OSM user <code>skfd</code></sub></p>
