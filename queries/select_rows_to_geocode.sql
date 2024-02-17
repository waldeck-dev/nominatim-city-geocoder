SELECT id, city, country FROM location
WHERE city IS NOT NULL AND country IS NOT NULL
AND (lat IS NULL OR long IS NULL);