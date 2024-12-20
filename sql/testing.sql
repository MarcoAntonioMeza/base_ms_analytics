SELECT
    mp.id,
    mp.empresa_preventa_id,
    CASE
        WHEN mp.metodo_pago = 10 THEN 'CREDITO'
        WHEN mp.metodo_pago = 20 THEN 'PUNTOS'
        ELSE 'DESCONOCIDO'
    END AS tipo_pago,
    mp.cantidad,
    FROM_UNIXTIME(ep.created_at) AS fecha
FROM
    empresa_preventa_metodo_pago AS mp
    JOIN empresa_preventa AS ep ON ep.id = mp.empresa_preventa_id
WHERE
    mp.empresa_preventa_id = 2194