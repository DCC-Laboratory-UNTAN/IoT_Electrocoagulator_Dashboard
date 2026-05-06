"""
Styling Utilities Module

This module provides helper functions for applying custom CSS styling to Streamlit components.
It enables consistent theming and visual enhancements throughout the application.

Functions:
- apply_metric_style(): Colors metric cards with custom background
- status_box(): Creates colored ON/OFF status indicators
- horizontal_rule(): Renders styled divider lines

Colors used:
- Blue (#3498DB): Default metric background
- Dark Green (#1f7a3e): Active/ON status
- Dark Red (#7a1f1f): Inactive/OFF status
"""

import streamlit as st


def apply_metric_style(color: str = "#3498DB") -> None:
    """
    Apply custom CSS styling to st.metric components.
    
    Args:
        color (str): Hexadecimal color code for metric card background.
                    Default: #3498DB (light blue)
    
    Effect:
    - Injects CSS that targets all metric elements
    - Applies background color, padding, and border radius
    - Creates a more visually cohesive dashboard
    """
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
    """
    Render a colored status indicator box for actuator ON/OFF display.
    
    Args:
        label (str): Name of the actuator (e.g., "Mixing Motor")
        status (str): Status text, typically "ON" or "OFF"
    
    Visual Design:
    - Green background (#1f7a3e) for ON status
    - Red background (#7a1f1f) for OFF status
    - White text with bold status indicator
    - Rounded corners and padding for clarity
    
    Usage:
    Used in render_actuator_status() to display a quick visual overview
    of which actuators are currently running.
    """
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
    """
    Render a thin horizontal divider (separator line).
    
    Args:
        margin (str): CSS margin property to control vertical spacing.
                     Default: "5px 0" (5px top and bottom margin)
    
    Usage:
    Used to visually separate sections of the dashboard and improve readability.
    
    Example:
    horizontal_rule()  # Default spacing
    horizontal_rule("10px 0")  # Larger spacing
    """
    st.markdown(
        f"<hr style='margin:{margin}'>",
        unsafe_allow_html=True,
    )