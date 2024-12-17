
DROP VIEW IF EXISTS simulador_solicitud_view;
CREATE VIEW  IF NOT EXISTS simulador_solicitud_view AS
SELECT
    s.id,
    s.consumo_kwh,
    s.pago,
    s.cantidad_energia_ahorrada,
    s.cliente_id,
    s.estado_id,
    st.nombre AS estado,
    cc.nombres,
    s.created_at AS fecha
FROM
    simulador_solicitud AS s
    JOIN direccion_estado AS st ON st.id = s.estado_id
    JOIN clientes_cliente AS cc ON cc.id = s.cliente_id