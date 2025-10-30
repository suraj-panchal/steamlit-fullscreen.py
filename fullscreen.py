import streamlit as st
import plotly.graph_objects as go

# Example figure
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='lines+markers',
    name='Sample Data'
))

# === UPDATED LAYOUT FOR FULL SCREEN ===
fig.update_layout(
    title=f"GCF07 Graph ({'Auto Mode' if True else 'Manual Mode'})",
    xaxis=dict(title="DateTime", tickformat="%d:%H:%M", tickangle=45),
    yaxis=dict(title="Production / Electricity", side="left", range=[0, 3], dtick=0.5),
    yaxis2=dict(title="Air Pressure", overlaying="y", side="right", range=[0, 1000], dtick=100),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
    template="plotly_white",
    autosize=True,  # <-- enables responsive resizing
    height=None,    # <-- removes fixed height
    margin=dict(l=0, r=0, t=80, b=0)  # reduces padding for true fullscreen
)

# === Streamlit Full Screen Display ===
st.set_page_config(layout="wide")  # <-- this makes the whole page wide
st.plotly_chart(fig, use_container_width=True)  # <-- stretches chart to full width
