import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib as plt
import seaborn as sns
import shap
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from streamlit_shap import st_shap

# Set page configuration
st.set_page_config(
    page_title="Breast Cancer Survival Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #e63946;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #1d3557;
        margin-bottom: 0.5rem;
    }
    .info-text {
        background-color: #f1faee;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border: 1px solid #a8dadc;
        color: #1d3557;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #28a745;
        color: #155724;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #ffc107;
        color: #856404;
    }
    .stButton>button {
        background-color: #457b9d;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1d3557;
    }
    /* Improve general text visibility */
    p, h1, h2, h3, label {
        color: #1d3557;
    }
    /* Improve form field visibility */
    .stNumberInput, .stSelectbox {
        background-color: #f1faee !important;
    }
</style>
""", unsafe_allow_html=True)
