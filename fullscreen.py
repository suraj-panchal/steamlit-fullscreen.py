import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta

# === 1️⃣ Streamlit Page Config ===
st.set_page_config(page_title="GCF07 Fullscreen Graph", layout="wide")

# === 2️⃣ Hide Streamlit Default UI & make container fullscreen ===
st.markdown("""
    <style>
        header, footer, [data-testid="stToolbar"], [data-testid="stSidebar"], 
        [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
            display: none !important;
        }
        /* Fullscreen block container */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
        }
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: white;
        }
        /* Ensure iframe or Plotly chart takes full height */
        iframe, div[data-testid="stPlotlyChart"] > div {
            width: 100vw !important;
            height: 100vh !important;
        }
    </style>
""", unsafe_allow_html=True)

# === 3️⃣ Sample Data ===
start = datetime(2025, 10, 30, 8, 0)
times = [start + timedelta(minutes=30 * i) for i in range(8)]
values_production = [0.5, 1.2, 2.5, 1.8, 1.9, 2.2, 2.0, 2.5]
values_pressure = [300, 500, 400, 700, 650, 800, 750, 900]

# === 4️⃣ Create Plotly Figure ===
fig = go.Figure()

# Production Line
fig.add_trace(go.Scatter(
    x=times,
    y=values_production,
    mode="lines+markers",
    name="Production",
    line=dict(width=3, color="royalblue")
))

# Air Pressure Line (Right Y-Axis)
fig.add_trace(go.Scatter(
    x=times,
    y=values_pressure,
    mode="lines+markers",
    name="Air Pressure",
    yaxis="y2",
    line=dict(width=3, color="red")
))

# === 5️⃣ Layout Settings ===
fig.update_layout(
    title=dict(
        text="GCF07 Fullscreen Graph",
        x=0.5,
        font=dict(size=22, color="black")
    ),
    xaxis=dict(
        title=dict(text="DateTime (30-min intervals)", font=dict(size=16)),
        tickformat="%H:%M",
        dtick=1800000,  # 30 minutes in ms
        showgrid=True,
        gridcolor="lightgrey",
        tickangle=45,
        constrain="domain"
    ),
    yaxis=dict(
        title=dict(text="Production", font=dict(size=16)),
        showgrid=True,
        gridcolor="lightgrey",
        constrain="domain"
    ),
    yaxis2=dict(
        title=dict(text="Air Pressure", font=dict(size=16)),
        overlaying="y",
        side="right",
        showgrid=False,
        range=[0, 1000]
    ),
    template="plotly_white",
    autosize=True,
    margin=dict(l=0, r=0, t=40, b=40),
)

# === 6️⃣ Remove Plotly Toolbar ===
config = {
    "displayModeBar": False,  # hide all toolbar icons
    "staticPlot": False,
    "responsive": True
}

# === 7️⃣ Display Chart Fullscreen & Responsive ===
st.plotly_chart(fig, use_container_width=True, config=config)

# === 8️⃣ Extra: Auto-resize when tablet rotates (optional) ===
# Streamlit automatically resizes the container, but this ensures chart scales dynamically
st.markdown("""
    <script>
        window.addEventListener("resize", () => {
            let charts = document.querySelectorAll('[data-testid="stPlotlyChart"] > div');
            charts.forEach(c => {
                c.style.width = window.innerWidth + 'px';
                c.style.height = window.innerHeight + 'px';
            });
        });
    </script>
""", unsafe_allow_html=True)
