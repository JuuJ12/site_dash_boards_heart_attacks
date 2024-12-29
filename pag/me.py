import streamlit as st



st.title('Sobre Mim')
def formulario():
    st.title('Escreve Sua Mensagem:e-mail:')
    formulario_de_contato = """
        <form action="https://formsubmit.co/juliovitortb99@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder ="Seu Nome" required>
        <input type="email" name="email" placeholder="Seu Email">
        <textarea name="message" placeholder="Escreva Sua Mensagem"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(formulario_de_contato, unsafe_allow_html=True)
    
def perfil():
    col1,col2=st.columns([0.4,0.6], gap='small',vertical_alignment='center')

    with col1:
        st.image('pictures/perfil_foto.png', caption='Julio Vitor dos Santos')
    with col2:
            st.write('''- Técnico em Análise de Desenvolvimento de Sistemas.''')
            st.write('''- Cursando Bacharelado em Sistemas de Informação.''')
            with st.expander('Experiencias'):
             st.write('''
                   - Análise e mineração de dados em bases diversas, como aquelas envolvendo filmes e séries, e dados médicos de pacientes com problemas cardíacos.
                   - Aplicação modelos de Machine Learning para recomendações de filmes e séries, bem como para a previsão de doenças cardíacas.
                   - Desenvolvimento de sistemas web utilizando o framework Streamlit, criando interfaces para operações CRUD.
                   - Desenvolvimento de sistemas web utilizando o framework Streamlit, criando interfaces gráficas interativas para visualização de dados.
                   - Criação de Agentes de AI para resolução de Problemas.
                   - Modelagem de Banco de Dados.
                   ''')
            with st.expander("Certificados"):
                 st.write('''
                            - AWS Academy Graduate - AWS Academy Cloud Foundations.
                            - AWS Academy Graduate - AWS Academy Machine Learning Foundations.
                            - AWS Academy Graduate - AWS Academy Cloud Web Application Builder.
                            - Programa Ganhe o Mundo(Idioma Inglês) - Nível Básico 1 e 2.
                            - Programa Ganhe o Mundo(Idioma Inglês) - Nível Pré-Intermediário e Intermediário.
                            ''')
            button = st.button(":e-mail: Entre em Contato")
            


    retangulo_com_titulo = """
            <style>
                .retangulo {
                    background-color: #E0FFFF;
                    padding: 20px;
                    border-radius: 8px;
                    text-align: center;
                }
                .titulo {
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 20px;
                    color: #333;
                }
                .icones-container {
                    overflow-x: auto;
                    white-space: nowrap;
                    padding-bottom: 10px;
                }
                .icones-container::-webkit-scrollbar {
                    height: 8px; /* Altura da barra de rolagem */
                }
                .icones-container::-webkit-scrollbar-thumb {
                    background-color: #007BFF; /* Cor da barra de rolagem */
                    border-radius: 4px; /* Arredondamento da barra */
                }
                .icones-container::-webkit-scrollbar-track {
                    background-color: #333; /* Cor do trilho */
                    border-radius: 4px;
                }
                .icones {
                    display: inline-flex;
                    justify-content: flex-start;
                    align-items: center;
                    gap: 25px; /* Aumentando o espaçamento entre os ícones */
                }
                .icones img {
                    display: inline-block;
                    width: 65px;
                    height: 65px;
                }
                .ai-icon {
                    display: inline-block;
                    width: 500px; /* Largura aumentada */
                    height: 100px; /* Altura aumentada */
                    background-color: #007BFF; /* Fundo azul */
                    color: white; /* Cor do texto */
                    font-size: 30px; /* Tamanho da fonte */
                    font-weight: bold; /* Texto em negrito */
                    text-align: center; /* Texto centralizado */
                    line-height: 90px; /* Alinhamento vertical */
                    border-radius: 50%; /* Ícone circular */
                }
            </style>

            <div class="retangulo">
                <div class="titulo">Tecnologias</div>
                <div class="icones-container">
                    <div class="icones">
                        <div class="ai-icon">AI</div>
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-plain-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/plotly/plotly-original-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-plain-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original-wordmark.svg" />
                    </div>
                </div>
            </div>
        """
    st.markdown(retangulo_com_titulo, unsafe_allow_html=True)


    st.markdown("""
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
        """, unsafe_allow_html=True)

    st.markdown("""
            <link href="https://cdn.jsdelivr.net/npm/devicon@2.14.0/devicon.min.css" rel="stylesheet">
        """, unsafe_allow_html=True)


    if button:
        formulario()


def ler_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def build_page_me():
    perfil() 
    ler_css("style\\formulario.css")

build_page_me()