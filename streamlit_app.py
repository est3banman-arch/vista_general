import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="SOROCARE")
if 'pagina' not in st.session_state:
    st.session_state.pagina = "📊 Vista general"
### CSS 
st.markdown("""
    <style>
    /*----HEADER ----*/
    .stApp {
        background: linear-gradient(145deg, #43b9e8 0%, #c8d9e0 90%) !important;
        margin-top: -4rem;
    }
    .stMainBlockContainer{
        padding-top: 4rem !important; 
        padding-bottom: 20rem !important;
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
    
    /*---------BOTON VIVIENDA --------*/ 
    button[data-testid="stPopoverButton"]  {
        border: none;
        background: transparent;
        color: #1f80cf;
        padding: 0 !important; 
        margin-top: 0rem;
        line-height: 1 !important;
    }
    .st-key-popover [data-testid="stPopover"] button p {
        font-size: 23px; 
    }
    [data-testid="stRadio"] label {
        display: flex !important;
        align-items: center !important; /* El secreto del centro perfecto */
        margin-bottom: 5px !important; /* Espacio entre opciones */
    }
            
    /*----------MAPA--------*/
    .st-key-auto{
        background-color: transparent;
        max-height: 40vh !important;
        overflow-y:hidden;
        
        min-width: 98vw !important;/* Casi todo el ancho de la pantalla */
        position: relative !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
    }
            
    /*---------COLUMNAS ------*/
    .st-key-auto [data-testid="stColumn"]{
        background-color: rgba(154, 206, 227, 0.6) !important;
        border: 1px solid rgba(151, 192, 201, 0.2);
    }
      
            
    /* -------TABS DESIGN--------*/ 
    button[data-testid="stTab"] p {
        color: black !important;         
    }        
    button[data-testid="stTab"][aria-selected="true"] p {
        font-weight: bold !important;
        margin-right:3px;
        margin-left: 3px;
    }
    div[data-baseweb="tab-highlight"] {
        background-color: black !important;
    }
    [data-testid="stMarkdownContainer"] > p {
        font-size: 23px;   
    }
    
    </style>
""", unsafe_allow_html=True)

## --- FUNCIONES DE CADA SECCION ---

def vista_datos():
    with st.container(key="auto"):
            col_datos, col_mapa = st.columns(2,border=True)
            
            with col_datos:
                st.markdown("<h3 style='text-align: center; color: black;'>Datos Usuario: </h3>", unsafe_allow_html=True)
                st.write("Nombre: ")
                st.write("Apellidos: ")
                st.write("Dirección: ")
                st.write("Población: ")
            with col_mapa:
                st.markdown("<h3 style='text-align: center; color: black;'>Mapa</h3>", unsafe_allow_html=True)
                # Mapa de ejemplo
                st.image("https://previews.123rf.com/images/meteoropata/meteoropata1702/meteoropata170200660/72499643-valladolid-map-spain-province-vector-map-high-detailed-vector-map-of-spain-with-separated-regions.jpg", 
                        width="content") 

def vista_mapa():
        st.subheader("Mapa con posible iframe")
        

def vista_actividad():
    st.subheader("Registro de Actividades", text_alignment="center")

## HEADER ##
with st.container(key="header"):
    
    username = "Usuario 1" ##se sacaran del token 
    rol = "Gestor" ##se sacaran del token 

    col_vivienda,col_logo,col_usuario = st.columns([1,2,1], vertical_alignment="center")
    with col_logo: 
        st.markdown("<h1 style= 'text-align: center;margin-top:0px;padding-top:0;'>SOROCARE</h1>", unsafe_allow_html=True)

    with col_vivienda:
        with st.popover(f"{st.session_state.pagina}", on_change="rerun", key="popover"):
            opciones = [
                "Vivienda 1", "Vivienda 2", "Vivienda 3", 
                "Vivienda 4", "Vivienda 5", "Vivienda 6"
            ]
            seleccion = st.radio("Ir a:", opciones, label_visibility="collapsed")
            if seleccion != st.session_state.pagina:
                st.session_state.pagina = seleccion
                st.rerun()

    with col_usuario:
        st.markdown(f"<p style='text-align: right; font-size: 18px; margin-top:3px; opacity: 1; color: #1f80cf; '>👤 {username}</p>", unsafe_allow_html=True)
        st.markdown(f"""<p style="margin-top: -10px; font-size: 18px; margin-bottom: 10px; color: #1f80cf; ">Perfil: {rol} </p>""", unsafe_allow_html=True,text_alignment="right")

st.space()

## TABS ## 

tab_datos, tab_mapa, tab_actividad = st.tabs(["Datos Vivienda", "Mapa", "Actividad"])

with tab_datos: 
    vista_datos()
    
with tab_mapa: 
    vista_mapa()

with tab_actividad: 
    vista_actividad()

         
