# 🚇 Metro Route Planner & Dijkstra's Algorithm Visualizer

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=for-the-badge&logo=streamlit)

An interactive web application that calculates the fastest route between two stations in a metro network, built from the ground up using core data structures and Dijkstra's shortest path algorithm.

---

### 📍 Live Demo Screenshot

*(I recommend you replace this with a screenshot of your own running application!)*

![App Screenshot](https://i.imgur.com/uI67LzK.png)

---

### ✨ Overview

This project is a practical implementation of fundamental graph theory to solve a common real-world problem: finding the most efficient path through a network. The application models a metro system as a weighted, undirected graph and uses Dijkstra's algorithm to identify the route with the minimum travel time between any two selected stations.

The backend logic is built entirely in Python, focusing on efficiency and clean, object-oriented design. The frontend is a user-friendly web interface created with Streamlit.

---

### 🚀 Key Features

- **Interactive UI:** Select start and end stations from dynamic dropdown menus.
- **Fastest Route Calculation:** Instantly computes the optimal path using Dijkstra's algorithm.
- **Detailed Path Display:** Clearly shows the sequence of stations in the fastest route.
- **Total Travel Time:** Calculates and displays the total time for the journey in minutes.
- **Scalable Graph Structure:** Easily add new stations and routes to expand the network.

---

### 🧠 Core Concepts Demonstrated

This project serves as a strong showcase of foundational computer science principles:

- **Graph Data Structure:** The entire metro network is modeled using an **Adjacency List** (a dictionary of lists in Python). This provides an efficient way to store and access station connections and travel times (edge weights).
- **Dijkstra's Shortest Path Algorithm:** The core engine of the application. The algorithm is implemented from scratch to methodically find the shortest path from a starting node to all other nodes in a weighted graph.
- **Priority Queue (Min-Heap):** A `heapq` (min-heap) is used as a priority queue to make the Dijkstra's algorithm implementation highly efficient. It ensures that the next station to visit is always the one with the currently known shortest travel time, which is the "greedy" choice that guarantees an optimal solution.
- **Object-Oriented Programming (OOP):** The entire system is encapsulated within a `Graph` class, separating the data structure and logic from the user interface.

---

### 🛠️ Tech Stack

- **Backend:** Python
- **Frontend:** Streamlit
- **Core Libraries:** `heapq` for the priority queue implementation.

---

### ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/metro-planner.git](https://github.com/your-username/metro-planner.git)
    cd metro-planner
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    *(First, make sure you have a `requirements.txt` file by running `pip freeze > requirements.txt` in your local project directory)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    Your web browser should automatically open with the running application.

---

### 📂 File Structure

The project is organized into two main files:

-   `metro_planner.py`: The backend module. It contains the `Graph` class, which encapsulates all the logic for creating the metro network and implementing Dijkstra's algorithm.
-   `app.py`: The frontend application script. It uses the Streamlit library to build the user interface and calls the `Graph` class from the backend to perform calculations.

