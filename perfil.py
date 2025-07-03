import streamlit as st

def pagina_perfil():
    st.title("👤 Meu Perfil")
    
    if not st.session_state.logado:
        st.warning("🔐 Você precisa estar logado para ver seu perfil.")
        return
    
    user_dado = st.session_state.user_dado
    st.subheader("📋 Informações Pessoais")
    st.write(f"**👤 Nome:** {user_dado['nome']}")
    st.write(f"**📧 Email:** {user_dado['email']}")
    st.write(f"**🆔 ID:** {user_dado['id']}")