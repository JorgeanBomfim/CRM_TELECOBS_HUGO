import pymysql
import pandas as pd
import numpy as np
import warnings
import glob
from unidecode import unidecode
##### CONECTANDO NO BANCO SERVIDOR EXPERT ATN
def conectar_banco():
        conexao = pymysql.connect(host='10.0.6.2',
        user='planejamento',
        passwd='@Planejamento!123',
        db='atn',
        charset ='utf8'
        )
        return conexao


### BAIXANDO TODAS AS CHAMADAS DIA DA CLARO COBRANÇA
def parametro_busca(data_ini, data_fim):
    query = f"""
    SELECT DISTINCT
    DATE_FORMAT(a.instante, '%d/%m/%Y') AS DATA
    ,a.CallID
    ,a.GrupoFila
    ,CONCAT(a.DDD ,a.Fone) AS 'TELEFONE'
    ,a.GrupoPrincipal
    ,1 as DISCADO_SIM
    ,(CASE WHEN a.ResultadoClassificacao = 'vozhumana' THEN 1 ELSE 0  END) AS 'ATENDIDO_SIM'
    ,(CASE WHEN a.GrupoFila IN ('6192') THEN 1 ELSE 0  END) AS 'DTMF_SIM'
    FROM totalinfo_2024_07 AS a
    WHERE a.instante >= '{data_ini} 07:00:00'
    AND a.instante <= '{data_fim} 23:00:00'
    AND a.GrupoPrincipal IN (6186,6187,6192,6195,6196,6199,6200,6202,6203,
    6204,6313,6335,6342,6529,6188,6189,6193,6197,6198,6200,6205,6314,6336,
    6190,6191,6194,6201,6207,6209,6315,6337)
    """
    return query
def fechar_conexao():
    conexao = conectar_banco()   
    # Fechando as conexões
    conexao.close()



def chamadas_agentes(data_ini, data_fim):
        query = f""" SELECT DISTINCT
        DATE_FORMAT(a.instante, '%d/%m/%Y') AS DATA,
        a.CallID,
        a.GrupoFila,
        a.GrupoPrincipal,
        CONCAT(a.DDD , a.Fone)AS TELEFONE,
        a.agentederivacao AS CPF_AGENTE,
        j.nome AS NOME_AGENTE,

		(CASE
				WHEN UPPER(f.arc_desc) LIKE '%CLARO%' THEN 'CLARO'
				WHEN UPPER(f.arc_desc) LIKE '%NET%' THEN 'NET'
				ELSE 'REC SEM MAILING' 
				END) AS 'FILA',    
				1 AS ATENDIDAS,
                
        (CASE WHEN a.GrupoPrincipal  IN ('6202','6203','6204','6335', '6200','6336','6201','6337') THEN 1 ELSE 0  END) AS 'PREDITIVO',
		(CASE WHEN a.GrupoFila IN ('6209','6197','6193', '6192','6195') THEN 1 ELSE 0  END) AS 'URA',
        (CASE WHEN a.GrupoFila IN ('6196','6342','6198','6194') THEN 1 ELSE 0  END) AS 'RECEPTIVO'       
    FROM totalinfo_2024_07 a
    LEFT JOIN arquivo_mailing f ON a.id_arquivo = f.ID_ARQUIVOMAILING
    LEFT JOIN agentes j ON (a.agentederivacao = j.username)
    WHERE a.instante >= '{data_ini} 07:00:00'
        AND a.instante <= '{data_fim} 23:00:00'
        AND a.GrupoPrincipal IN (6186,6187,6192,6195,6196,6199,6202,6203,6204,6313,6335,6342,6529, ## FILAS CLARO
                                 6188,6189,6193,6197,6198,6200,6205,6314,6336, ## FILAS NET
								 6190,6191,6194,6201,6207,6209,6315,6337)  ## FILAS GEVENUE
        AND j.nome NOT REGEXP '[0-9]' ## SOMENTE AGENTES QUE NAO CONTÉM NÚMERO NO NOME (REMOVE TODOS OS AGVS)
        """
        return query
        
        
        
        
        
        





















        
        
        
        
        

        









########################################### CARREGANDO AS BASES UNIFICADAS DA ATN FIBRA
def carregar_bases_claro_padronizada(caminho, extensao="txt", chunksize=1000000, sep=';', encoding='iso-8859-1'):
    try:
        # Encontrar todos os arquivos com a extensão especificada no caminho
        arquivos = glob.glob(f"{caminho}/*.{extensao}")
        if not arquivos:
            raise FileNotFoundError(f"Nenhum arquivo '{extensao}' encontrado no caminho especificado: {caminho}")
        
        df_list = []

        # Iterar sobre cada arquivo encontrado
        for arquivo in arquivos:
            print(f"Carregando {arquivo}...")
            # Ler o arquivo em chunks e adicionar à lista de DataFrames
            for chunk in pd.read_csv(arquivo, chunksize=chunksize, dtype='str', sep=sep, encoding=encoding):
                df_list.append(chunk)

        # Concatenar todos os DataFrames em um único DataFrame
        bases_concatenadas = pd.concat(df_list, sort=False, ignore_index=True)
        print("Carregamento e concatenação concluídos com sucesso.")
        return bases_concatenadas
    
    except Exception as e:
        print(f"Erro ao carregar arquivos: {e}")
        return None
    
