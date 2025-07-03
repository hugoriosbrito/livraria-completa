import streamlit as st
import pandas as pd
import time

from perfil import pagina_perfil
from catalogo import pagina_catalogo, exibir_card_livro, carregar_livros
from navegacao import render_navega
from sobre import pagina_sobre_nos
from login import pagina_login
from cadastro import pagina_cadastro

st.set_page_config(
    page_title="Livraria Pride 🏳️‍🌈",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

def css(arquivo):
    #carrega o conteúdo de um arquivo CSS e o injeta na aplicação.
    try:
        with open(arquivo, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Erro: O arquivo CSS '{arquivo}' não foi encontrado.")

#chama a função para carregar o CSS
css("style.css")

#inicialização do estado da sessão
def iniciar_sessao():
    if 'logado' not in st.session_state:
        st.session_state.logado = False
    if 'user_dado' not in st.session_state:
        st.session_state.user_dado = {}
    if 'pag_atual' not in st.session_state:
        st.session_state.pag_atual = "home"

iniciar_sessao()

def render_cab():
    st.markdown("""
    <div class="main-header">
        <h1>🏳️‍🌈 Livraria Pride 📚</h1>
        <p>Literatura LGBTQ+ para todos os públicos</p>
    </div>
    """, unsafe_allow_html=True)
    
    #header nome do usuário e função de sair
    with st.container():
        col1, col2 = st.columns([10, 5])
        
        if st.session_state.logado:
            with col2:
                st.success(f"👤 {st.session_state.user_dado.get('nome', 'Usuário')}")
                if st.button("🚪 Sair", use_container_width=True):
                    logout()

def logout():
    st.session_state.logado = False
    st.session_state.user_dado = {}
    st.session_state.pag_atual = "home"
    st.success("✅ Logout realizado com sucesso!")
    time.sleep(1)
    st.rerun()

def pagina_home():
    st.title("Bem-vindos à Livraria Pride! 🌈")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>📖</h2>
            <h3>Literatura Inclusiva</h3>
            <p>Catálogo especializado em literatura LGBTQ+ com diversidade de autores e histórias.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>🏳️‍🌈</h2>
            <h3>Representatividade</h3>
            <p>Promovemos vozes LGBTQ+ e criamos um espaço seguro para todos os leitores.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>⬇️</h2>
            <h3>Download</h3>
            <p>Download rápido e seguro de livros em formato pdf.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("📚 Livros em Destaque")
    
    livros = carregar_livros()
    
    for i in range(0, min(4, len(livros)), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            if i < len(livros):
                exibir_card_livro(livros[i], comp=True)
        
        with col2:
            if i + 1 < len(livros):
                exibir_card_livro(livros[i + 1], comp=True)
    
def main():
    render_cab()
    render_navega()
    
    page = st.session_state.pag_atual
    
    if page == "home":
        pagina_home()
    elif page == "catalogo":
        pagina_catalogo()
    elif page == "sobre_nos":
        pagina_sobre_nos()
    elif page == "perfil":
        pagina_perfil()
    elif page == "login":
        pagina_login()
    elif page == "cadastro":
        pagina_cadastro()
    
    #rodapé
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🏳️‍🌈 Livraria Pride")
        st.markdown("Literatura LGBTQ+ para todos")    
    with col2:
        st.markdown("### 📞 Contato")
        st.markdown("📧 contato@livrariaarcoiris.com")
        st.markdown("📱 (71) 99249-8333")      
    with col3:
        st.markdown("### 📊 Estatísticas")
        livros_backend = carregar_livros()
        total_livros = len(livros_backend) if livros_backend else 0
        st.markdown(f"📚 **{total_livros}** livros no catálogo")

if __name__ == "__main__":
    main()