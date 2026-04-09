from dash import Dash, dcc, html, Input, Output
import pandas
import plotly.express as px

data = "./formatted.csv"
data_reader = pandas.read_csv(data)
data_reader = data_reader.sort_values(by="date")

dash_app = Dash(__name__)

radio = dcc.RadioItems(id="radio",
                       options=["all", "north", "east", "south", "west"],
                       value="all",
                       inline=True,
                       style={"marginBottom": "20px"},
                       labelStyle={"fontSize": "18px"})

visual = dcc.Graph(id="visual",
                   style={"width": "100%",
                          "margin": "auto",
                          "backgroundColor": "lightpink",
                          "borderRadius": "10px",
                          "padding": "10px"})

header = html.H1("Pink Morsel visualization", id = "header",
                 style = {"textAlign": "center", "padding": "20px", "color": "white"})
dash_app.layout = html.Div([header, radio, visual], style={
    "background": "linear-gradient (to right, #667eea, #764ba2", "minHeight": "100vh"})

@dash_app.callback(
    Output("visual", "figure"),
    Input("radio", "value")
)
def update_graph(selected_radio):
    if selected_radio == "all":
        filtered_data = data_reader
    else:
        filtered_data = data_reader[data_reader["region"] == selected_radio]

    chart = px.line(filtered_data, x="date", y="sales")

    return chart



if __name__ == "__main__":
    dash_app.run()