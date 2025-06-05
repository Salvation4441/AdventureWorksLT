from connection import connect_to_db #importing the function to connect to the database
import warnings
warnings.filterwarnings('ignore')
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go

## Sales
# 1. What is the total sales generated?
def get_total_sales():
    total_sales = """
        SELECT
            SUM(LineTotal) AS [Total Sales] 
        FROM SalesOrderDetail
    """
    try:
        conn = connect_to_db()
        total_sales_df = pd.read_sql(total_sales, conn)
        total_sales_value = total_sales_df.iloc[0, 0]
        return total_sales_value
    except Exception as e:
        raise Exception(f"Error fetching total sales: {e}") from e
    
# 2. What is the total order generated?
def get_total_orders():
    total_orders = """
            SELECT 
                COUNT(OrderQty) AS [Total Orders]
            FROM SalesOrderDetail
    """

    try:
        conn = connect_to_db()
        total_orders_df = pd.read_sql(total_orders, conn)
        total_orders_value = total_orders_df.iloc[0, 0]
        return total_orders_value
    except Exception as e:
        raise Exception(f"Error fetching total orders: {e}") from e
    
# 3. What is the average sales generated?
def get_average_sales():
    average_sales = """
        SELECT 
            AVG(LineTotal) AS [Average Sales]
        FROM SalesOrderDetail
    """
    try:
        conn = connect_to_db()
        average_sales_df = pd.read_sql(average_sales, conn)
        average_sales_value = average_sales_df.iloc[0, 0]
        return average_sales_value
    except Exception as e:
        raise Exception(f"Error fetching average sales: {e}") from e
    
# 4. Sales generated per a product
def get_sales_per_product():
    query = """
        SELECT 
            p.Name AS [Product Name],
            SUM(od.LineTotal) AS [Total Sales]
        FROM SalesOrderDetail od
        JOIN Product p ON od.ProductID = p.ProductID
        GROUP BY p.Name
        ORDER BY [Total Sales] DESC
        LIMIT 10
    """
    
    try:
        conn = connect_to_db()
        df = pd.read_sql(query, conn)

        fig = px.bar(
            df,
            x='Product Name',
            y='Total Sales',
            color='Product Name',
            labels={'Product Name': 'Product', 'Total Sales': 'Total Sales ($)'},
        )
        
        fig.update_layout(showlegend=False)
        return fig

    except Exception as e:
        raise Exception(f"Error fetching sales per product: {e}") from e


# 5. What is the total revenue per sales territory?
def get_total_revenue():
    query = """
        SELECT 
            st.Name AS [Territory Name],
            SUM(od.LineTotal) AS [Total Revenue]
        FROM SalesOrderDetail od
        JOIN SalesOrderHeader oh ON od.SalesOrderID = oh.SalesOrderID
        JOIN SalesTerritory st ON oh.TerritoryID = st.TerritoryID
        GROUP BY st.Name
        ORDER BY [Total Revenue] DESC
    """

    try:
        conn = connect_to_db()
        df = pd.read_sql(query, conn)

        fig = go.Figure(go.Bar(
            y=df['Territory Name'],
            x=df['Total Revenue'],
            text=df['Total Revenue'].map('${:,.0f}'.format),
            textposition='auto',
            orientation='h',
            marker=dict(
                color=df['Total Revenue'],
                colorscale='Viridis'
            )
        ))

        fig.update_layout(
    
            xaxis_title='Total Revenue ($)',
            yaxis_title='Sales Territory',
            template='plotly_white',
            margin=dict(l=40, r=40, t=60, b=80),
            height=500
        )

        return fig

    except Exception as e:
        raise Exception(f"Error generating histogram: {e}") from e
    

## Customer
# 1. Who are the top 5 customers by total purchases?
