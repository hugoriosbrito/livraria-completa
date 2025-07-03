import streamlit as st
import json
from livraria.backend.api.integracao_front import listar_livros
from livraria.backend.api.integracao_front import realizar_download_livro

def carregar_livros():
    try:
        resposta = listar_livros()
        livros_json = json.loads(resposta)
        
        livros_adaptados = []
        for livro in livros_json:
            livro_adaptado = {
                'idLivro': livro.get('idLivro'),
                'titulo': livro.get('titulo', 'Título não disponível'),
                'autor': livro.get('nomeAutor','Autor não informado'),  # autor não aparece
                'descricao': livro.get('descricao', 'Descrição não disponível'),
                'categoria': livro.get('categoria','Categoria não disponível'),  # categoria não aparece
                'imagem': livro.get('urlImagem', ''),
                'linkLivro': livro.get('linkLivro', ''),
                'paginas': livro.get('paginas', 0)
            }
            livros_adaptados.append(livro_adaptado)
        
        return livros_adaptados
    except Exception as e:
        st.error(f"❌ Erro ao carregar livros do backend: {str(e)}")
        return []

def exibir_card_livro(livro, comp=False):
    if comp:
        #card compactado
        st.markdown(f"""
        <div class="livro-card-comp">
            <img src="{livro['imagem']}" class="livro-imagem-comp" alt="{livro['titulo']}">
            <div class="livro-titulo">{livro['titulo']}</div>
            <div class="livro-autor">{livro['autor']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        col_detalhes, col_download = st.columns(2)

        with col_detalhes:
            with st.popover(f"📚 Detalhes", use_container_width=True):
                st.subheader(f"Detalhes de {livro['titulo']}")
                st.image(livro['imagem'], caption=livro['titulo'], width=150)
                st.markdown(f"**Autor:** {livro['autor']}")
                st.markdown(f"**Categoria:** {livro['categoria']}")
                st.markdown(f"**Descrição:** {livro['descricao']}")                
                if livro.get('paginas'):
                    st.markdown(f"**📄 Páginas:** {livro['paginas']}")

        with col_download:
            if st.session_state.logado:
                try:
                    resposta_download = realizar_download_livro(livro.get('idLivro'), st.session_state.user_dado['id'])
                    if resposta_download:
                        dados_download = json.loads(resposta_download)
                        link_download = dados_download.get('linkDownload')
                        print(link_download)
                        
                        if link_download:
                            st.link_button("⬇️ Baixar PDF", link_download, use_container_width=True)
                        else:
                            st.warning("Link de download não encontrado.")
                    else:
                        st.warning("Erro ao obter download do livro.")
                except json.JSONDecodeError:
                    st.error("Erro ao processar resposta do servidor.")
                except Exception as e:
                    st.error(f"Erro inesperado: {str(e)}")
            else:
                st.info("Faça login para baixar")
    else:
        #card completo
        st.markdown(f"""
        <div class="livro-card-cheio">
            <img src="{livro['imagem']}" class="livro-imagem" alt="{livro['titulo']}">
            <div class="livro-info">
                <h4>📖 {livro['titulo']}</h4>
                <p><strong>✍️ Autor:</strong> {livro['autor']}</p>
                <p><strong>📂 Categoria:</strong> {livro['categoria']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col_detalhes, col_download = st.columns(2)

        with col_detalhes:
            with st.popover(f"📚 Detalhes", use_container_width=True):
                st.subheader(f"Detalhes de {livro['titulo']}")
                st.image(livro['imagem'], caption=livro['titulo'], width=150)
                st.markdown(f"**Autor:** {livro['autor']}")
                st.markdown(f"**Categoria:** {livro['categoria']}")
                st.markdown(f"**Descrição:** {livro['descricao']}")
                if livro.get('paginas'):
                    st.markdown(f"**📄 Páginas:** {livro['paginas']}")

        with col_download:
             if st.session_state.logado:
                try:
                    resposta_download = realizar_download_livro(livro.get('idLivro'), st.session_state.user_dado['id'])
                    if resposta_download:
                        dados_download = json.loads(resposta_download)
                        link_download = dados_download.get('linkDownload')
                        print(link_download)
                        
                        if link_download:
                            st.link_button("⬇️ Baixar PDF", link_download, use_container_width=True)
                        else:
                            st.warning("Link de download não encontrado.")
                    else:
                        st.warning("Erro ao obter download do livro.")
                except json.JSONDecodeError:
                    st.error("Erro ao processar resposta do servidor.")
                except Exception as e:
                    st.error(f"Erro inesperado: {str(e)}")
             else:
                st.info("Faça login para baixar")
        
        st.markdown("---")

def pagina_catalogo():
    st.title("📚 Catálogo Completo")
    
    #carrega os livros do backend
    livros = carregar_livros()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        busca = st.text_input("🔍 Buscar livros", placeholder="Digite o título ou autor...")
    
    with col2:
        categoria_filtro = st.selectbox("🏷️ Categoria", ["Todas"] + list(set([livro["categoria"] for livro in livros])))
    
    livros_filtrados = livros.copy()

    if busca:
        livros_filtrados = [
            livro for livro in livros_filtrados
            if busca.lower() in livro['titulo'].lower() or busca.lower() in livro['autor'].lower()
        ]
    
    if categoria_filtro != "Todas":
        livros_filtrados = [livro for livro in livros_filtrados if livro['categoria'] == categoria_filtro]
    
        num_livros = len(livros_filtrados)
        palavra = "livro" if num_livros == 1 else "livros"

        st.info(f"📊 Encontrados {num_livros} {palavra}")    

    for livro in livros_filtrados:
        exibir_card_livro(livro, comp=False)