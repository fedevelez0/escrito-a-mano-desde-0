import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_drawable_canvas import st_canvas
# App
def predictDigit(image):
    model = tf.keras.models.load_model("model/handwritten.h5")
    image = ImageOps.grayscale(image)
    img = image.resize((28,28))
    img = np.array(img, dtype='float32')
    img = img/255
    plt.imshow(img)
    plt.show()
    img = img.reshape((1,28,28,1))
    pred= model.predict(img)
    result = np.argmax(pred[0])
    return result

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

# Add buttons for saving and clearing
col1, col2 = st.columns(2)
with col1:
    if st.button('Guardar'):
        st.write("Imagen guardada.")
with col2:
    if st.button('Borrar'):
        st.session_state.canvas_data = None
        st.experimental_rerun()
