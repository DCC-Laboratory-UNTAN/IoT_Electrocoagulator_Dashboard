import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from app.config import DATA_PATH


def render_process_history() -> None:
    """Load and display the process history chart."""
    st.subheader("Process History (Last Hour)")

    try:
        df = pd.read_excel(DATA_PATH)
    except FileNotFoundError:
        st.warning(f"Data file not found at `{DATA_PATH}`. Please add `process_history.xlsx` to the `data/` folder.")
        return
    except Exception as e:
        st.error(f"Failed to load process history: {e}")
        return

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Time"], y=df["pH"], mode="lines+markers", name="pH Level"))
    fig.add_trace(go.Scatter(x=df["Time"], y=df["Turbidity (NTU)"], mode="lines+markers", name="Turbidity (NTU)"))
    fig.add_trace(go.Scatter(x=df["Time"], y=df["Flow Rate (L/min)"], mode="lines+markers", name="Flow Rate (L/min)"))

    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Value",
        legend_title="Sensors",
        hovermode="x unified",
    )

    st.plotly_chart(fig, use_container_width=True)