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
    page_title='Customer & Behavior',
    page_icon=':blue[👥]',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS for padding
st.markdown('<style>div.block-container{padding-top:2vh;}</style>', unsafe_allow_html=True)

# Page title
st.title('👥 :blue[Customer & Behavior Analysis]')
st.markdown(" ")


total1, total2, = st.columns([3,3], gap='large')

with total1:
    with st.container(border=True,height=600):
        st.write("🏆 Top 5 Customers by Total Purchases")
        st.plotly_chart(get_top_purchase(), use_container_width=True)

with total2:
    with st.container(border=True, height=600):
        st.write("📦 Top 10 Customers by Number of Orders")
        st.plotly_chart(get_orders_per_customer(), use_container_width=True)

with st.container(border=True, height=600):
        st.write("🌍 Number of Customers per Sales Territory")
        st.plotly_chart(get_territory_per_customer(), use_container_width=True)   
