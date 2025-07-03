import streamlit as st

def pagina_sobre_nos():
    cor_principal = "#CE035F"

    st.markdown(f"<h1 class='titulo-pagina' style='color: {cor_principal};'>Sobre Nós</h1>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='bloco-conteudo'>
        <div class='cabecalho-bloco'>
            <img src='https://img.icons8.com/ios-filled/32/{cor_principal.replace('#','')}/book.png' style='margin-right: 12px;'>
            <h2 class='titulo-bloco' style='color: {cor_principal};'>Iniciativa Livraria Pride</h2>
        </div>
        <p class='paragrafo-conteudo'>A “Livraria Pride” é um aplicativo web que visa suprir a carência de espaços digitais que valorizem as vozes LGBTQIAPN+, a medida que promove um espaço acolhedor, simples e funcional para todos.</p>
        <p class='paragrafo-conteudo'>Nós acreditamos que os livro tem o poder de transformar vidas, quebrar preconceitos e construir pontes de compreensão. Nossa biblioteca online reúne obras de autores LGBTQIAPN+ e suas histórias que celebram a diversidade em todas as suas formas.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='bloco-conteudo'>
        <div class='cabecalho-bloco'>
            <img src='https://img.icons8.com/ios-filled/40/FFE551/exclamation-mark.png' style='margin-right: 12px;'>
            <h2 class='titulo-bloco' style='color: #FFE551;'>Nossa Missão</h2>
        </div>
        <img src='https://images.unsplash.com/photo-1462899006636-339e08d1844e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0NTYyMDF8MHwxfHNlYXJjaHw2fHxtaXNzaW9ufGVufDB8fHx8MTc0OTc3MTgzNXww&ixlib=rb-4.1.0&q=80&w=1080' class='imagem-bloco'>
        <p class='paragrafo-conteudo' font-weight: 500;'>Promover a diversidade e inclusão através da literatura, oferecendo um catálogo especializado em obras LGBTQIA+ que inspirem, eduquem e empoderem nossa comunidade e aliados.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='bloco-conteudo'>
        <div class='cabecalho-bloco'>
            <img src='https://img.icons8.com/ios-filled/32/0585FB/visible.png' style='margin-right: 12px;'>
            <h2 class='titulo-bloco' style='color: #0091FF;'>Nossa Visão</h2>
        </div>
        <img src='https://images.unsplash.com/photo-1545935950-b7a28791ad7a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0NTYyMDF8MHwxfHNlYXJjaHwxfHx2aXNpb258ZW58MHx8fHwxNzQ5NzcxOTI5fDA&ixlib=rb-4.1.0&q=80&w=1080' class='imagem-bloco'>
        <p class='paragrafo-conteudo' font-weight: 500;'>Ser reconhecida como a principal referência em literatura LGBTQIA+ no país, criando um movimento de transformação social através da leitura e construindo um futuro mais inclusivo para todas as pessoas.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='bloco-conteudo'>
        <div class='cabecalho-bloco'>
            <img src='https://img.icons8.com/ios-filled/32/F4080B/handshake.png' style='margin-right: 12px;'>
            <h2 class='titulo-bloco' style='color: #E90D10;'>Nossos Valores</h2>
        </div>
        <img src='https://images.unsplash.com/photo-1505455184862-554165e5f6ba?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0NTYyMDF8MHwxfHNlYXJjaHw2fHx2YWx1ZXN8ZW58MHx8fHwxNzQ5NzcxOTk1fDA&ixlib=rb-4.1.0&q=80&w=1080' class='imagem-bloco'>
        <ul class='lista-valores'>
            <li class='item-valor'><img src='https://img.icons8.com/ios-filled/20/F60228/star--v1.png' class='icone-item-valor'>Respeito e acolhimento a todas as identidades</li>
            <li class='item-valor'><img src='https://img.icons8.com/ios-filled/20/F60228/star--v1.png' class='icone-item-valor'>Compromisso com a representatividade autêntica</li>
            <li class='item-valor'><img src='https://img.icons8.com/ios-filled/20/F60228/star--v1.png' class='icone-item-valor'>Educação e conscientização através da literatura</li>
            <li class='item-valor'><img src='https://img.icons8.com/ios-filled/20/F60228/star--v1.png' class='icone-item-valor'>Construção de uma comunidade forte e unida</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)