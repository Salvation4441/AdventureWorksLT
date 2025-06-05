import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Page config
st.set_page_config(layout="wide", page_title="Dashboard")

# Inject custom CSS for card styling
st.markdown("""
    <style>
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .metric-card {
        text-align: center;
        padding: 1rem;
        border-radius: 1rem;
        background-color: #f9fafb;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Sample metrics
total_revenue = 72408
percentage_growth = 17
user_count = 2534

# Sidebar
with st.sidebar:
    st.title("📊 Menu")
    st.markdown("Dashboard")
    st.markdown("Settings")

# KPI cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Total Revenue", f"${total_revenue:,}")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Growth", f"{percentage_growth}%", delta=f"{percentage_growth}%")
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Users", f"{user_count:,}")
    st.markdown('</div>', unsafe_allow_html=True)

# Charts in cards
st.markdown("### 📈 Analytics Overview")

col4, col5, col6 = st.columns(3)

with col4:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Monthly Revenue Trend")
        x = pd.date_range(start='2024-01-01', periods=12, freq='M')
        y = np.random.randint(5000, 9000, size=12)
        fig_line = px.line(x=x, y=y, labels={'x': 'Month', 'y': 'Revenue'})
        st.plotly_chart(fig_line, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col5:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Category Performance")
        data_bar = pd.DataFrame({
            'Category': ['A', 'B', 'C', 'D', 'E'],
            'Values': np.random.randint(1000, 5000, 5)
        })
        fig_bar = px.bar(data_bar, x='Category', y='Values')
        st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col6:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Segment Distribution")
        data_donut = pd.DataFrame({
            'Segment': ['Alpha', 'Beta', 'Gamma', 'Delta'],
            'Value': [40, 30, 20, 10]
        })
        fig_donut = px.pie(data_donut, names='Segment', values='Value', hole=0.5)
        st.plotly_chart(fig_donut, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Filters in a card
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📅 Filters")
    col7, col8 = st.columns(2)
    with col7:
        st.selectbox("Start Date", ["2024-01", "2024-02", "2024-03"])
    with col8:
        st.selectbox("Category", ["All", "A", "B", "C"])
    st.markdown('</div>', unsafe_allow_html=True)

# Table in a card
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 Data Table")
    df = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=10),
        'Category': np.random.choice(['A', 'B', 'C'], size=10),
        'Value': np.random.randint(100, 1000, size=10)
    })
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
