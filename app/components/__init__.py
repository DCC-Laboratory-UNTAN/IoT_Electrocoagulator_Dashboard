"""
Components Package - Reusable UI Components

This package contains modular UI components that can be rendered independently.
Each module focuses on a specific aspect of the dashboard:

- actuator_status.py: Display component for actuator ON/OFF states
- process_history.py: Chart component for historical data visualization
- sensor_data.py: Display components for water quality and level metrics
- sidebar.py: Control component for system operation and manual actuator control

Benefits of modular components:
- Each component is independently testable
- Easy to reuse or modify without affecting other parts
- Cleaner main.py with better separation of concerns
- Easier to maintain and debug
"""
