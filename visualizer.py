from dash import Dash, dcc, html
import pandas
from plotly.express import line

data = "./formatted.csv"
data_reader = pandas.read_csv(data)
data_reader = data_reader.sort_values(by="date")

dash_app = Dash(__name__)

chart = line(data_reader, x="date", y="sales", title="Pink Morsel sales")
visual = dcc.Graph(id="visual", figure=chart)

header = html.Header("Pink Morsel visualization", id = "header")
dash_app.layout = html.Div([header, visual])

if __name__ == "__main__":
    dash_app.run()