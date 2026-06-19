# DuckDB

## 2026

- [Optimizing DuckDB Spatial Queries](https://www.geomermaids.com/cookbook/duckdb-spatial/): A technical deep-dive comparing spatial join performance between PostGIS and DuckDB, explaining how DuckDB's R-tree index fires only for single constant geometry comparisons while PostGIS auto-uses its GiST index — and showing that DuckDB's streaming `SPATIAL_JOIN` operator wins at scale when both datasets are large. [Keywords: `DuckDB` `PostGIS` `spatial queries` `R-tree` `GiST` `spatial join` `performance` `geospatial`]

- [spatial-access-measures](https://github.com/developmentseed/spatial-access-measures): Web map using DuckDB-WASM and GeoParquet for in-browser SQL queries and filtering of Statistics Canada spatial access measures (transit, cycling, and walking accessibility to jobs, schools, and services). No server backend required — everything runs in the browser. [Demo](https://developmentseed.org/spatial-access-measures/) [Keywords: `DuckDB-WASM` `GeoParquet` `deck.gl` `in-browser SQL` `accessibility` `Canada` `cloud-native`]

- [Freestiler](https://walker-data.com/freestiler/): R and Python tool for creating PMTiles vector tilesets from spatial data, including from DuckDB SQL queries. Uses a Rust tiling engine for in-process performance, producing single `.pmtiles` files compatible with Mapbox and MapLibre formats. [Keywords: `PMTiles` `DuckDB` `R` `Python` `vector tiles` `cloud-native` `MapLibre` `geospatial`]

- [GeoParquet Writing Cookbook](https://www.geomermaids.com/cookbook/geoparquet/): A practical guide with best practices and recipes for creating GeoParquet files using tools like GDAL, DuckDB, and geopandas, covering encoding strategies and optimization techniques for cloud-native geospatial workflows. [Keywords: `GeoParquet` `DuckDB` `GDAL` `cloud-native` `geospatial` `spatial queries` `Python`]
