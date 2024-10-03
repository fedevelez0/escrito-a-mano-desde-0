import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Streamlit layout
st.set_page_config(page_title='Tablero para Dibujo', layout='wide')
st.title('✨ Tablero para Dibujo ✨')

# Sidebar settings
st.sidebar.title("🎨 Propiedades del Tablero")
drawing_mode = st.sidebar.selectbox("Herramienta de Dibujo", ["freedraw", "line", "rect", "circle", "polygon"])
stroke_width = st.sidebar.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = st.sidebar.color_picker('Color de trazo', '#FF6347')  # Color vibrante (Tomato)
bg_color = '#1E1E1E'       # Fondo oscuro

# Set fill_color based on drawing_mode
if drawing_mode in ["rect", "circle", "polygon"]:
    fill_color = "rgba(0, 0, 0, 0)"  # Sin relleno
else:
    fill_color = "rgba(0, 204, 204, 0.3)"  # Color de relleno en un tono aqua

# Create canvas
canvas_result = st_canvas(
    fill_color=fill_color,  # Color de relleno según el modo
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=450,  # Tamaño del canvas
    width=450,
    drawing_mode=drawing_mode,  # Establecer el modo de dibujo seleccionado
    key="canvas",
)


