import streamlit as st
import streamlit.components.v1 as components
import os

# Configuração da página
st.set_page_config(
    page_title="Julgamento e Tomada de Decisão em Contabilidade",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para melhorar a aparência
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    
    .stSelectbox > div > div > select {
        background-color: #ffffff;
        border: 2px solid #667eea;
        border-radius: 5px;
    }
    
    .aula-info {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
    }
    
    .iframe-container {
        border: 2px solid #e1e5e9;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("""
<div class="main-header">
    <h1>📊 Julgamento e Tomada de Decisão em Contabilidade</h1>
    </div>
""", unsafe_allow_html=True)

# Dicionário com informações das aulas
aulas_info = {
    "Aula1_nova.html": {
        "titulo": "Bloco 1 - Fundamentos e Ruído",
        "descricao": "Introdução à Hipótese do Mercado Eficiente (EMH), críticas empíricas, Behavioral Finance e aplicações contábeis.",
        "topicos": [
            "EMH e modelo clássico",
            "Críticas e anomalias",
            "Noise traders e limites à arbitragem",
            "Aplicações em impairment e provisões"
        ]
    },
    "Aula2_nova.html": {
        "titulo": "Bloco 2 - Anomalias e Prospect Theory",
        "descricao": "Aprofundamento em vieses cognitivos, Prospect Theory e implicações para julgamentos contábeis.",
        "topicos": [
            "Prospect Theory e aversão à perda",
            "Vieses: ancoragem, framing, sunk cost",
            "Disposition effect e representatividade",
            "Aplicações práticas em contabilidade"
        ]
    },
    "Aula3_nova.html": {
        "titulo": "Bloco 3 - Séries Temporais e Efeitos de Mercado",
        "descricao": "Análise de padrões temporais, momentum, reversão à média e efeitos de calendário.",
        "topicos": [
            "Previsibilidade vs. random walk",
            "Mean reversion e momentum",
            "Efeitos de calendário",
            "Aplicações em valuation e auditoria"
        ]
    },
    "Aula4_nova.html": {
        "titulo": "Bloco 4 - Integração e Neuroeconomia",
        "descricao": "Integração dos conceitos, neuroeconomia, economia experimental e casos práticos.",
        "topicos": [
            "Equity Premium Puzzle",
            "Neuroeconomia e estruturas cerebrais",
            "Economia experimental",
            "Integração prática e governança"
        ]
    },
    "AppBF.html": {
        "titulo": "Aplicativo Interativo - Exercícios Práticos",
        "descricao": "Aplicação interativa com exercícios, simulações e estudos de caso para cada bloco do curso.",
        "topicos": [
            "Simulação de mercado",
            "Estudos de caso da crise de 2008",
            "Exercícios de vieses cognitivos",
            "Análise de decisões em grupo"
        ]
    }
}

# Sidebar para navegação
st.sidebar.title("📚 Navegação do Curso")
st.sidebar.markdown("---")

# Seleção da aula
aula_selecionada = st.sidebar.selectbox(
    "Selecione uma aula:",
    options=list(aulas_info.keys()),
    format_func=lambda x: aulas_info[x]["titulo"],
    index=0
)

# Informações da aula selecionada na sidebar
if aula_selecionada:
    info_aula = aulas_info[aula_selecionada]
    
    st.sidebar.markdown("### 📖 Sobre esta aula")
    st.sidebar.markdown(f"**{info_aula['titulo']}**")
    st.sidebar.markdown(info_aula['descricao'])
    
    st.sidebar.markdown("### 📋 Tópicos abordados:")
    for topico in info_aula['topicos']:
        st.sidebar.markdown(f"• {topico}")

st.sidebar.markdown("---")
st.sidebar.markdown("**Professor:** Dr. César Valentim")
st.sidebar.markdown("**Curso:** Julgamento e Tomada de Decisão em Contabilidade")

# Área principal - exibição da aula
if aula_selecionada:
    info_aula = aulas_info[aula_selecionada]
    
    # Informações da aula atual
    st.markdown(f"""
    <div class="aula-info">
        <h2>{info_aula['titulo']}</h2>
        <p><strong>Descrição:</strong> {info_aula['descricao']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Verificar se o arquivo existe
    caminho_arquivo = os.path.join(os.getcwd(), aula_selecionada)
    
    if os.path.exists(caminho_arquivo):
        # Ler o conteúdo do arquivo HTML
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Exibir o HTML em um iframe
        st.markdown('<div class="iframe-container">', unsafe_allow_html=True)
        components.html(html_content, height=800, scrolling=True)
        st.markdown('</div>', unsafe_allow_html=True)

  # 🔽 Botão só para o Bloco 2
    if aula_selecionada == "Aula2_nova.html":
        st.markdown("### 📷 Recurso extra")
        if st.button("Mostrar imagem complementar"):
            st.image(
                "https://www.economicsonline.co.uk/content/images/size/w1000/2024/02/3-2.webp",
                caption="Exemplo visual complementar - Prospect Theory",
                use_container_width=True
        )
        
        # Instruções de uso
        st.markdown("---")
        st.markdown("""
        ### 💡 Como usar:
        - Use os controles de navegação dentro da apresentação para avançar/retroceder slides
        - Para aulas interativas (AppBF.html), preencha os exercícios diretamente na interface
        - Use a barra lateral para alternar entre diferentes aulas
        - Todas as funcionalidades originais dos arquivos HTML são preservadas
        """)
        
    else:
        st.error(f"Arquivo {aula_selecionada} não encontrado!")
        st.info("Verifique se todos os arquivos HTML estão no diretório correto.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>📊 Curso de Julgamento e Tomada de Decisão em Contabilidade</p>
    <p>Desenvolvido com Streamlit | Prof. Dr. César Valentim</p>
</div>
""", unsafe_allow_html=True)
