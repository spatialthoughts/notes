# SQL

## Spatial SQL Examples

### Find buildings NOT within 30m of other buildings

```sql
SELECT a.fid, a.geometry as geometry
FROM parcels a
LEFT JOIN parcels b
ON st_intersects(st_buffer(a.geometry, 30), b.geometry)
   AND NOT(st_equals(a.geometry, b.geometry))
WHERE b.geometry IS NULL
```
Keywords: SQL, PostGIS, spatial SQL, buffer, GIS
