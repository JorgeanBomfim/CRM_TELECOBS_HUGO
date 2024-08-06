## -- QUARTIL DA CLARO (JESSICA) --
 SELECT DISTINCT
    CONCAT(DDD, Fone) AS 'Telefone',
    ag.nome AS Nome_Agente,
    ag.nome_supervisor AS Nome_Supervisor,
    CASE
        WHEN a.GrupoFila = 6342 THEN 'CLARO RECEPTIVO ATN'
        WHEN a.GrupoFila = 6196 THEN 'CLARO RECEPTIVO ATN'
        WHEN a.GrupoFila = 6198 THEN 'NET RECEPTIVO MUTANT'
        WHEN a.GrupoFila = 6194 THEN 'GEVENUE  REC'
        
        WHEN a.grupoprincipal = 6222 THEN 'PRED ATN'
        WHEN a.grupoprincipal = 6226 THEN 'PRED POS'
        WHEN a.grupoprincipal = 6202 THEN 'CLARO FIXO'
        WHEN a.grupoprincipal = 6204 THEN 'CLARO TV'
        WHEN a.grupoprincipal = 6335 THEN 'CLARO PJ'
        WHEN a.grupoprincipal = 6203 THEN 'CLARO MOVEL'
        WHEN a.grupoprincipal = 6200 THEN 'NET PRED'
        WHEN a.grupoprincipal = 6336 THEN 'NET PJ'
	    WHEN a.grupoprincipal = 6201 THEN 'GEVENUE PRED'
        WHEN a.grupoprincipal = 6337 THEN 'GEVENUE PJ'
            END AS Filas_URA,
    DATE_FORMAT(a.instante, '%d-%m-%y') AS DATA
FROM
    totalinfo_2023_10 a
JOIN
    agentes ag ON a.agentederivacao = ag.username
WHERE
    a.Agente <> ''
    AND a.instante >= '2023-10-16 08:00:00'
    AND a.instante <= '2023-10-16 20:00:00'
    AND a.GrupoFila IN (6202,6204,6335,6203,6200,6336,6201,6337,6342,6196,6198,6194)
    AND ag.nome NOT LIKE 'AVT%';