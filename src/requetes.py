"""Module centralisant les requêtes SQL appliquées au schéma GTFS."""

QUERY_ARRETS_PAR_MODE = """
SELECT 
    CASE r.route_type
        WHEN 0 THEN 'Tramway'
        WHEN 1 THEN 'Métro'
        WHEN 2 THEN 'RER / Train'
        ELSE 'Autre'
    END AS mode_transport,
    COUNT(DISTINCT st.stop_id) AS nombre_d_arrets
FROM routes r
JOIN trips t ON r.route_id = t.route_id
JOIN stop_times st ON t.trip_id = st.trip_id
WHERE r.route_type IN (0, 1, 2)
GROUP BY r.route_type
ORDER BY nombre_d_arrets DESC;
"""

QUERY_TOP_LIGNES_ARRETS = """
SELECT 
    r.route_id,
    COALESCE(r.route_short_name, r.route_long_name) AS nom_ligne,
    CASE r.route_type
        WHEN 0 THEN 'Tramway'
        WHEN 1 THEN 'Métro'
        WHEN 2 THEN 'RER / Train'
        ELSE 'Autre'
    END AS mode_transport,
    COUNT(DISTINCT st.stop_id) AS nombre_d_arrets
FROM routes r
JOIN trips t ON r.route_id = t.route_id
JOIN stop_times st ON t.trip_id = st.trip_id
GROUP BY r.route_id, r.route_short_name, r.route_long_name, r.route_type
ORDER BY nombre_d_arrets DESC
LIMIT 10;
"""

QUERY_AMPLITUDE_HORAIRE_MAX = """
WITH AmplitudeParTrip AS (
    SELECT 
        t.route_id,
        MIN(st.arrival_time::interval) AS premier_passage,
        MAX(st.departure_time::interval) AS dernier_passage,
        MAX(st.departure_time::interval) - MIN(st.arrival_time::interval) AS amplitude
    FROM trips t
    JOIN stop_times st ON t.trip_id = st.trip_id
    GROUP BY t.route_id
)
SELECT 
    r.route_id,
    COALESCE(r.route_short_name, r.route_long_name) AS nom_ligne,
    a.premier_passage::text,
    a.dernier_passage::text,
    a.amplitude::text AS amplitude_horaire
FROM AmplitudeParTrip a
JOIN routes r ON a.route_id = r.route_id
ORDER BY a.amplitude DESC
LIMIT 1;
"""

QUERY_CORRESPONDANCES_PAR_STATION = """
SELECT 
    COALESCE(s.parent_station, s.stop_id) AS station_id,
    p.stop_name AS nom_station,
    COUNT(DISTINCT s.stop_id) AS nombre_d_arrets_rattaches,
    COUNT(DISTINCT t.route_id) AS nombre_de_lignes_en_correspondance
FROM stops s
LEFT JOIN stops p ON s.parent_station = p.stop_id
JOIN stop_times st ON s.stop_id = st.stop_id
JOIN trips t ON st.trip_id = t.trip_id
GROUP BY COALESCE(s.parent_station, s.stop_id), p.stop_name
ORDER BY nombre_de_lignes_en_correspondance DESC, nombre_d_arrets_rattaches DESC
LIMIT 10;
"""
