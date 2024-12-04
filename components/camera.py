import streamlit as st
from PIL import Image


def camera_component():
    st.markdown("""
        <style>
        .stCamera > button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
        }
        .stCamera > button:hover {
            background-color: #FF3333;
        }
        </style>
    """, unsafe_allow_html=True)

    img_file_buffer = st.camera_input("Toma una foto", key="camera")
    if img_file_buffer is not None:
        img = Image.open(img_file_buffer)
        return img
    return None