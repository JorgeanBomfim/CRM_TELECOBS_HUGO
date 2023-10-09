import streamlit as st
from streamlit_option_menu import option_menu



############### VISUAL ############
st.set_page_config(
    page_title="CRM TELECOB'S",
    page_icon="py-removebg-preview.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    selected = option_menu("Menu", ["INICIO", 'RELATÓRIOS', 'DASHBOARDS', 'HIGIENIZAÇÕES' ], 
        icons=['house','info-square', 'graph-up-arrow','database-lock'], menu_icon="incognito", default_index=1)



# Função para exibir o conteúdo da página de início
def pagina_inicio():
    st.text("""
                Bem-Vindo ao Sistema de Telecobrança
                Você está prestes a entrar em uma ferramenta poderosa que vai revolucionar a forma como você gerencia suas equipes de telecobrança e aprimora o relacionamento com seus clientes. O Sistema de Telecobrança é a solução completa para transformar dados em insights e ações eficazes.
                Nossas Funcionalidades Principais:
                1. Dashboards Dinâmicos:
                Acompanhe em tempo real o desempenho de suas equipes.
                Visualize métricas-chave e indicadores de desempenho de forma clara e intuitiva.
                Tome decisões informadas com base em dados precisos e atualizados.
                2. Relatórios Consolidados:
                Acesse relatórios detalhados com números consolidados de bases, saldos e outros dados fundamentais.
                Analise tendências ao longo do tempo para planejar estratégias eficazes.
                3. Higienização de Bases:
                Mantenha suas bases de contatos atualizadas e otimizadas.
                Melhore a qualidade da localização de clientes para um atendimento mais eficiente.
                Com o nosso sistema, você terá as ferramentas necessárias para impulsionar o sucesso da sua equipe de telecobrança. Estamos comprometidos em simplificar o gerenciamento de dados e transformá-los em ações concretas.

                Vamos começar!

                Faça login agora para explorar todas as funcionalidades do Sistema de Telecobrança. Se você é novo aqui, não se preocupe. Nossa interface é intuitiva e fácil de usar. Estamos aqui para apoiá-lo em cada etapa do caminho.

                Estamos ansiosos para ajudá-lo a atingir seus objetivos de telecobrança e a elevar o nível de excelência em sua empresa.

                Equipe do Sistema de Telecobrança""" )


# Função para exibir o conteúdo da página de relatórios
def pagina_relatorios():
    st.write("Página de Relatórios")
    # Adicione aqui qualquer conteúdo relacionado aos relatórios.

# Função para exibir o conteúdo da página de dashboards
def pagina_dashboards():
    st.write("Página de Dashboards")
    # Adicione aqui qualquer conteúdo relacionado aos dashboards.

# Função para exibir o conteúdo da página de higienizações
def pagina_higienizacoes():
    st.write("Página de Higienizações")
    # Adicione aqui qualquer conteúdo relacionado às higienizações.

# Conteúdo principal com base na seleção do menu
if selected == "INICIO":
    pagina_inicio()
elif selected == "RELATÓRIOS":
    pagina_relatorios()
elif selected == "DASHBOARDS":
    pagina_dashboards()
elif selected == "HIGIENIZAÇÕES":
    pagina_higienizacoes()



