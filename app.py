import streamlit as st
from components.camera import camera_component
from components.video_player import video_player
from components.form import show_form_popup
from utils.image_processor import ImageProcessor

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Imágenes",
    page_icon="📸",
    layout="wide"
)

# Estilos globales
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .analysis-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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

# Inicializar el procesador de imágenes
if 'image_processor' not in st.session_state:
    st.session_state.image_processor = ImageProcessor()

# Título con estilo
st.markdown("""
    <h1 style='text-align: center; color: #FF4B4B; margin-bottom: 2rem;'>
        📸 Análisis de Imágenes con IA
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

        # Análisis de la imagen con OpenAI
        with st.spinner('Analizando la imagen con IA...'):
            analysis = st.session_state.image_processor.analyze_image(image)

            if analysis:
                st.markdown("### 🤖 Análisis de la IA")
                st.markdown(f"""
                    <div class="analysis-container">
                        {analysis}
                    </div>
                """, unsafe_allow_html=True)

                # Reproducción de video basado en la raza
                st.markdown("### 🎥 Video Informativo")
                video_player(analysis)  # Pasamos el diccionario completo

                # Botón para mostrar el formulario
                if st.button("📝 Guardar Análisis", key="form_button"):
                    show_form_popup()

# Manejo de estado para el formulario
if 'form_submitted' in st.session_state and st.session_state.form_submitted:
    st.success("✅ Análisis guardado exitosamente!")
    # Reiniciar el estado
    st.session_state.form_submitted = False
