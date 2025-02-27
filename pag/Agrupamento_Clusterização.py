import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from utils import readDataframe_parquet, labels, rename_colunas

import matplotlib.pyplot as plt

from sklearn.decomposition import PCA


dfp= readDataframe_parquet()
dfp_c = pd.read_parquet('data/clusters_kmodes.parquet')
dfp_c2= pd.read_parquet('data/clusters_kmeans.parquet')
dfp_c= dfp_c.rename(columns={'Cluster':'Clusters'})
dfp_c['HeartDiseaseorAttack'] = dfp['HeartDiseaseorAttack']
dfp_c2['HeartDiseaseorAttack'] = dfp['HeartDiseaseorAttack']
dfp_c_labels=labels(dfp_c.copy())
dfp_c2_labels= labels(dfp_c2.copy())

st.title('Clusterização K-means e K-modes')
def analise_clusters():
    with st.expander('Notas'):
        st.write('Através do método do cotovelo e silhueta foi definido que o melhor número de clusters é 4.')
        col1,col2= st.columns(2)
        with col1:
            st.image('data/cotovelo_kmodes.png', caption='Cotovelo do KModes')
            st.image('data/silhouette_score_kmodes.png', caption='Silhouette Score KModes')
        with col2:
            st.image('data/cotovelo_kmeans.png', caption='Cotovelo do KMeans')
            st.image('data/silhouette_score_kmeans.png', caption='Silhouette Score KMeans')

    with st.expander('Analise dos Clusters (KModes)'):
        col1, col2 = st.columns([0.3, 0.7])

        with col1:
            analise_cluster_kmodes = dfp_c.copy().groupby('Clusters').mean() * 100
            analise_cluster_kmodes = rename_colunas(analise_cluster_kmodes)

            for cluster in analise_cluster_kmodes.index:
                st.subheader(f"Cluster {cluster} KModes")
                formatted_df = analise_cluster_kmodes.loc[cluster].reset_index().rename(
                    columns={'index': 'Característica', cluster: 'Percentual (%)'}
                )
                formatted_df['Percentual (%)'] = formatted_df['Percentual (%)'].map(lambda x: f'{x:.2f}%')
                
                st.dataframe(formatted_df)

        with col2:
            for cluster in analise_cluster_kmodes.index:
                sorted_df = analise_cluster_kmodes.loc[cluster].reset_index().sort_values(by=cluster, ascending=False)
                fig = px.bar(
                    sorted_df,
                    x=cluster,  
                    y='index',  
                    labels={'index': 'Característica',
                        '0': f'Porcentagem do Grupo {cluster}','1': f'Porcentagem do Grupo {cluster}','2': f'Porcentagem do Grupo {cluster}',
                        '3': f'Porcentagem do Grupo {cluster}'},
                    title=f"Distribuição de Características no Cluster {cluster} (KModes)",
                    orientation='h'  
                )
                st.plotly_chart(fig)

        st.subheader("Resumo Geral dos Percentuais dos Clusters")
        analise_cluster_kmodes_transposed = analise_cluster_kmodes.T
        analise_cluster_kmodes_transposed.columns = [f'Grupo {i}' for i in range(len(analise_cluster_kmodes_transposed.columns))]
        formatted_kmodes_transposed = analise_cluster_kmodes_transposed.applymap(lambda x: f'{x:.2f}%')
        st.table(formatted_kmodes_transposed)



    with st.expander('Analise dos Clusters (KMeans)'):
        col1, col2 = st.columns([0.3, 0.7])

        with col1:
            analise_cluster_kmeans = dfp_c2.copy().groupby('Clusters').mean() * 100
            analise_cluster_kmeans = rename_colunas(analise_cluster_kmeans)

            for cluster in analise_cluster_kmeans.index:
                st.subheader(f"Cluster {cluster} KMeans")
                formatted_df = analise_cluster_kmeans.loc[cluster].reset_index().rename(
                    columns={'index': 'Característica', cluster: 'Percentual (%)'}
                )
                formatted_df['Percentual (%)'] = formatted_df['Percentual (%)'].map(lambda x: f'{x:.2f}%')
                
                st.dataframe(formatted_df)

        with col2:
            for cluster in analise_cluster_kmeans.index:
                sorted_df = analise_cluster_kmeans.loc[cluster].reset_index().sort_values(by=cluster, ascending=False)
                fig = px.bar(
                    sorted_df,
                    x=cluster,  
                    y='index',  
                    labels={
                        'index': 'Característica',
                        '0': f'Porcentagem do Grupo {cluster}','1': f'Porcentagem do Grupo {cluster}','2': f'Porcentagem do Grupo {cluster}',
                        '3': f'Porcentagem do Grupo {cluster}'
                    },
                    title=f"Distribuição de Características no Cluster {cluster} (KMeans)",
                    orientation='h'  
                )
                st.plotly_chart(fig)

        st.subheader("Resumo Geral dos Percentuais dos Clusters")
        analise_cluster_kmeans_transposed = analise_cluster_kmeans.T
        analise_cluster_kmeans_transposed.columns = [f'Grupo {i}' for i in range(len(analise_cluster_kmeans_transposed.columns))]
        formatted_kmeans_transposed = analise_cluster_kmeans_transposed.applymap(lambda x: f'{x:.2f}%')
        st.table(formatted_kmeans_transposed)





dfp_c_labels=labels(dfp_c.copy())
dfp_c2_labels= labels(dfp_c2.copy())

def grafico1():
    st.subheader('Histogramas Relacionados aos Clusters Apenas de Hábitos e Características dos Individuos')

    
    nome_colunas = ['Problemas Cardíacos', 'Fumantes', "Pratica Atividade Física", 'Sexo', 'Saúde Boa',
                    'Saúde Excelente', 'Saúde Moderada', 'Saúde Pobre', 'Saúde Ruim',
                    'Consumo de Frutas', 'Consumo de Legumes e Verduras','Idade Entre 18-24','Idade entre 25-29','Idade Entre 30-34',
                    'Idade Entre 35-39','Idade Entre 40-44','Idade Entre 45-49','Idade Entre 50-54','Idade Entre 55-59','Idade Entre 60-64',
                    'Idade Entre 65-69','Idade Entre 70-74','Idade Entre 75-79','Idade 80+']

   
    colunas = st.selectbox('Colunas', options=nome_colunas, key='histograma')
    
    
    col1, col2 = st.columns(2)
    
    
    cores_clusters = {'Grupo 0': '#636EFA', 'Grupo 1': '#19D3F3', 'Grupo 2': '#1f77b4','Grupo 3':'#00FA9A'}
    
   
    button_input = st.button('Gerar Gráfico')
    
    if button_input:
        with col1:
            st.subheader('Histograma 1 KModes')
            
            
            fig = px.histogram(dfp_c_labels, x=colunas, color='Clusters', 
                               title=f'Distribuição de {colunas} por Cluster (KModes)',
                               color_discrete_map=cores_clusters,
                               category_orders={'Clusters': ['Grupo 0', 'Grupo 1', 'Grupo 2']})  
            fig.update_layout(barmode='group',yaxis_title='Quantidade')
            fig.update_traces(texttemplate='%{y}', textposition='auto')
            st.plotly_chart(fig)

        with col2:
            st.subheader('Histograma 2 KMeans')
            fig = px.histogram(dfp_c2_labels, x=colunas, color='Clusters', 
                               title=f'Distribuição de {colunas} por Cluster (KMeans)',
                               color_discrete_map=cores_clusters,
                               category_orders={'Clusters': ['Grupo 0', 'Grupo 1', 'Grupo 2']})  
            fig.update_layout(barmode='group',yaxis_title='Quantidade')
            fig.update_traces(texttemplate='%{y}', textposition='auto')
            st.plotly_chart(fig)
 



def dispersao():
    st.subheader('Gráficos de Dispersão Apenas de Hábitos e Características dos Individuos')
    
    
    cores_clusters = {'Grupo 0': '#636EFA', 'Grupo 1': '#19D3F3', 'Grupo 2': '#1f77b4', 'Grupo 3':'#00FA9A'}
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write('Gráficos de Dispersão dos Clusters com PCA (KModes)')
        
        
        pca = PCA(n_components=2)
        df_pca = pca.fit_transform(dfp_c)
        df_pca = pd.DataFrame(df_pca, columns=['PCA1', 'PCA2'])
        df_pca['Clusters'] = dfp_c['Clusters'].map(lambda x: f'Grupo {x}')  
        
       
        fig = px.scatter(df_pca, x='PCA1', y='PCA2', color='Clusters',
                        title='Clusters KModes visualizados em 2D usando PCA',
                        color_discrete_map=cores_clusters,
                        category_orders={'Clusters': ['Grupo 0', 'Grupo 1', 'Grupo 2']})  
        
        fig.update_layout(xaxis_title='PCA Componente 1',
                          yaxis_title='PCA Componente 2')
        
        st.plotly_chart(fig)
    
    with col2:
        st.write('Gráficos de Dispersão dos Clusters com PCA (KMeans)')
        
        
        pca = PCA(n_components=2)
        df_pca = pca.fit_transform(dfp_c2)
        df_pca = pd.DataFrame(df_pca, columns=['PCA1', 'PCA2'])
        df_pca['Clusters'] = dfp_c2['Clusters'].map(lambda x: f'Grupo {x}')
        
       
        fig = px.scatter(df_pca, x='PCA1', y='PCA2', color='Clusters',
                        title='Clusters KMeans visualizados em 2D usando PCA',
                        color_discrete_map=cores_clusters,
                        category_orders={'Clusters': ['Grupo 0', 'Grupo 1', 'Grupo 2']})  
        
        fig.update_layout(xaxis_title='PCA Componente 1',
                          yaxis_title='PCA Componente 2')
        
        st.plotly_chart(fig)



def mapa_calor(df1,df2):
    st.subheader('Mapas de Calor (HeatMaps)')
    df1=rename_colunas(df1)
    df2=rename_colunas(df2)
    col1,col2= st.columns(2)
    df_cluster_corr = (df1.corr())
    df_cluster_corr2 = df2.corr()
    
    with col1:
        st.write('Heatmap de Correlação KModes')
        plt.figure(figsize=(10,8))
        sns.heatmap(df_cluster_corr, annot=False, cmap='coolwarm', linewidths=0.5)
        plt.title("Heatmap de Correlação entre Variáveis de Hábitos e Características dos Individuos")
        st.pyplot(plt)
        
    with col2:
        st.write('Heatmap de Correlação KMeans')
        plt.figure(figsize=(10,8))
        sns.heatmap(df_cluster_corr2, annot=False, cmap='coolwarm', linewidths=0.5)
        plt.title("Heatmap de Correlação entre Variáveis de Hábitos e Características dos Individuos")
        st.pyplot(plt)



def buildPage_clusterizacao():
    analise_clusters()
    grafico1()
    dispersao()
    mapa_calor(dfp_c,dfp_c2)

buildPage_clusterizacao()

