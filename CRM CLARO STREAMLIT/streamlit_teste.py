import pandas as pd
import streamlit as st
import base64
import streamlit as st
import glob
import warnings



############### VISUAL ############
st.set_page_config(
    page_title="CRM TELECOB'S",
    page_icon="py-removebg-preview.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Crie duas colunas, sendo a primeira para a imagem e a segunda para o conteúdo
col1, col2 = st.columns([1, 12])

# Carregue a imagem desejada
image_url = "py-removebg-preview.png"
col1.image(image_url, width=150)
col2.subheader("CRM TELECOB")


padding_top = 2,1  # Defina o valor desejado para o padding-top

def main():
    # Use format() para substituir a variável no código CSS
    css = """
    <style>
    .appview-container .main .block-container {{
        padding-top: {}rem;
    }}
    </style>
    """.format(padding_top)

    # Renderize o código CSS
    st.markdown(css, unsafe_allow_html=True)

if __name__ == "__main__":
    main()



## ocultando menu e marca d'agua
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

### PERSONALIZANDO O TAMANHO DO BOTÃO
st.markdown("<style>div.stButton > button:first-child { font-size: 18px; }</style>", unsafe_allow_html=True)



def carregar_bases_claro():
    caminho = r"R:\TI\TELEFONIA\BASES CLARO E NET ATIVA\BASES CLARO"
    arquivos = glob.glob(caminho + "/*.txt")
    #Lista de larguras do layout NET COB
    lista_de_larguras = [50,50,20,50,20,50,50,100,20,50,9,9,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,17,17,19,18,8,11]
    lista = []
    for arquivo in arquivos:
        print(arquivo)
        lista.append(arquivo)
        
        dfList = []
        
        for item in lista:   
            chunks = pd.read_fwf(item, encoding='iso-8859-1', chunksize=1000000, sep=";",widths = lista_de_larguras, dtype='str')
            for df in chunks:
                dfList.append(df)

    # Criando DataFrame com concat e a lista criada a cima
    bases_claro = pd.concat(dfList, sort=False, ignore_index=False)


    bases_claro = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE', 'TELEFONE_1', 'TELEFONE_2',
        'TELEFONE_3', 'TELEFONE_4', 'TELEFONE_5', 'TELEFONE_6', 'TELEFONE_7',
        'TELEFONE_8', 'TELEFONE_9', 'TELEFONE_10', 'TELEFONE_11', 'TELEFONE_12',
        'TELEFONE_13', 'TELEFONE_14','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]


    # TRATANDO CPF E CNPJ, INCLUINDO ZEROS A ESQUERDA.
    df_cpfs_correto = bases_claro[bases_claro['CPF'].str.len()==11]
    df_cnpjs_correto = bases_claro[bases_claro['CPF'].str.len()==14]
    df_cpfs_corrigir = bases_claro[bases_claro['CPF'].str.len()<11]
    df_cpfs_corrigir['CPF'] = df_cpfs_corrigir['CPF'].apply(lambda x: '{0:0>11}'.format(x))
    df_cnpj_corrigir = bases_claro[bases_claro['CPF'].str.len()>11]
    df_cnpj_corrigir['CPF']  = df_cnpj_corrigir['CPF'].apply(lambda x: '{0:0>14}'.format(x))
    bases_claro = pd.concat([df_cpfs_correto,df_cpfs_correto,df_cpfs_corrigir,df_cnpj_corrigir],ignore_index=True)\
    .drop_duplicates(['CPF','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO'])

    claro_1 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_2 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_1','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_3 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_2','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_4 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_3','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_5 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_4','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_6 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_5','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_7 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_6','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_8 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_7','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_9 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_8','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_10 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_9','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_11 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_10','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_12 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_11','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_13 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_12','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_14 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_13','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]
    claro_15 = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_14','ATR_CLAR','SALDO_ABERTO_CLARO','OPERACAO']]

    # RENOMEANDO PRA CONCATENAR
    claro_2 = claro_2.rename(columns={'TELEFONE_1':'TELEFONE'})
    claro_3 = claro_3.rename(columns={'TELEFONE_2':'TELEFONE'})
    claro_4 = claro_4.rename(columns={'TELEFONE_3':'TELEFONE'})
    claro_5 = claro_5.rename(columns={'TELEFONE_4':'TELEFONE'})
    claro_6 = claro_6.rename(columns={'TELEFONE_5':'TELEFONE'})
    claro_7 = claro_7.rename(columns={'TELEFONE_6':'TELEFONE'})
    claro_8 = claro_8.rename(columns={'TELEFONE_7':'TELEFONE'})
    claro_9 = claro_9.rename(columns={'TELEFONE_8':'TELEFONE'})
    claro_10 = claro_10.rename(columns={'TELEFONE_9':'TELEFONE'})
    claro_11 = claro_11.rename(columns={'TELEFONE_10':'TELEFONE'})
    claro_12 = claro_12.rename(columns={'TELEFONE_11':'TELEFONE'})
    claro_13 = claro_13.rename(columns={'TELEFONE_12':'TELEFONE'})
    claro_14 = claro_14.rename(columns={'TELEFONE_13':'TELEFONE'})
    claro_15 = claro_15.rename(columns={'TELEFONE_14':'TELEFONE'})

    bases_claro = pd.concat([claro_1,claro_2,claro_3,claro_4,claro_5,claro_6,claro_7,claro_8,claro_9,claro_10,claro_11,claro_12,claro_13,claro_14,claro_15])
    # FILTRANDO APENAS AS COLUNAS COM TELEFONE, POIS A BASE DA INTERSIC TEM MUITA LINHA NAN
    bases_claro = bases_claro.query("TELEFONE.notnull()")
    bases_claro = bases_claro.rename(columns={'OPERACAO':'BASE'})
    bases_claro = bases_claro.assign(EMAIL="")

    bases_claro = bases_claro.loc[:,['CPF','DEVEDOR','NOME','TELEFONE','EMAIL','ATR_CLAR','SALDO_ABERTO_CLARO','BASE']]
    bases_claro = bases_claro.rename(columns={'ATR_CLAR':'ATRASO'})
    bases_claro = bases_claro.rename(columns={'SALDO_ABERTO_CLARO':'SALDO_ABERTO'})

    bases_claro['ATRASO'] = bases_claro['ATRASO'].astype('int16')
    bases_claro = bases_claro.sort_values(['ATRASO','BASE'],ascending=True)
    
    return bases_claro

def carregar_bases_net():
    caminho = r"R:\TI\TELEFONIA\BASES CLARO E NET ATIVA\BASES NET"
    arquivos = glob.glob(caminho + "/*.txt")
    #Lista de larguras do layout NET COB
    lista_de_larguras = [50,50,20,50,20,50,50,100,20,50,9,9,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,17,17,19,18,11,20]
    lista = []
    for arquivo in arquivos:
        print(arquivo)
        lista.append(arquivo)
        
        dfList = []
        
        for item in lista:   
            chunks = pd.read_fwf(item, encoding='iso-8859-1', chunksize=1000000, sep=";",widths = lista_de_larguras, dtype='str')
            for df in chunks:
                dfList.append(df)
                
    ###########################################################################################################################################    

    # Criando DataFrame com concat e a lista criada a cima
    bases_net = pd.concat(dfList, sort=False, ignore_index=False)


    bases_net = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE', 'TELEFONE_1', 'TELEFONE_2',
        'TELEFONE_3', 'TELEFONE_4', 'TELEFONE_5', 'TELEFONE_6', 'TELEFONE_7',
        'TELEFONE_8', 'TELEFONE_9', 'TELEFONE_10', 'TELEFONE_11', 'TELEFONE_12',
        'TELEFONE_13', 'TELEFONE_14','ATR_NET','SALDO_ABERTO_NET']]
    bases_net = bases_net.assign(OPERACAO="NET")

    net_1 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_2 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_1','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_3 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_2','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_4 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_3','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_5 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_4','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_6 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_5','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_7 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_6','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_8 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_7','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_9 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_8','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_10 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_9','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_11 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_10','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_12 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_11','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_13 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_12','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_14 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_13','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]
    net_15 = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE_14','ATR_NET','SALDO_ABERTO_NET','OPERACAO']]

    # RENOMEANDO PRA CONCATENAR
    net_2 = net_2.rename(columns={'TELEFONE_1':'TELEFONE'})
    net_3 = net_3.rename(columns={'TELEFONE_2':'TELEFONE'})
    net_4 = net_4.rename(columns={'TELEFONE_3':'TELEFONE'})
    net_5 = net_5.rename(columns={'TELEFONE_4':'TELEFONE'})
    net_6 = net_6.rename(columns={'TELEFONE_5':'TELEFONE'})
    net_7 = net_7.rename(columns={'TELEFONE_6':'TELEFONE'})
    net_8 = net_8.rename(columns={'TELEFONE_7':'TELEFONE'})
    net_9 = net_9.rename(columns={'TELEFONE_8':'TELEFONE'})
    net_10 = net_10.rename(columns={'TELEFONE_9':'TELEFONE'})
    net_11 = net_11.rename(columns={'TELEFONE_10':'TELEFONE'})
    net_12 = net_12.rename(columns={'TELEFONE_11':'TELEFONE'})
    net_13 = net_13.rename(columns={'TELEFONE_12':'TELEFONE'})
    net_14 = net_14.rename(columns={'TELEFONE_13':'TELEFONE'})
    net_15 = net_15.rename(columns={'TELEFONE_14':'TELEFONE'})

    bases_net = pd.concat([net_1,net_2,net_3,net_4,net_5,net_6,net_7,net_8,net_9,net_10,net_11,net_12,net_13,net_14,net_15])

    # FILTRANDO APENAS AS COLUNAS COM TELEFONE, POIS A BASE DA INTERSIC TEM MUITA LINHA NAN
    bases_net = bases_net.query("TELEFONE.notnull()")
    bases_net = bases_net.rename(columns={'OPERACAO':'BASE'})
    bases_net = bases_net.assign(EMAIL="")

    bases_net = bases_net.loc[:,['CPF','DEVEDOR','NOME','TELEFONE','EMAIL','ATR_NET','SALDO_ABERTO_NET','BASE']]
    bases_net = bases_net.rename(columns={'ATR_NET':'ATRASO'})
    bases_net = bases_net.rename(columns={'SALDO_ABERTO_NET':'SALDO_ABERTO'})

    bases_net['ATRASO'] = bases_net['ATRASO'].astype('int32')
    bases_net = bases_net.sort_values(['ATRASO','BASE'],ascending=True)
    
    return bases_net

def carregar_base_gevenue():
    caminho = r"R:\TI\TELEFONIA\BASES CLARO E NET ATIVA\BASES GEVENUE"
    arquivos = glob.glob(caminho + "/*.dat")

    header_gevenue = ["SENHA","AGENCIA","NOME","CPF/CNPJ","TIPO_PESSOA","SCORE_DEVEDOR","DATA_AGENDA","HORA_AGENDA","VLR_NET_TV_VIRTUA","VLR_NET_FONE","VLR_CLR_MOVEL","VLR_CLR_TV",
                    "VLR_CLR_FIXO","VLR_TOTAL","AGING","EMAIL","CONTRATO",
                    "TIPO_TELEFONE","DDI","DDD","TELEFONE","RAMAL",
                    "TIPO_TELEFONE.1","DDI.1","DDD.1","TELEFONE.1","RAMAL.1",
                            "TIPO_TELEFONE.2","DDI.2","DDD.2","TELEFONE.2","RAMAL.2",
                            "TIPO_TELEFONE.3","DDI.3","DDD.3","TELEFONE.3","RAMAL.3",
                            "TIPO_TELEFONE.4","DDI.4","DDD.4","TELEFONE.4","RAMAL.4",
                            "TIPO_TELEFONE.5","DDI.5","DDD.5","TELEFONE.5","RAMAL.5",
                            "TIPO_TELEFONE.6","DDI.6","DDD.6","TELEFONE.6","RAMAL.6",
                            "TIPO_TELEFONE.7","DDI.7","DDD.7","TELEFONE.7","RAMAL.7"]

    #Lista de larguras do layout NET COB
    lista = []
    for arquivo in arquivos:
        print(arquivo)
        lista.append(arquivo)
        
        dfList = []
        
        for item in lista:   
            chunks = pd.read_csv(item, encoding='iso-8859-1', chunksize=500000, sep=";", dtype='str',names=header_gevenue)
            for df in chunks:
                dfList.append(df)
                
    ###########################################################################################################################################    

    # Criando DataFrame com concat e a lista criada a cima
    base_gevenue = pd.concat(dfList, sort=False, ignore_index=False)
    pd.set_option("display.max_columns", None)

    # TRATANDO CPF E CNPJ, INCLUINDO ZEROS A ESQUERDA.
    df_cpfs_correto = base_gevenue[base_gevenue['CPF/CNPJ'].str.len()==11]
    df_cnpjs_correto = base_gevenue[base_gevenue['CPF/CNPJ'].str.len()==14]
    df_cpfs_corrigir = base_gevenue[base_gevenue['CPF/CNPJ'].str.len()<11]
    df_cpfs_corrigir['CPF/CNPJ'] = df_cpfs_corrigir['CPF/CNPJ'].apply(lambda x: '{0:0>11}'.format(x))
    df_cnpj_corrigir = base_gevenue[base_gevenue['CPF/CNPJ'].str.len()>11]
    df_cnpj_corrigir['CPF/CNPJ']  = df_cnpj_corrigir['CPF/CNPJ'].apply(lambda x: '{0:0>14}'.format(x))
    base_gevenue = pd.concat([df_cpfs_correto,df_cpfs_correto,df_cpfs_corrigir,df_cnpj_corrigir],ignore_index=True)\
    .drop_duplicates(['CPF/CNPJ','AGING','VLR_TOTAL'])

    # Dropar a coluna "AGENCIA"
    base_gevenue = base_gevenue.drop('AGENCIA', axis=1)


    base_gevenue = base_gevenue.loc[:,['CPF/CNPJ','SENHA','NOME','DDD', 'TELEFONE','DDD.1', 'TELEFONE.1','DDD.2', 'TELEFONE.2','DDD.3', 'TELEFONE.3',
                                    'DDD.4', 'TELEFONE.4','DDD.5', 'TELEFONE.5','DDD.6', 'TELEFONE.6','DDD.7', 'TELEFONE.7','EMAIL','AGING','VLR_TOTAL']]

    base_gevenue = base_gevenue.assign(OPERACAO="GEVENUE")

    gevenue_1 = base_gevenue.loc[:,['CPF/CNPJ','SENHA','NOME','DDD','TELEFONE','EMAIL','AGING','VLR_TOTAL','OPERACAO']]
    gevenue_2 = base_gevenue.loc[:,['CPF/CNPJ','SENHA','NOME','DDD.1','TELEFONE.1','EMAIL','AGING','VLR_TOTAL','OPERACAO']]
    gevenue_3 = base_gevenue.loc[:,['CPF/CNPJ','SENHA','NOME','DDD.2','TELEFONE.2','EMAIL','AGING','VLR_TOTAL','OPERACAO']]
    gevenue_4 = base_gevenue.loc[:,['CPF/CNPJ','SENHA','NOME','DDD.3','TELEFONE.3','EMAIL','AGING','VLR_TOTAL','OPERACAO']]
    gevenue_5 = base_gevenue.loc[:,['CPF/CNPJ','SENHA','NOME','DDD.4','TELEFONE.4','EMAIL','AGING','VLR_TOTAL','OPERACAO']]
    gevenue_6 = base_gevenue.loc[:,['CPF/CNPJ','SENHA','NOME','DDD.5','TELEFONE.5','EMAIL','AGING','VLR_TOTAL','OPERACAO']]
    gevenue_7 = base_gevenue.loc[:,['CPF/CNPJ','SENHA','NOME','DDD.6','TELEFONE.6','EMAIL','AGING','VLR_TOTAL','OPERACAO']]
    gevenue_8 = base_gevenue.loc[:,['CPF/CNPJ','SENHA','NOME','DDD.7','TELEFONE.7','EMAIL','AGING','VLR_TOTAL','OPERACAO']]


    # RENOMEANDO PRA CONCATENAR
    gevenue_2 = gevenue_2.rename(columns={'DDD.1':'DDD'})
    gevenue_3 = gevenue_3.rename(columns={'DDD.2':'DDD'})
    gevenue_4 = gevenue_4.rename(columns={'DDD.3':'DDD'})
    gevenue_5 = gevenue_5.rename(columns={'DDD.4':'DDD'})
    gevenue_6 = gevenue_6.rename(columns={'DDD.5':'DDD'})
    gevenue_7 = gevenue_7.rename(columns={'DDD.6':'DDD'})
    gevenue_8 = gevenue_8.rename(columns={'DDD.7':'DDD'})

    # RENOMEANDO PRA CONCATENAR
    gevenue_2 = gevenue_2.rename(columns={'TELEFONE.1':'TELEFONE'})
    gevenue_3 = gevenue_3.rename(columns={'TELEFONE.2':'TELEFONE'})
    gevenue_4 = gevenue_4.rename(columns={'TELEFONE.3':'TELEFONE'})
    gevenue_5 = gevenue_5.rename(columns={'TELEFONE.4':'TELEFONE'})
    gevenue_6 = gevenue_6.rename(columns={'TELEFONE.5':'TELEFONE'})
    gevenue_7 = gevenue_7.rename(columns={'TELEFONE.6':'TELEFONE'})
    gevenue_8 = gevenue_8.rename(columns={'TELEFONE.7':'TELEFONE'})


    base_gevenue = pd.concat([gevenue_1,gevenue_2,gevenue_3,gevenue_4,gevenue_5,gevenue_6,gevenue_7,gevenue_8])
    base_gevenue['TELEFONE'] = base_gevenue['DDD'] + base_gevenue['TELEFONE']

    # FILTRANDO APENAS AS COLUNAS COM TELEFONE, POIS A BASE DA INTERSIC TEM MUITA LINHA NAN
    base_gevenue = base_gevenue.query("TELEFONE.notnull()")
    base_gevenue = base_gevenue.rename(columns={'OPERACAO':'BASE'})
    base_gevenue = base_gevenue.rename(columns={'CPF/CNPJ':'CPF'})
    base_gevenue = base_gevenue.rename(columns={'SENHA':'DEVEDOR'})
    base_gevenue = base_gevenue.loc[:,['CPF','DEVEDOR','NOME','TELEFONE','EMAIL','AGING','VLR_TOTAL','BASE']]
    base_gevenue = base_gevenue.rename(columns={'AGING':'ATRASO'})
    base_gevenue = base_gevenue.rename(columns={'VLR_TOTAL':'SALDO_ABERTO'})

    base_gevenue['ATRASO'] = base_gevenue['ATRASO'].astype('int32')
    base_gevenue = base_gevenue.sort_values(['ATRASO','BASE'],ascending=True)
    return base_gevenue


caminho = r"R:\TI\TELEFONIA\Mailings Prontos\2023\Maio\24"
filename_claro = "BASES_CLARO"
filename_net = "BASES_NET"
filename_gevenue = "BASES_GEVENUE"
filepath_claro = fr"{caminho}\{filename_claro}.csv"
filepath_net = fr"{caminho}\{filename_net}.csv"
filepath_gevenue = fr"{caminho}\{filename_gevenue}.csv"


def download_csv(dataframe, filename, filepath):
    csv = dataframe.to_csv(index=False, sep=";", line_terminator="\n")
    b64 = base64.b64encode(csv.encode()).decode()

    # Salvar o arquivo CSV no caminho especificado
    with open(filepath, "w", encoding="iso-8859-1") as f:
        f.write(csv)

    href = f'<a href="file://{filepath}" download="{filename}.csv" style="text-decoration: none; color: green; font-size: 20px;">Download {filename} Realizado !</a>'
    return href


st.title("Carregamento de Bases de Dados")



# Crie duas colunas para os botões de carregamento da 
tab1, tab2, tab3 = st.tabs(["📈 CLARO", "🗃 NET", "GEVENUE"])

if tab1.button("CARREGAR BASE CLARO"):
    url_imagem = "https://files.tecnoblog.net/wp-content/uploads/2015/04/claro-logotipo-marca-700x394.png"
    # Exibir a imagem centralizada
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(url_imagem, caption="A Base da claro foi totalmente padronizada, foi mudado o layout da INTERSIC para o layout padrão.")
    
    with st.spinner("Carregando..."):
        bases_claro = carregar_bases_claro()
        st.subheader("Base Claro carregada com sucesso!")
        st.write(bases_claro.head(5))
        st.markdown(download_csv(bases_claro, "BASES_CLARO", filepath_claro), unsafe_allow_html=True)
        st.success("Normalização da Base Claro feita com sucesso!")
        if st.button("Refresh"):
            st.experimental_rerun()

if tab2.button("CARREGAR BASE NET"):
    url_imagem = "https://vendamuitomais.com.br/wp-content/uploads/2016/02/net_logo21.png"
    # Exibir a imagem centralizada
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(url_imagem, caption="A Base da Net foi totalmente padronizada, foi mudado o layout da INTERSIC para o layout padrão.")
    
    with st.spinner("Carregando..."):
        bases_net = carregar_bases_net()
        st.write("Base Net carregada com sucesso!")
        st.write(bases_net.head(5))
        st.markdown(download_csv(bases_net, "BASES_NET", filepath_net), unsafe_allow_html=True)
        st.success("Normalização da Base Net feita com sucesso!")
        if st.button("Refresh"):
            st.experimental_rerun()

if tab3.button("CARREGAR BASE GEVENUE"):
    url_imagem = "gevenue.png"
    # Exibir a imagem centralizada
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(url_imagem, caption="A Base da Gevenue foi totalmente padronizada, foi mudado o layout da GEVENUE para o layout padrão.")
    
    with st.spinner("Carregando..."):
        base_gevenue = carregar_base_gevenue()
        st.write("Base Gevenue carregada com sucesso!")
        st.write(base_gevenue.head(5))
        st.markdown(download_csv(base_gevenue, "BASES_GEVENUE", filepath_gevenue),unsafe_allow_html=True)
        st.success("Normalização da Base Gevenue feita com sucesso!")
        if st.button("Refresh"):
            st.experimental_rerun()





#                                              ############################# ENTRELACES #######################


# Função para carregar o DataFrame
def entrelace_de_bases():
    warnings.filterwarnings('ignore')
    pd.set_option("display.max_columns", None)

    #################################################### CARERGANDO A BASE QUE FOI NORMALIZADA QUE COMPREENDE A TODAS AS EQUIPES DO HUGO (CLAROS/NET/GEVENUE)

    caminho = r"R:\TI\TELEFONIA\BASES CLARO E NET ATIVA\BASES SEMANA PADRAO"
    arquivos = glob.glob(caminho + "/*.csv")
    lista = []
    for arquivo in arquivos:
        print(arquivo)
        lista.append(arquivo)
        
        dfList = []
        
        for item in lista:   
            chunks = pd.read_csv(item, encoding='iso-8859-1', chunksize=1000000, sep=";", dtype='str')
            for df in chunks:
                dfList.append(df)

    # Criando DataFrame com concat e a lista criada a cima
    df_telecobs_hugo = pd.concat(dfList, sort=False, ignore_index=False)



    #################################################### CARERGANDO A BASE DE TELEFONES HIGIENIZADOS

    caminho = r"R:\TI\TELEFONIA\BASES_HIGIENIZADAS_CLARO_E_NET\TELEFONES CLARO E NET"
    arquivos = glob.glob(caminho + "/*.csv")
    lista = []
    for arquivo in arquivos:
        print(arquivo)
        lista.append(arquivo)
        
        dfList = []
        
        for item in lista:   
            chunks = pd.read_csv(item, encoding='iso-8859-1', chunksize=1000000, sep=";", dtype='str')
            for df in chunks:
                dfList.append(df)

    # Criando DataFrame com concat e a lista criada a cima
    telefones_higienizados = pd.concat(dfList, sort=False, ignore_index=False)
    telefones_higienizados = telefones_higienizados.rename(columns={'TELEFONE':'TELEFONE_HIGIENIZADO'})

    ######################################################  BASE NORMALIZADA X TELEFONES HIGIENIZADOS  ######################################################

    df_telecobs_hugo = pd.merge(df_telecobs_hugo, telefones_higienizados, right_on=['CPF'], left_on=['CPF'], how="left")\
    .loc[:,['CPF','DEVEDOR','NOME_x','TELEFONE','EMAIL','ATRASO','SALDO_ABERTO','BASE','TELEFONE_HIGIENIZADO']]

    ### REMOVENDO DUPLICADOS DEPOIS DO CRUZAMENTO, PARA EVITAR NOS PROXIMOS CRUZAMENTOS TER VARIOS CPF'S IGUAIS DESNCESSARIAMENTE.
    df_telecobs_hugo = df_telecobs_hugo.drop_duplicates(['CPF','DEVEDOR', 'NOME_x', 'TELEFONE', 'EMAIL','ATRASO', 'BASE', 'TELEFONE_HIGIENIZADO'])




    #################################################### CARERGANDO A BASE DE EMAILS HIGIENIZADOS

    caminho = r"R:\TI\TELEFONIA\BASES_HIGIENIZADAS_CLARO_E_NET\EMAILS CLARO E NET"
    arquivos = glob.glob(caminho + "/*.csv")
    lista = []
    for arquivo in arquivos:
        print(arquivo)
        lista.append(arquivo)
        
        dfList = []
        
        for item in lista:   
            chunks = pd.read_csv(item, encoding='iso-8859-1', chunksize=1000000, sep=";", dtype='str')
            for df in chunks:
                dfList.append(df)

    # Criando DataFrame com concat e a lista criada a cima
    emails_higienizados = pd.concat(dfList, sort=False, ignore_index=False)
    emails_higienizados = emails_higienizados.rename(columns={'EMAIL':'EMAIL_HIGIENIZADO'})


    ######################################################  BASE NORMALIZADA X EMAILS HIGIENIZADOS  ######################################################

    df_telecobs_hugo = pd.merge(df_telecobs_hugo, emails_higienizados, right_on=['CPF'], left_on=['CPF'], how="left")\
    .loc[:,['CPF','DEVEDOR','NOME_x','TELEFONE','EMAIL','ATRASO','SALDO_ABERTO','BASE','TELEFONE_HIGIENIZADO','EMAIL_HIGIENIZADO']]

    ### REMOVENDO DUPLICADOS DEPOIS DO CRUZAMENTO, PARA EVITAR NOS PROXIMOS CRUZAMENTOS TER VARIOS CPF'S IGUAIS DESNCESSARIAMENTE.
    df_telecobs_hugo = df_telecobs_hugo.drop_duplicates(['CPF','DEVEDOR', 'NOME_x', 'TELEFONE', 'EMAIL','ATRASO', 'BASE', 'TELEFONE_HIGIENIZADO', 'EMAIL_HIGIENIZADO'])


    #################################################### CARERGANDO A BASE DE VALIDADOS

    caminho = r"R:\TI\TELEFONIA\BASE DE VALIDADOS"
    arquivos = glob.glob(caminho + "/*.csv")
    lista = []
    for arquivo in arquivos:
        print(arquivo)
        lista.append(arquivo)
        
        dfList = []
        
        for item in lista:   
            chunks = pd.read_csv(item, encoding='iso-8859-1', chunksize=1000000, sep=";", dtype='str',usecols=['Numero', 'Usa whatsapp', 'data de envio'])
            for df in chunks:
                dfList.append(df)

    # Criando DataFrame com concat e a lista criada a cima
    telefones_validados = pd.concat(dfList, sort=False, ignore_index=False)


    ######################################################  BASE NORMALIZADA X TELEFONES INTERSIC E GEVENUE  ######################################################

    df_telecobs_hugo = pd.merge(df_telecobs_hugo, telefones_validados, right_on=['Numero'], left_on=['TELEFONE'], how="left")\
    .loc[:,['CPF','DEVEDOR','NOME_x','TELEFONE','Usa whatsapp','data de envio','EMAIL','ATRASO','SALDO_ABERTO','BASE','TELEFONE_HIGIENIZADO','EMAIL_HIGIENIZADO']]

    ############ APÓS O CRUZAMENTO, MARCAMOS COMO "NAO_VALIDADO" A BASE QUE NÃO FOI ENCONTRADA NO BANCO DE VALIDOS OU NAO.
    ########## RENOMEANDO A COLUNA SE USA WHATSS PARA IDENTIFICAR QUE A VALIDAÇÃO É REFERENTE A BASE DE CONTRATANTE / DATA DA VALIDACAO TAMBEM
    df_telecobs_hugo['Usa whatsapp'] = df_telecobs_hugo['Usa whatsapp'].fillna('Nao_Validado')
    df_telecobs_hugo = df_telecobs_hugo.rename(columns={'Usa whatsapp':'BASE_CONTRATANTE_VALIDADOS'})
    df_telecobs_hugo = df_telecobs_hugo.rename(columns={'data de envio':'DATA_VALIDACAO_CONTRATANTE'})

    ######################################################  BASE NORMALIZADA X TELEFONES HIGIENIZADOS  ######################################################

    df_telecobs_hugo = pd.merge(df_telecobs_hugo, telefones_validados, right_on=['Numero'], left_on=['TELEFONE_HIGIENIZADO'], how="left")\
    .loc[:,['CPF','DEVEDOR','NOME_x','TELEFONE','BASE_CONTRATANTE_VALIDADOS','DATA_VALIDACAO_CONTRATANTE','EMAIL','ATRASO','SALDO_ABERTO','BASE',
            'TELEFONE_HIGIENIZADO','Usa whatsapp','data de envio','EMAIL_HIGIENIZADO']]

    ############ APÓS O CRUZAMENTO, MARCAMOS COMO "NAO_VALIDADO" A BASE QUE NÃO FOI ENCONTRADA NO BANCO DE VALIDOS OU NAO.
    df_telecobs_hugo['Usa whatsapp'] = df_telecobs_hugo['Usa whatsapp'].fillna('Nao_Validado')
    ############ APÓS O CRUZAMENTO, MARCAMOS COMO "NAO_VALIDADO" A BASE QUE NÃO FOI ENCONTRADA NO BANCO DE VALIDOS OU NAO.
    ########## RENOMEANDO A COLUNA SE USA WHATSS PARA IDENTIFICAR QUE A VALIDAÇÃO É REFERENTE A BASE DE CONTRATANTE / DATA DA VALIDACAO TAMBEM
    df_telecobs_hugo = df_telecobs_hugo.rename(columns={'Usa whatsapp':'BASE_HIGI_VALIDADOS'})
    df_telecobs_hugo = df_telecobs_hugo.rename(columns={'data de envio':'DATA_VALIDACAO_HIGI'})




    ### REMOVENDO DUPLICADOS DEPOIS DO CRUZAMENTO, PARA EVITAR NOS PROXIMOS CRUZAMENTOS TER VARIOS CPF'S IGUAIS DESNCESSARIAMENTE.
    df_telecobs_hugo = df_telecobs_hugo.drop_duplicates(['CPF','DEVEDOR', 'NOME_x', 'TELEFONE', 'EMAIL','ATRASO', 'BASE', 'TELEFONE_HIGIENIZADO','EMAIL_HIGIENIZADO'])
    return df_telecobs_hugo



st.markdown("---")

# Título do aplicativo
st.title("Entrelace das Bases")

##### baixando a base entrelaçada
caminho_base_operacional = r"R:\TI\TELEFONIA\Mailings Prontos\2023\Maio\24"
filename_base_operacional = "BASE_OPERACIONAL_TELECOB_HUGO"
filepath_base_operacional = fr"{caminho_base_operacional}\{filename_base_operacional}.txt"

def download_txt_entrelacada(dataframe, filename, filepath):
    txt = dataframe.to_csv(index=False, sep=";", encoding="utf-8", line_terminator="\n")
    b64 = base64.b64encode(txt.encode()).decode()

    # Salvar o arquivo TXT no caminho especificado
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(txt)

    href = f'<a href="file://{filepath}" download="{filename}.txt" style="text-decoration: none; color: green; font-size: 22px;">Download {filename} Realizado!</a>'
    return href


# Botão para carregar a base normalizada
if st.button("Carregar Base Normalizada"):
    with st.spinner("Carregando..."):
        df_telecobs_hugo = entrelace_de_bases()
        st.success("A base normalizada foi carregada")
        st.write(df_telecobs_hugo.head(10))
        st.markdown(download_txt_entrelacada(df_telecobs_hugo, "BASE_OPERACIONAL_TELECOB_HUGO", filepath_base_operacional),unsafe_allow_html=True)
        if st.button("Refresh"):
            st.experimental_rerun()   