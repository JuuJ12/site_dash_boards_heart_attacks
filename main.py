import streamlit as st



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


st.sidebar.text('Make By Julio Santos With Streamlit.')

pagina.run()

