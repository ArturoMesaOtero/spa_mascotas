import streamlit as st


def video_player(video_path):
    st.markdown("""
        <style>
        .stVideo {
            width: 100%;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    st.video(video_path)