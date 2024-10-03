import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Streamlit layout
st.set_page_config(page_title='Tablero para dibujo', layout='wide')
st.title('Tablero para dibujo')

# Sidebar settings
st.sidebar.title("Propiedades del Tablero")
drawing_mode = st.sidebar.selectbox("Herramienta de Dibujo", ["freedraw"])
stroke_width = st.sidebar.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = '#FFFFFF' 
bg_color = '#000000'

# Create canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)", 
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=200,
    width=200,
    key="canvas",
)


