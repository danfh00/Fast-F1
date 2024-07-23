import streamlit as st
import matplotlib as mpl

from plot_speed_on_track import create_speed_visualization


def main():
    st.title("F1 Speed Visualization Dashboard")

    st.sidebar.header("Plot Settings")
    year = st.sidebar.selectbox("Year", [2021, 2020, 2019])
    wknd = st.sidebar.number_input(
        "Weekend", min_value=1, max_value=25, value=9)
    session_type = st.sidebar.selectbox("Session Type", ['R', 'Q', 'P'])
    driver = st.sidebar.text_input("Driver", 'RIC')
    colormap = st.sidebar.selectbox(
        "Colormap", [mpl.cm.plasma, mpl.cm.viridis, mpl.cm.inferno])

    st.header("Speed Visualization on Track Map")
    fig = create_speed_visualization(
        year, wknd, session_type, driver, colormap)
    st.pyplot(fig)


if __name__ == "__main__":
    main()
