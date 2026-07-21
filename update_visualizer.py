from dash import Dash, html, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px

dash_app = Dash(__name__)

df = pd.read_csv("./merged_data.csv")
df = df.sort_values("Date")

dash_app.layout = html.Div([
    html.H1("Welcome to Dash"),
   
    dcc.RadioItems(
        options=['north', 'south', 'east', 'west', 'all'],
        value='north',
        id='input_vals',
        inline=True
    ),

     dcc.Graph(id="visualiser"),
])

@callback(
    Output("visualiser", "figure"),
    Input("input_vals", "value")
)
def update_graph(region):
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == region]

    fig = px.line(filtered_df, x="Date", y="Sales")
    return fig

if __name__ == "__main__":
    dash_app.run(debug=True)