import streamlit as st
import time
import json

from livraria.backend.api.integracao_front import login_usuario

def pagina_login():
    st.title("🔐 Entrar")
    with st.form("form_login_page"):
        col1, col2 = st.columns(2)
        
        with col1:
            email = st.text_input("📧 Email", placeholder="seu@email.com", key="login_email")
        
        with col2:
            senha = st.text_input("🔑 Senha", type="password", placeholder="Sua senha", key="login_senha")
        
        col_login, col_cancel = st.columns(2)
        
        with col_login:
            enviar = st.form_submit_button("Entrar", use_container_width=True)
        
        with col_cancel:
            cancel = st.form_submit_button("❌ Cancelar", use_container_width=True)
        
        if cancel:
            st.session_state.pag_atual = "home"
            st.rerun()
        
        if enviar:
            if not email or not senha:
                st.error("❌ Por favor, preencha email e senha!")
                return
            
            dados_login = {
                'email': email,
                'senha': senha
            }
            
            try:
                resposta = login_usuario(dados_login)
                try:
                    resposta_json = json.loads(resposta)
                    
                    if resposta_json.get('status') == 'sucesso' and resposta_json.get('idUsuario'):
                        # Login bem-sucedido
                        st.session_state.logado = True
                        st.session_state.user_dado = {
                            'email': email,
                            'nome': resposta_json.get('nome', email.split('@')[0]),
                            'id': resposta_json.get('idUsuario'),
                            'token': resposta_json.get('token', '')
                        }
                        st.session_state.pag_atual = "catalogo"
                        st.success("✅ Login realizado com sucesso!")
                        time.sleep(1)
                        st.rerun()
                        return
                    else:
                        error_msg = resposta_json.get('erro', 'Email ou senha incorretos!')
                        st.error(f"❌ {error_msg}")
                        
                except json.JSONDecodeError:
                    if "sucesso" in resposta.lower() or "success" in resposta.lower():
                        st.session_state.logado = True
                        st.session_state.user_dado = {
                            'email': email,
                            'nome': email.split('@')[0],
                            'id': '1'
                        }
                        st.session_state.pag_atual = "catalogo"
                        st.success("✅ Login realizado com sucesso!")
                        time.sleep(1)
                        st.rerun()
                        return
                    else:
                        st.error(f"❌ Erro no login: {resposta}")
                        
            except Exception as e:
                st.error(f"❌ Erro ao conectar com o servidor: {str(e)}")