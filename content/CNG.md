# CNG (Cloud Native Geospatial)

## 2026

- [dynamical.org](https://dynamical.org/): A research lab providing a public catalog of cloud-optimized weather and climate datasets, helping researchers, forecasters, and developers access, understand, and act on environmental data. [Keywords: `weather` `climate` `data` `cloud-optimized` `open data` `forecast`]

- [EO Platforms, Science Platforms, and the Apartment Between Binder and Earth Engine](https://whatnicklife.blogspot.com/2026/06/eo-platforms-science-platforms-and.html): Blog post on the current state of Earth Observation platforms, arguing they exist on a spectrum from managed services (Google Earth Engine) to bare infrastructure (Kubernetes), with "apartment model" namespaces offering identity, storage, and compute as an optimal middle ground. [Keywords: `Earth Observation` `platforms` `Google Earth Engine` `Kubernetes` `cloud-native` `infrastructure`]

- [spatial-access-measures](https://github.com/developmentseed/spatial-access-measures): Web map using DuckDB-WASM and GeoParquet for in-browser SQL queries and filtering of Statistics Canada spatial access measures (transit, cycling, and walking accessibility to jobs, schools, and services). No server backend required — everything runs in the browser. [Demo](https://developmentseed.org/spatial-access-measures/) [Keywords: `DuckDB-WASM` `GeoParquet` `deck.gl` `web mapping` `in-browser SQL` `accessibility` `Canada` `cloud-native`]

- [deck.gl-raster](https://developmentseed.org/deck.gl-raster/): Client-side visualization library for large raster datasets like COGs and Zarr arrays directly in the browser using WebGL2 through deck.gl, with GPU-accelerated processing for color mapping and reprojection. [Keywords: `deck.gl` `COG` `Zarr` `WebGL` `raster` `visualization` `cloud-native` `JavaScript`]

- [S2Mosaic](https://github.com/DPIRD-DMA/S2Mosaic): Python package for creating cloud-free mosaics from Sentinel-2 imagery, with flexible scene selection, multiple compositing methods, and state-of-the-art cloud masking via OmniCloudMask. [Keywords: `Sentinel-2` `cloud masking` `mosaicking` `Python` `remote sensing` `STAC` `geospatial`]

- [Freestiler](https://walker-data.com/freestiler/): R and Python tool for creating PMTiles vector tilesets from spatial data, including from DuckDB SQL queries. Uses a Rust tiling engine for in-process performance, producing single `.pmtiles` files compatible with Mapbox and MapLibre formats. [Keywords: `PMTiles` `DuckDB` `R` `Python` `vector tiles` `cloud-native` `MapLibre` `geospatial`]

- [Yosegi](https://github.com/Kanahiro/yosegi): Python tool that generates pyramid GeoParquet files optimized for efficiently streaming large geospatial datasets. Uses density-based thinning, Sort-Tile-Recursive spatial packing, and GeoParquet 1.1 bbox covering metadata for fast overview queries and row-group pruning. [Keywords: `GeoParquet` `Python` `pyramid` `cloud-native` `spatial data` `optimization` `streaming`]
