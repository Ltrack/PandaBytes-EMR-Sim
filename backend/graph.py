import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def vitals_graph_grid_plotly(patient):
    vitals = patient["vitals"]
    vitals_dict = {}
    for i in range(len(vitals)):
        vitals_dict[i] = vitals[i]["Time"]
    vitals_df = pd.DataFrame.from_dict(vitals_dict, orient="index")
    vitals_df.columns = ["Time"]
    vitals_df["Time"] = pd.to_datetime(vitals_df["Time"])
    vitals_df["Pulse"] = [vitals[i]["Pulse"] for i in range(len(vitals))]
    vitals_df["Resp"] = [vitals[i]["Resp"] for i in range(len(vitals))]
    vitals_df["BP"] = [vitals[i]["BP"] for i in range(len(vitals))]
    vitals_df["SpO2"] = [vitals[i]["SpO2"] for i in range(len(vitals))]
    vitals_df["Weight_kg"] = [vitals[i]["Weight_kg"] for i in range(len(vitals))]
    vitals_df["MAP_mmHg"] = [vitals[i]["MAP_mmHg"] for i in range(len(vitals))]
    vitals_df["O2_Status"] = [vitals[i]["O2_Status"] for i in range(len(vitals))]
    vitals_df["Temp_C"] = [vitals[i]["Temp_C"] for i in range(len(vitals))]

    # Create subplots
    fig = make_subplots(
        rows=4,
        cols=2,
        subplot_titles=(
            "Pulse",
            "Respiratory Rate",
            "SpO2",
            "Weight (kg)",
            "MAP (mmHg)",
            "Temperature (C)",
            "O2 Status",
            "Blood Pressure",
        ),
    )

    fig.add_trace(
        go.Scatter(x=vitals_df["Time"], y=vitals_df["Pulse"], mode="lines"),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=vitals_df["Time"], y=vitals_df["Resp"], mode="lines"), row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=vitals_df["Time"], y=vitals_df["SpO2"], mode="lines"), row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=vitals_df["Time"], y=vitals_df["Weight_kg"], mode="lines"),
        row=2,
        col=2,
    )
    fig.add_trace(
        go.Scatter(x=vitals_df["Time"], y=vitals_df["MAP_mmHg"], mode="lines"),
        row=3,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=vitals_df["Time"], y=vitals_df["Temp_C"], mode="lines"),
        row=3,
        col=2,
    )
    fig.add_trace(
        go.Scatter(x=vitals_df["Time"], y=vitals_df["O2_Status"], mode="lines"),
        row=4,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=vitals_df["Time"], y=vitals_df["BP"], mode="lines"), row=4, col=2
    )

    fig.update_layout(height=800, width=1200, title_text="Vitals", showlegend=False)
    config = {
        "displaylogo": False,
        "modeBarButtonsToRemove": [
            "zoom2d",
            "pan2d",
            "select2d",
            "lasso2d",
            "zoomIn2d",
            "zoomOut2d",
            "resetScale2d",
            "toImage",
            "hoverClosestCartesian",
            "hoverCompareCartesian",
            "toggleSpikelines",
        ],
    }

    fig = fig.to_html(full_html=False, config=config)
    vitals_table_html = vitals_df.to_html(classes="table table-striped", index=False)

    return fig, vitals_table_html


def labs_graph_grid_plotly(patient):
    labs = patient["labs"]
    labs_dict = {}
    for i in range(len(labs)):
        labs_dict[i] = labs[i]["Time"]
    labs_df = pd.DataFrame.from_dict(labs_dict, orient="index")
    labs_df.columns = ["Time"]
    labs_df["Time"] = pd.to_datetime(labs_df["Time"])
    labs_df["Pulse"] = [labs[i]["Pulse"] for i in range(len(labs))]
    labs_df["Resp"] = [labs[i]["Resp"] for i in range(len(labs))]
    labs_df["BP"] = [labs[i]["BP"] for i in range(len(labs))]
    labs_df["SpO2"] = [labs[i]["SpO2"] for i in range(len(labs))]
    labs_df["Weight_kg"] = [labs[i]["Weight_kg"] for i in range(len(labs))]
    labs_df["MAP_mmHg"] = [labs[i]["MAP_mmHg"] for i in range(len(labs))]
    labs_df["O2_Status"] = [labs[i]["O2_Status"] for i in range(len(labs))]
    labs_df["Temp_C"] = [labs[i]["Temp_C"] for i in range(len(labs))]

    # Create subplots
    fig = make_subplots(
        rows=4,
        cols=2,
        subplot_titles=(
            "Pulse",
            "Respiratory Rate",
            "SpO2",
            "Weight (kg)",
            "MAP (mmHg)",
            "Temperature (C)",
            "O2 Status",
            "Blood Pressure",
        ),
    )

    fig.add_trace(
        go.Scatter(x=labs_df["Time"], y=labs_df["Pulse"], mode="lines"),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=labs_df["Time"], y=labs_df["Resp"], mode="lines"), row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=labs_df["Time"], y=labs_df["SpO2"], mode="lines"), row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=labs_df["Time"], y=labs_df["Weight_kg"], mode="lines"),
        row=2,
        col=2,
    )
    fig.add_trace(
        go.Scatter(x=labs_df["Time"], y=labs_df["MAP_mmHg"], mode="lines"),
        row=3,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=labs_df["Time"], y=labs_df["Temp_C"], mode="lines"),
        row=3,
        col=2,
    )
    fig.add_trace(
        go.Scatter(x=labs_df["Time"], y=labs_df["O2_Status"], mode="lines"),
        row=4,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=labs_df["Time"], y=labs_df["BP"], mode="lines"), row=4, col=2
    )

    fig.update_layout(height=800, width=1200, title_text="Vitals", showlegend=False)
    config = {
        "displaylogo": False,
        "modeBarButtonsToRemove": [
            "zoom2d",
            "pan2d",
            "select2d",
            "lasso2d",
            "zoomIn2d",
            "zoomOut2d",
            "resetScale2d",
            "toImage",
            "hoverClosestCartesian",
            "hoverCompareCartesian",
            "toggleSpikelines",
        ],
    }

    fig = fig.to_html(full_html=False, config=config)
    labs_table_html = labs_df.to_html(classes="table table-striped", index=False)

    return fig, labs_table_html
