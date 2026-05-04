import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="EIAROB")

st.markdown("""
    <style>
        
            .stMainBlockContainer{
                padding-top: 1.5rem !important; /* Un poco más de espacio para que no se corte */
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
            header[data-testid="stHeader"] {
        background: transparent;
        height: 0px;
            }
            /* 3. Estilo del título sin márgenes negativos peligrosos */
    .titulo-pagina {
        padding-top: 2.5rem !important;
        font-size:  1.5rem;
        font-weight: 500;
        color: #FFFFFF;
        line-height: 1.2; /* Asegura que el emoji y el texto tengan espacio vertical */
        margin: 0; 
        padding-top: 5px; /* Ajuste fino hacia abajo si queda muy pegado al borde */
    }
    
    /* 4. Estilo para el logo central */
    .logo-central {
        text-align: center;
        margin: 0;
        line-height: 1;
    }       
    </style>
""", unsafe_allow_html=True)

col_titulo,col_logo,col_usuario = st.columns([1,2,1])

with col_logo: 
    st.markdown("<h1 style= 'text-align: center;'>EIAROB</h1>", unsafe_allow_html=True)


with st.sidebar:
    seleccion = st.radio(
        "Selecciona Vista: ",
        [
            "📊 Vista general", 
            "⚙️ Configuración", 
            "📡 Sensores", 
            "📈 Métricas", 
            "📅 Calendario de eventos", 
            "📥 Descargar app"          
        ] 
    )

with col_titulo:
    st.markdown(f"""<div class="titulo-pagina">{seleccion}</div>""",unsafe_allow_html=True)


with col_usuario:
    st.markdown("<p style='text-align: right; margin: 0; opacity: 1; margin-top:2.5rem'>👤 Usuario</p>", unsafe_allow_html=True)
    
st.divider()

st.write("Contenido de preuba")
