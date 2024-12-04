import streamlit as st
from components.camera import camera_component
from components.video_player import video_player
from components.form import show_form_popup

# Configuración de la página
st.set_page_config(
    page_title="Mi Aplicación",
    page_icon="📸",
    layout="wide"
)

# Estilos globales
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Título con estilo
st.markdown("""
    <h1 style='text-align: center; color: #FF4B4B; margin-bottom: 2rem;'>
        📸 Mi Aplicación de Captura
    </h1>
""", unsafe_allow_html=True)

# Contenedor principal
with st.container():
    # Sección de la cámara
    col1, col2 = st.columns([2, 1])
    with col1:
        image = camera_component()

    if image is not None:
        with col2:
            st.image(image, caption="Foto capturada", use_column_width=True)

        # Reproducción de video
        st.markdown("### 🎥 Video Relacionado")
        video_player("./videos/Afgano.mp4")

        # Botón para mostrar el formulario
        if st.button("📝 Abrir Formulario", key="form_button"):
            show_form_popup()