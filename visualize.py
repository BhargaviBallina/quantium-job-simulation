from dash import Dash, html, dcc
import plotly.express as px
# from plotly.express import line
import pandas as pd

data_dir = "./merged_data.csv"

dash_app = Dash()



df = pd.read_csv(data_dir)
df= df.sort_values(by="Date")
fig = px.bar(df, x="Date", y="Sales", title="Sales increase visualiser") 

# fig = line(df, x="Date", y="Sales", title="Sales increase visualiser") 
header=html.Div([
    html.H1("Pink Morsel sales visualiser"),
    # html.Div("Hey there")
]
)
graph= dcc.Graph(
    id="pink morsel",
    figure=fig,
    
)
dash_app.layout = [
    header,
    graph
]


if __name__ == '__main__':
    dash_app.run(debug=True)