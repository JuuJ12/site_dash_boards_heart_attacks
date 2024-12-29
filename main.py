import streamlit as st
from Pages.Análise_Exploratória import buildPage
from Pages.Agrupamento_Clusterização import buildPage_clusterizacao
from Pages.me import build_page_me


# st.set_page_config(
#     page_title='Sobre Mim',
#     layout="wide",
#     menu_items={
#         'About' : '''teste'''
#     }
       
# )

pag1 = st.Page(
    page= "Pages/me.py",
    title="Sobre Mim",
    icon=':material/mail:',
    default= True
)


pag2 = st.Page(
    page="Pages/Análise_Exploratória.py",
    title='Gráficos',
    icon='📊'
)

pag3 = st.Page(
    page= "Pages/Agrupamento_Clusterização.py",
    title="Agrupamento",
    icon= '🔍'
)


#pagina= st.navigation(Pages=[pag1,pag2])

pagina= st.navigation({
        "Info":[pag1],
        "Dashboards":[pag2],
        "Clusterização":[pag3]
    }
)

pagina.run()

