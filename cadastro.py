import streamlit as st
import time
import json
from livraria.backend.api.integracao_front import cadastrar_usuario
from livraria.backend.validacao.validacao import Validacao, ValidacaoException

def pagina_cadastro():
    st.title("📝 Cadastre-se")

    with st.form("form_cadastro_page"):
        st.subheader("Dados Pessoais")
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("👤 Nome completo*", placeholder="Digite seu nome", key="cadastro_nome")
            email = st.text_input("📧 Email*", placeholder="seu@email.com", key="cadastro_email")
        
        with col2:
            senha = st.text_input("🔑 Senha*", type="password", placeholder="Mínimo 8 caracteres + caracter especial", key="cadastro_senha")
            confirmar_senha = st.text_input("🔑 Confirmar senha*", type="password", key="cadastro_confirmar_senha")
        
        col_enviar, col_cancel = st.columns(2)
        
        with col_enviar:
            enviar = st.form_submit_button("Cadastrar", use_container_width=True)
        
        with col_cancel:
            cancel = st.form_submit_button("❌ Cancelar", use_container_width=True)
        
        if cancel:
            st.session_state.pag_atual = "home"
            st.rerun()
        
        if enviar:
            if not all([nome, email, senha, confirmar_senha]):
                st.error("❌ Por favor, preencha todos os campos obrigatórios!")
                return
            
            if senha != confirmar_senha:
                st.error("❌ As senhas não coincidem!")
                return
            
            dados_usuario = {
                'nome': nome,
                'email': email,
                'senha': senha
            }
            
            try:
                resposta = cadastrar_usuario(dados_usuario)
                
                try:
                    resposta_json = json.loads(resposta)
                    if resposta_json.get('usuario') and resposta_json['usuario'].get('id'):
                        st.session_state.pag_atual = "login" 
                        st.success("✅ Cadastro realizado com sucesso! Você já pode fazer login.")
                        time.sleep(2) 
                        st.rerun()
                    else:
                        error_msg = resposta_json.get('erro', 'Erro desconhecido no cadastro')
                        st.error(f"❌ {error_msg}")
                except json.JSONDecodeError:
                    if "usuario" in resposta and "id" in resposta:
                        st.session_state.pag_atual = "login" 
                        st.success("✅ Cadastro realizado com sucesso! Você já pode fazer login.")
                        time.sleep(2) 
                        st.rerun()
                    else:
                        st.error(f"❌ Erro no cadastro: {resposta}")
                        
            except ValidacaoException as e:
                st.error(f"❌ {str(e)}")
            except Exception as e:
                st.error(f"❌ Erro ao cadastrar: {str(e)}")