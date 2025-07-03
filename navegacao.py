import streamlit as st
from catalogo import carregar_livros

def render_navega():
    with st.sidebar:
        st.title("Navegação")
        
        if st.session_state.logado:
            st.success(f"Logado como: {st.session_state.user_dado.get('nome', 'Usuário')}")
        
        menu_opcoes = [
            ("🏠", "Home", "home"),
            ("📚", "Catálogo", "catalogo"),
            ("ℹ️", "Sobre Nós", "sobre_nos")
        ]
        
        if st.session_state.logado:
            menu_opcoes.extend([
                ("👤", "Perfil", "perfil")
            ])
        else:
            menu_opcoes.extend([
                ("🔐", "Login", "login"),
                ("📝", "Cadastro", "cadastro")
            ])
        
        for icon, label, pag_key in menu_opcoes:
            if st.button(f"{icon} {label}", key=f"nav_{pag_key}", use_container_width=True):
                st.session_state.pag_atual = pag_key
                st.rerun()
        
        st.markdown("---")
        st.subheader("📊 Sistema")
        livros_backend = carregar_livros()
        total_livros = len(livros_backend) if livros_backend else 0
        st.metric("📚 Livros", total_livros)
