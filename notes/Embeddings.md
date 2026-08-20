# Embeddings

**Summary**: Notes on vector embeddings and representation learning across domains.
**Last updated**: 2026-08-20

---

## 2026

- [Downscaling Weather Prediction using TESSERA Embeddings](https://anil.recoil.org/notes/weather-downscaling-tessera): Downscaling weather prediction using Tessera embeddings — replaces hand-crafted terrain descriptors with TESSERA satellite foundation model embeddings to downscale coarse 25km weather grids into finer-resolution predictions, validated against Microsoft's Aurora AI model and ERA5 reanalysis. Related: [[Climate]], [[Deep_Learning]], [[AI]]. Keywords: TESSERA, embeddings, weather, downscaling, foundation model, Aurora, ERA5

- [Butterfly Habitat Mapping with TESSERA Embeddings](https://github.com/s19835/tessera-embeddings-habitat): Tests whether TESSERA satellite embeddings can distinguish quality butterfly habitat from random locations, using UK Butterfly Monitoring Scheme data across 2,921 sites to train a logistic regression classifier validated with permutation testing. Related: [[Python]], [[Data]]. Keywords: TESSERA, embeddings, butterfly, habitat mapping, logistic regression, Python, scikit-learn

- [Building Classification with GeoAI - Google AlphaEarth in Python](https://www.youtube.com/watch?v=Vqoq1N0jLok): Day 5 of the #30DayMapChallenge demonstrating building type classification on OSM building footprints using Google AlphaEarth embeddings with the GeoAI Python package. Related: [[Web_Mapping]], [[Python]]. Keywords: GeoAI, AlphaEarth, embeddings, OSM, building classification, Python, 30DayMapChallenge

- [S2Vec: Mapping the Modern World](https://research.google/blog/mapping-the-modern-world-how-s2vec-learns-the-language-of-our-cities/): Google Research's S2Vec framework uses masked autoencoding on rasterized Google Maps tiles (S2 Geometry cells) to generate general-purpose embeddings of the built environment, enabling prediction of socioeconomic and environmental metrics like population density, income, and carbon emissions at global scale. Related: [[Urban_Planning]]. Keywords: S2Vec, embeddings, masked autoencoding, S2 Geometry, Google Maps, urban analytics, geospatial ML, self-supervised, socioeconomic

- [Geospatial Skills for Coding Agents](https://isaac.earth/geospatial-skills/): A catalog of installable geospatial skills for coding agents (including Claude), providing plug-in workflows for GDAL, GeoParquet validation, and TESSERA embeddings via the `geotessera` CLI. Related: [[Claude_Code]], [[Remote_Sensing]], [[CNG]]. Keywords: Claude Code, coding agents, GDAL, GeoParquet, TESSERA, geotessera, geospatial, remote sensing, Python

- [Streaming millions of TESSERA tiles over HTTP with Zarr v3](https://anil.recoil.org/notes/tessera-zarr-v3-layout): Describes how TESSERA's geospatial embedding system was restructured from millions of individual NumPy files into sharded Zarr v3 stores per year, enabling efficient HTTP range requests for single-pixel to regional data retrieval with xarray/dask compatibility. Related: [[CNG]], [[XArray]], [[Data]]. Keywords: TESSERA, Zarr, embeddings, HTTP, geospatial, xarray, dask, cloud native

- [The Technical Debt of Earth Embedding Products](https://cloudnativegeo.org/blog/2026/02/the-technical-debt-of-earth-embedding-products/): Examines fragmentation and interoperability challenges in Earth embedding products, arguing that standardizing how embeddings are distributed, stored, and accessed is the real bottleneck for geospatial foundation models. Related: [[Deep_Learning]]. Keywords: embeddings, geospatial, foundation models, interoperability, technical debt, cloud native

## 2025

- [GeoVibes](https://github.com/cr458/geovibes): A geospatial tool for evaluating embedding models through interactive similarity search, using geoparquet and Python for nearest-neighbor queries and binary classifier training with spatial cross-validation. Related: [[CNG]], [[Python]], [[Machine_Learning]]. Keywords: embeddings, geospatial, similarity search, geoparquet, Python, classification

- [SkyScript](https://github.com/wangzhecheng/SkyScript): A large, semantically diverse image-text dataset for remote sensing containing 5.2 million image-text pairs with 29,000+ semantic tags, designed for vision-language model (CLIP) development. Related: [[AI]], [[Remote_Sensing]], [[Data]]. Keywords: VLM, CLIP, satellite imagery, text, remote sensing, embeddings, dataset

- [Scalable Geospatial Data Generation Using AlphaEarth Foundations Model](https://arxiv.org/pdf/2508.11739): Paper on using AlphaEarth foundation model embeddings for transfer learning in forest monitoring applications. Related: [[Deep_Learning]], [[Data]]. Keywords: foundation model, embeddings, AlphaEarth, forest, transfer learning

- [TESSERA: Temporal Embeddings of Surface Spectra for Earth Representation and Analysis](https://arxiv.org/abs/2506.20380): Foundation model paper generating 128-dimensional embeddings from satellite time-series for land classification and canopy height prediction at 10-meter global resolution. Related: [[Deep_Learning]], [[XArray]], [[Remote_Sensing]]. Keywords: foundation model, embeddings, time series, Sentinel-2, land classification, canopy height

- [TESSERA GitHub](https://github.com/ucam-eo/tessera): Open-source implementation of the TESSERA foundation model that processes satellite time-series imagery to generate embeddings for Earth observation tasks. Related: [[Deep_Learning]], [[Remote_Sensing]], [[Python]]. Keywords: foundation model, embeddings, satellite, Python, open source

- [What Do Embeddings Actually Encode in Earth Observation Foundation Models?](https://www.linkedin.com/posts/hdcouture_earthobservation-foundationmodels-embeddings-activity-7364612325808431105-BsZ0): LinkedIn post discussing what semantic information EO foundation model embeddings actually capture. Related: [[Deep_Learning]], [[Remote_Sensing]]. Keywords: embeddings, foundation models, Earth observation, semantics

- [Air Quality Using Satellite Embedding](https://www.preprints.org/manuscript/202508.1202/v1): Preprint on using satellite-derived embeddings for air quality estimation and monitoring. Related: [[Climate]], [[Remote_Sensing]]. Keywords: air quality, satellite, embeddings, remote sensing

- [Text Embeddings for Semantic Search with Overture](https://link.springer.com/article/10.1007/s41651-025-00232-5): Research on text embedding-based semantic search over Overture Maps places dataset. Related: [[AI]]. Keywords: embeddings, semantic search, Overture Maps, NLP, geospatial

- [OSM Embeddings - SRAI](https://kraina-ai.github.io/srai/latest/): SRAI (Spatial Representations for AI) Python library for geospatial machine learning on vector geometries, enabling spatial data download, regionalization, and vector embeddings for ML tasks. Related: [[Web_Mapping]], [[Python]], [[AI]]. Keywords: OSM, embeddings, spatial AI, Python, geospatial ML

## Earlier

- [AlphaEarthFire](https://github.com/afland/AlphaEarthFire): AlphaEarth × MODIS burn dataset builder and model trainer using AEF embeddings to model slow fire variables and predict forest fires. Related: [[Remote_Sensing]], [[Deep_Learning]], [[Python]]. Keywords: embeddings, fire prediction, MODIS, AlphaEarth, foundation model, Python
