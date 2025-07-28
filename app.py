import streamlit as st
from metro_planner import Graph # Import our backend class

# --- Page Configuration ---
st.set_page_config(page_title="Metro Route Planner", page_icon="🚇", layout="centered")

# --- Function to build the graph ---
# We use @st.cache_resource to build the graph only once.
@st.cache_resource
def load_metro_map():
    mumbai_metro = Graph()
    stations = ["Churchgate", "Marine Lines", "Charni Road", "Grant Road", "Mumbai Central", "Mahalaxmi"]
    for station in stations:
        mumbai_metro.add_station(station)
    
    mumbai_metro.add_route("Churchgate", "Marine Lines", 2)
    mumbai_metro.add_route("Marine Lines", "Charni Road", 3)
    mumbai_metro.add_route("Charni Road", "Grant Road", 4)
    mumbai_metro.add_route("Grant Road", "Mumbai Central", 2)
    mumbai_metro.add_route("Mumbai Central", "Mahalaxmi", 3)
    mumbai_metro.add_route("Marine Lines", "Grant Road", 8)
    
    return mumbai_metro

# Load the graph
metro_map = load_metro_map()
station_list = list(metro_map.adjacency_list.keys())

# --- UI Elements ---
st.title("🚇 Mumbai Metro Route Planner")
st.write("Select your start and end stations to find the fastest route.")

# Dropdown menus for station selection
start_station = st.selectbox("From:", station_list)
end_station = st.selectbox("To:", station_list)

# Button to trigger the calculation
if st.button("Find Fastest Route"):
    if start_station == end_station:
        st.warning("Start and end stations cannot be the same.")
    else:
        # Call the backend dijkstra method
        path, time = metro_map.dijkstra(start_station, end_station)

        if path:
            st.success(f"Fastest route found in {time} minutes!")
            # Display the path in a more visually appealing way
            st.markdown(f"**Path:** `{' → '.join(path)}`")
        else:
            st.error("No path could be found between the selected stations.")