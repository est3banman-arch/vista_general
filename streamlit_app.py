import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="EIAROB")
if 'pagina' not in st.session_state:
    st.session_state.pagina = "📊 Vista general"

st.markdown("""
    <style>
    
    .stApp {
        background: linear-gradient(145deg, #1e3a8a 0%, #581c87 100%) !important;
    }
    .stMainBlockContainer{
        padding-top: 4rem !important; 
    }   
    
    button[data-testid="stPopoverButton"]  {
        border: none;
        background: transparent;
        font-size: 1.2rem;
        font-weight: bold;
        color: #ffffff;
        padding: 0 !important; 
        margin-top: 0rem;height: auto !important;
        line-height: 1 !important;
    }
    
    .st-key-auto [data-testid="stColumn"]{
        background-color: rgba(114, 174, 214, 0.4) !important;
    }
    .st-key-auto{
        background-color:transparent;
        max-height: 50vh;
        overflow-y:auto;
    }

    .st-key-header{
        background-color: rgba(255, 255, 255, 0.05) !important; /* Fondo sutil */
        backdrop-filter: blur(12px); /* Efecto cristal */
        padding: 10px 20px !important;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        width: 100vw;
    }
    
    
    </style>
""", unsafe_allow_html=True)


with st.container(key="header"):
    
    col_titulo,col_logo,col_usuario = st.columns([1,2,1], vertical_alignment="center")
    with col_logo: 
        st.markdown("<h1 style= 'text-align: center;'>EIAROB</h1>", unsafe_allow_html=True)



    with col_titulo:
        with st.popover(f"☰ {st.session_state.pagina}"):
            opciones = [
                "📊 Vista general", "⚙️ Configuración", "📡 Sensores", 
                "📈 Métricas", "📅 Calendario", "📥 Descargar app"
            ]
            seleccion = st.radio("Ir a:", opciones, label_visibility="collapsed")
            if seleccion != st.session_state.pagina:
                st.session_state.pagina = seleccion
                st.rerun()
            


    with col_usuario:
        st.markdown("<p style='text-align: right; margin: 0; opacity: 1; '>👤 Usuario</p>", unsafe_allow_html=True)
        
st.divider() 



def vista_general():
    with st.container(key="auto"):
        col_buscador, col_mapa = st.columns(2,border=True)
        
        with col_buscador:
            st.markdown("<h3 style='text-align: center; color: white;'>Buscador de usuarios</h3>", unsafe_allow_html=True)
            st.selectbox("Select", ["Usuario 1", "Usuario 2"], label_visibility="collapsed", index=None, placeholder="Seleccione un usuario")
        
        with col_mapa:
            st.markdown("<h3 style='text-align: center; color: white;'>Mapa</h3>", unsafe_allow_html=True)
            # Mapa de ejemplo
            st.image("https://previews.123rf.com/images/meteoropata/meteoropata1702/meteoropata170200660/72499643-valladolid-map-spain-province-vector-map-high-detailed-vector-map-of-spain-with-separated-regions.jpg", 
                     width="stretch")
            



if st.session_state.pagina == "📊 Vista general":
    vista_general()
