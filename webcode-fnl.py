
from dash import Dash, dcc, Input, Output,html,ctx
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
import plotly.graph_objs as go
df = pd.read_csv(
    "dta.csv"
)

df["Data_Date"] = pd.to_datetime(df["Data_Date"])

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dcc.Markdown(
            "#### DASHBOARD",
            style={"textAlign": "center"},
            className="my-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id="datepicker",
                            min_date_allowed=min(df["Data_Date"]),
                            max_date_allowed=date(2026, 12, 12),
                            end_date=max(df["Data_Date"]),
                            start_date=min(df["Data_Date"]),
                            clearable=True,
                        ),
                        

                    ],
                    width=5,
                ),
                dbc.Col(
                    [
                        dcc.Tabs(
                            id="tabs",
                            value="tab-1",style={
                               'width': '150%',
                               
                               },
                            children=[
                                dcc.Tab(
                                    label="Temperature",
                                    value="tab-1",
                                    children=[dcc.Graph(id="pie1")],
                                ),
                                dcc.Tab(
                                    label="Humidity",
                                    value="tab-2",
                                    children=[dcc.Graph(id="pie2")],
                                ),
                                dcc.Tab(
                                    label="sleep Hours",
                                    value="tab-3",
                                    children=[dcc.Graph(id="pie3")],
                                ),
                                dcc.Tab(
                                    label="Snore",
                                    value="tab-4",
                                    children=[dcc.Graph(id="pie4")],
                                ),
                                dcc.Tab(
                                    label="REM Cycle",
                                    value="tab-5",
                                    children=[dcc.Graph(id="pie5")],
                                ),


                            ],
                        ),
                    ],
                    width=8,
                ),
            ]
        ),
    ]
)


@app.callback(
    Output("pie1", "figure"),
    Output("pie2", "figure"),
    Output("pie3", "figure"),
    Output("pie4", "figure"),
    Output("pie5", "figure"),
    Input("datepicker", "start_date"),
    Input("datepicker", "end_date"),
)
def render_content(start_date, end_date):
    df = pd.read_csv(
    "dta.csv"
    )

    df["Data_Date"] = pd.to_datetime(df["Data_Date"])
    #end_date=max(df["Data_Date"])


    dff = df.query("Data_Date > @start_date & Data_Date < @end_date")

    pie1_fig = px.line(x=dff["Data_Date"], y=dff["temperature"])
    pie2_fig = px.line(x=dff["Data_Date"], y=dff["humidity"])
    pie3_fig = px.line(x=dff["Data_Date"], y=dff["sleephr"])
    pie4_fig = px.line(x=dff["Data_Date"], y=dff["sound"])
    pie5_fig = px.line(x=dff["Data_Date"], y=dff["rem"])

    return (pie1_fig, pie2_fig, pie3_fig, pie4_fig, pie5_fig)







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050,debug=True)
