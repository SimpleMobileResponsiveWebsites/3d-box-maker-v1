import streamlit as st
import plotly.graph_objects as go

def render_3d_box(x, y, z, width, height, depth):
    """Generate a 3D box."""
    # Define vertices of the box
    vertices = [
        (x, y, z), (x + width, y, z), (x + width, y + depth, z), (x, y + depth, z),  # Bottom face
        (x, y, z + height), (x + width, y, z + height), (x + width, y + depth, z + height), (x, y + depth, z + height),  # Top face
    ]

    # Define edges by connecting vertices
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
        (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
        (0, 4), (1, 5), (2, 6), (3, 7),  # Vertical edges
    ]

    # Create 3D box
    fig = go.Figure()
    for edge in edges:
        x_coords = [vertices[edge[0]][0], vertices[edge[1]][0]]
        y_coords = [vertices[edge[0]][1], vertices[edge[1]][1]]
        z_coords = [vertices[edge[0]][2], vertices[edge[1]][2]]
        fig.add_trace(go.Scatter3d(x=x_coords, y=y_coords, z=z_coords, mode='lines'))

    # Update layout
    fig.update_layout(
        scene=dict(
            xaxis=dict(nticks=10, range=[0, 10]),
            yaxis=dict(nticks=10, range=[0, 10]),
            zaxis=dict(nticks=10, range=[0, 10]),
        ),
        margin=dict(r=0, l=0, b=0, t=0)
    )
    return fig

# Streamlit app
st.title("3D Box Renderer")
st.sidebar.header("Box Dimensions")

# Input box dimensions
x = st.sidebar.number_input("X-coordinate", value=0.0)
y = st.sidebar.number_input("Y-coordinate", value=0.0)
z = st.sidebar.number_input("Z-coordinate", value=0.0)
width = st.sidebar.number_input("Width", value=1.0, min_value=0.1)
height = st.sidebar.number_input("Height", value=1.0, min_value=0.1)
depth = st.sidebar.number_input("Depth", value=1.0, min_value=0.1)

# Render button
if st.sidebar.button("Render Box"):
    fig = render_3d_box(x, y, z, width, height, depth)
    st.plotly_chart(fig, use_container_width=True)
