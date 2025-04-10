from preswald import plotly, connect, get_df, selectbox, button, text, table, query
import pandas as pd
import plotly.express as px

# Load the data
connect()
df = get_df('online_shoppers_intention')

# Create a bar chart using Plotly Express
fig = px.bar(df, x='Month', y='Revenue', title='Monthly Revenue from Online Shoppers',
             labels={'Revenue': 'Revenue Generated', 'Month': 'Month of the Year'})

# Style the plot
fig.update_layout(template='plotly_white')

# Show the plot
plotly(fig)

sql_query = """
SELECT *
FROM online_shoppers_intention
WHERE VisitorType = 'Returning_Visitor' AND Month = 'Feb'
"""

# Execute the query
returning_users_feb = query(sql_query, 'online_shoppers_intention')
text("## Returning users on february")
table(returning_users_feb)

# Data summary
text("## Data Summary for Online Shoppers' Intention Dataset")
text("The dataset contains records of website visits by online shoppers and captures various metrics related to their browsing behavior on a website. Key metrics include:")
text("- **Administrative, Informational, ProductRelated**: Different types of pages visited by the user.")
text("- **Duration**: Time spent on these page categories.")
text("- **BounceRates, ExitRates**: Metrics indicating the quality of the visit.")
text("- **PageValues**: The average value of the pages visited by the user.")
text("- **SpecialDay**: Closeness of the site visiting time to a special day.")
text("- **Month**: Month of the visit.")
text("- **OperatingSystems, Browser, Region, TrafficType**: Technical details of the visit.")
text("- **VisitorType**: Indicates if the visitor is new or returning.")
text("- **Weekend**: If the visit happened during the weekend.")
text("- **Revenue**: Indicates if the visit resulted in a revenue.")

text("The dataset includes both categorical and numerical data, with a mix of user engagement metrics and technical details of the visit. This combination of features can be used to analyze user behavior patterns, predict future behavior, or segment users based on their interaction with the website.")

