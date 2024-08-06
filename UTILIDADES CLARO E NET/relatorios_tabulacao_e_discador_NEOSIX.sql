SELECT 
'ATN' AS EPS,
t.instante AS callbegin,
t.InstanteDesligamentoPub AS call_END,
t2.descricao AS TABULACAO,
	CASE
		WHEN t.GrupoFila = 6202 THEN 'CLARO FIXO'
		WHEN t.GrupoFila = 6203 THEN 'CLARO MOVEL'
		WHEN t.GrupoFila = 6204 THEN 'CLARO TV'
			END AS carteira,
t.Chave2 as cliente,
CONCAT(t.DDD,t.Fone),
t.Chave1 contrato,
t.Agente,
'' AS coringa1,
'' AS coringa2,
'' AS coringa3,
'' AS coringa4,
'' AS coringa5,
'' AS coringa6,
'' AS coringa7,
'' AS coringa8,
'' AS coringa9
 from atn.totalinfo_2024_01 t
INNER JOIN atn.tabulacaooper t1
ON t.CallID = t1.callid
INNER JOIN atn.tabulacao t2
ON t1.codtabulacao = t2.codtabulacao AND t1.codgrupo = t2.id_grupo
left JOIN arquivo_mailing am 
ON am.ID_ARQUIVOMAILING = t.id_arquivo
WHERE t.instante >'2024-01-03 00:00:00' AND t.instante <'2024-01-03 22:00:00'
AND t.GrupoPrincipal IN (6204,6202,6203,6204)
	AND t.ResultadoClassificacao ='VozHumana'

-- acima relatório discador

SELECT 
'ATN' AS EPS,
t.Chave2 as cliente,
	CASE
		WHEN t.GrupoFila = 6202 THEN 'CLARO FIXO'
		WHEN t.GrupoFila = 6203 THEN 'CLARO MOVEL'
		WHEN t.GrupoFila = 6204 THEN 'CLARO TV'
			END AS carteira,
t2.descricao AS TABULACAO,
t.Chave1 contrato,
t.Agente,
'' AS coringa1,
'' AS coringa2,
'' AS coringa3,
'' AS coringa4,
'' AS coringa5,
'' AS coringa6,
'' AS coringa7,
'' AS coringa8,
'' AS coringa9,
'' AS coringa10
 from atn.totalinfo_2024_01 t
INNER JOIN atn.tabulacaooper t1
ON t.CallID = t1.callid
INNER JOIN atn.tabulacao t2
ON t1.codtabulacao = t2.codtabulacao AND t1.codgrupo = t2.id_grupo
left JOIN arquivo_mailing am 
ON am.ID_ARQUIVOMAILING = t.id_arquivo
WHERE t.instante >'2024-01-03 00:00:00' AND t.instante <'2024-01-03 22:00:00'
AND t.GrupoPrincipal IN (6204,6202,6203,6204)
AND t.ResultadoClassificacao ='VozHumana';

-- acima relatório de tab