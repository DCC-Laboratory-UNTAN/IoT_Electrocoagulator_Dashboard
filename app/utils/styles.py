import streamlit as st


def apply_metric_style(color: str = "#3498DB") -> None:
    """Inject CSS to style st.metric cards."""
    st.markdown(
        f"""
        <style>
        div[data-testid="stMetric"] {{
            background-color: {color};
            padding: 10px;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def status_box(label: str, status: str) -> None:
    """Render a colored ON/OFF status box."""
    color = "#1f7a3e" if status == "ON" else "#7a1f1f"
    st.markdown(
        f"""
        <div style="
            background-color:{color};
            padding:10px;
            border-radius:8px;
            margin-bottom:20px;
            color:white;
        ">
            {label}: <strong>{status}</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )


def horizontal_rule(margin: str = "5px 0") -> None:
    """Render a thin horizontal divider."""
    st.markdown(
        f"<hr style='margin:{margin}'>",
        unsafe_allow_html=True,
    )