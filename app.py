import streamlit as st
import pandas as pd #easy to use open source data analysis and manipulate data
import numpy as np #used for working with arrays.
import plotly.express as px # used for data visualization
import plotly.graph_objects as go
import streamlit as st 

from connection import connect_to_db
import warnings
warnings.filterwarnings('ignore')


pd.set_option('display.max_colwidth',None)
pd.set_option('display.max_columns',None)


# Define pages
# dashboard = st.Page("report/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True)
sales = st.Page("reports/sales.py", title="Sales", icon=":material/euro:")
customer = st.Page("reports/customer.py", title="Customer", icon=":material/group:")
product = st.Page("reports/product.py", title="Production", icon=":material/category:")


# Navigation
pg = st.navigation(
    {
        "Reports": [sales, customer, product],
    }
)

pg.run()
