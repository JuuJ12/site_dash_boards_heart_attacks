import streamlit as st
# from pag.Análise_Exploratória import buildPage
# from pag.Agrupamento_Clusterização import buildPage_clusterizacao
# from pag.me import build_page_me


st.set_page_config(
    page_title='Sobre Mim',
    layout="centered",
    menu_items={
        'About' : '''teste'''
    }
       
)

pag1 = st.Page(
    page= "pag/me.py",
    title="Sobre Mim",
    icon=':material/mail:',
    default= True
)


pag2 = st.Page(
    page="pag/Análise_Exploratória.py",
    title='Gráficos',
    icon='📊'
)

pag3 = st.Page(
    page= "pag/Agrupamento_Clusterização.py",
    title="Agrupamento",
    icon= '🔍'
)



pagina= st.navigation({
        "Info":[pag1],
        "Dashboards":[pag2],
        "Clusterização":[pag3]
    }
)

pagina.run()

