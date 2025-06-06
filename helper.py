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
def get_top_purchase():
    query = """
        SELECT 
            c.CustomerID,
            SUM(soh.TotalDue) AS [Total Purchases]
        FROM Customer AS c
        JOIN SalesOrderHeader AS soh
            ON c.CustomerID = soh.CustomerID
        GROUP BY c.CustomerID
        ORDER BY [Total Purchases] DESC
        LIMIT 5
    """
    
    try:
        conn = connect_to_db()
        df = pd.read_sql(query, conn)
        df['CustomerID'] = df['CustomerID'].astype(str)

        fig = px.bar(
            df,
            x='CustomerID',
            y='Total Purchases',
            orientation='h',
            text='Total Purchases',
            color='CustomerID',
            labels={
                'CustomerID': 'Customer ID',
                'Total Purchases': 'Total Purchases ($)'
            },
            color_discrete_sequence=px.colors.sequential.Viridis
        )
        
        fig.update_traces(
            texttemplate='$%{text:,.0f}', 
            textposition='auto',
        )
        fig.update_layout(
            # showlegend=False,
            xaxis_title='Total Purchases ($)',
            yaxis_title='Customer ID',
            template='plotly_white',
            margin=dict(l=10, r=10, t=40, b=5)
        )
        
        return fig

    except Exception as e:
        raise Exception(f"Error fetching top customers: {e}") from e
    
# 2. What is the total number of orders per customer?
def get_orders_per_customer():
    query = """
        SELECT
            c.CustomerID,
            COUNT(soh.SalesOrderID) AS [Total Orders]
        FROM Customer c
        JOIN SalesOrderHeader soh
            ON c.CustomerID = soh.CustomerID
        GROUP BY c.CustomerID
        ORDER BY [Total Orders] DESC
        LIMIT 10
    """

    try:
        conn = connect_to_db()
        df = pd.read_sql(query, conn)
        df['CustomerID'] = df['CustomerID'].astype(str)  # Make sure CustomerID is string for display

        fig = px.bar(
            df,
            y='CustomerID',
            x='Total Orders',
            text='Total Orders',
            color='CustomerID',
            labels={'CustomerID': 'Customer ID', 'Total Orders': 'Number of Orders'},
            color_discrete_sequence=px.colors.sequential.Teal
        )

        fig.update_traces(textposition='outside')
        fig.update_layout(
            xaxis_title='Customer ID',
            yaxis_title='Total Orders',
            showlegend=False,
            template='plotly_white',
            margin=dict(l=40, r=40, t=60, b=40)
        )

        return fig

    except Exception as e:
        raise Exception(f"Error fetching orders per customer: {e}") from e
    

# 3. Which territory has the most customers?
def get_territory_per_customer():
    query = """
        SELECT 
            st.Name AS [Territory Name], 
            COUNT(c.CustomerID) AS [Number of Customers]
        FROM Customer c
        JOIN SalesTerritory st 
            ON c.TerritoryID = st.TerritoryID
        GROUP BY st.Name
        ORDER BY [Number of Customers] DESC
    """

    try:
        conn = connect_to_db()
        df = pd.read_sql(query, conn)

        fig = px.bar(
            df,
            x='Territory Name',
            y='Number of Customers',
            text='Number of Customers',
            color='Territory Name',
            labels={
                'Territory Name': 'Sales Territory',
                'Number of Customers': 'Number of Customers'
            },
            color_discrete_sequence=px.colors.sequential.Teal
        )

        fig.update_traces(textposition='outside')
        fig.update_layout(
            xaxis_title='Sales Territory',
            yaxis_title='Number of Customers',
            showlegend=False,
            template='plotly_white',
            margin=dict(l=40, r=40, t=60, b=40)
        )

        return fig

    except Exception as e:
        raise Exception(f"Error fetching customers per territory: {e}") from e
    

## Product
#1.  Which product has the highest average unit price sold?
def get_highest_avg_price_chart():
    
    query = """
        SELECT 
            p.Name AS [Product Name],
            AVG(sod.UnitPrice) AS [Average Unit Price]
        FROM SalesOrderDetail sod
        JOIN Product p 
        ON sod.ProductID = p.ProductID
        GROUP BY p.Name
        ORDER BY [Average Unit Price] DESC
        LIMIT 10
    """
    
    try:
        conn = connect_to_db()
        df = pd.read_sql(query, conn)

        fig = px.line(
            df,
            x='Product Name',
            y='Average Unit Price',
            markers=True,
            labels={'Product Name': 'Product', 'Average Unit Price': 'Avg. Unit Price ($)'}
        )
        fig.update_traces(line=dict(color='royalblue', width=3))
        fig.update_layout(
            xaxis_tickangle=-45,
            template='plotly_white',
            height=650,
            margin=dict(l=40, r=40, t=60, b=10),
            showlegend=True
        )

        return fig
    
    except Exception as e:
        raise Exception(f"Error generating chart for highest average unit price: {e}") from e
