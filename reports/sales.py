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
    page_title='Sales & Revenue',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS for padding
st.markdown('<style>div.block-container{padding-top:2vh;}</style>', unsafe_allow_html=True)

# Page title
st.title('💰:blue[Sales & Revenue Analysis]')
st.markdown(" ")

# Create three columns with medium gap and borders
col1, col2, col3 = st.columns(3, gap='small',border=True)

# Display content in col1
with col1:
    st.image('images/sales.png', width=50)
    st.metric(label="Total Sales", value=f"$ {get_total_sales():,.2f}")

with col2:
    st.image('images/order.png', width=50)
    st.metric(label="Total Order", value=f"{get_total_orders():,.0f}")

with col3:
    st.image('images/avg.png', width=50)
    st.metric(label="Average Sales", value=f"$ {get_average_sales():,.2f}")


total1, total2, = st.columns([3,2], gap='large')

with total1:
    with st.container(border=True,height=550):
        st.write("💰 Top 10 Products by Sales")
        st.plotly_chart(get_sales_per_product(), use_container_width=True)

with total2:
    with st.container(border=True, height=550):
        st.write("💰 Total Revenue by Sales Territory")
        st.plotly_chart(get_total_revenue(), use_container_width=True)

       
