import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="EIAROB")
if 'pagina' not in st.session_state:
    st.session_state.pagina = "📊 Vista general"

st.markdown("""
    <style>
    
    .stApp {
        background: linear-gradient(90deg, #43b9e8 20%, #e938f2 80%) !important;
        margin-top:-4rem;
    }
    .stMainBlockContainer{
        padding-top: 4rem !important; 
        padding-bottom: 20rem !important;
    }   
    
    button[data-testid="stPopoverButton"]  {
        border: none;
        background: transparent;
        color: #1f80cf;
        padding: 0 !important; 
        margin-top: 0rem;height: auto !important;
        line-height: 1 !important;
    }
    .st-key-auto [data-testid="stColumn"]{
        background-color: rgba(154, 206, 227, 0.6) !important;
        border: 1px solid rgba(151, 192, 201, 0.2);
    }
    
    
    .st-key-auto{
        background-color:transparent;
        max-height: 40vh !important;
        overflow-y:hidden;
        
        min-width: 98vw !important;/* Casi todo el ancho de la pantalla */
        position: relative !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        
    }

    .st-key-header{
        background-color: rgba(174, 217, 235, 0.8) !important; 
        padding: 15px 20px !important;
        border-radius: 5px;
        border: 1px solid rgba(151, 192, 201, 0.2);
        margin-top: -1.4rem !important; 
        margin-bottom: -0.7rem !important;
        
        min-width: 100vw !important;
        position: relative !important; 
        left: 50%;
        transform: translateX(-50%) !important;
    }
    div[data-testid="stToolbar"]{
        background-color: transparent;         
    }
    
    </style>
""", unsafe_allow_html=True)


with st.container(key="header"):
    
    col_titulo,col_logo,col_usuario = st.columns([1,2,1], vertical_alignment="center")
    with col_logo: 
        st.markdown("<h1 style= 'text-align: center;margin-top:0px;padding-top:0;'>EIAROB</h1>", unsafe_allow_html=True)

    with col_titulo:
        with st.popover(f"{st.session_state.pagina}"):
            opciones = [
                "📊 Vista general", "⚙️ Configuración", "📡 Sensores", 
                "📈 Métricas", "📅 Calendario", "📥 Descargar app"
            ]
            seleccion = st.radio("Ir a:", opciones, label_visibility="collapsed")
            if seleccion != st.session_state.pagina:
                st.session_state.pagina = seleccion
                st.rerun()

    with col_usuario:
        st.markdown("<p style='text-align: right; margin-top: 0; opacity: 1; color: #1f80cf; '>👤 Usuario</p>", unsafe_allow_html=True)
        
st.divider() 

def vista_general():
    with st.container(key="auto"):
        col_buscador, col_mapa = st.columns(2,border=True)
        
        with col_buscador:
            st.markdown("<h3 style='text-align: center; color: black;'>Buscador de usuarios</h3>", unsafe_allow_html=True)
            st.selectbox("Select", ["Usuario 1", "Usuario 2"], label_visibility="collapsed", index=None, placeholder="Seleccione un usuario")
        
        with col_mapa:
            st.markdown("<h3 style='text-align: center; color: black;'>Mapa</h3>", unsafe_allow_html=True)
            # Mapa de ejemplo
            st.image("https://previews.123rf.com/images/meteoropata/meteoropata1702/meteoropata170200660/72499643-valladolid-map-spain-province-vector-map-high-detailed-vector-map-of-spain-with-separated-regions.jpg", 
                     width="content")
            
if st.session_state.pagina == "📊 Vista general":
    vista_general()
