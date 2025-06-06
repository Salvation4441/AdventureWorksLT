# Importing the necessary packages
import pandas as pd  
import numpy as np  
import plotly.express as px  
import plotly.graph_objects as go
import streamlit as st
from helper import *  # Importing the function to get total sales

import warnings
warnings.filterwarnings('ignore')

# Display options for pandas
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

# Streamlit page configuration
st.set_page_config(
    page_title='Production Analysis',
    page_icon='🏭',
    layout='wide',
    initial_sidebar_state='expanded'
)
# Custom CSS for padding
st.markdown('<style>div.block-container{padding-top:2vh;}</style>', unsafe_allow_html=True)

# Page title
st.title('🏭 :blue[Production Analysis]')
st.markdown(" ")

with st.container(border=True):
        st.write("📈 Top 10 Products by Average Unit Price")
        st.plotly_chart(get_highest_avg_price_chart(), use_container_width=True)
