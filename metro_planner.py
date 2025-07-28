import heapq

class Graph:
    def __init__(self):
        """
        Initializes the graph.
        """
        self.adjacency_list = {}

    def add_station(self, station_name):
        """
        Adds a new station (a node) to our map if it's not already there.
        """
        if station_name not in self.adjacency_list:
            self.adjacency_list[station_name] = []
            print(f"Station '{station_name}' added.")
        else:
            print(f"Station '{station_name}' already exists.")


    def add_route(self, station1, station2, time):
        """
        Adds a route (an edge) between two stations with a travel time.
        """
        if station1 not in self.adjacency_list or station2 not in self.adjacency_list:
            print("Error: One or both stations do not exist.")
            return

        self.adjacency_list[station1].append((station2, time))
        self.adjacency_list[station2].append((station1, time))
        print(f"Route added between '{station1}' and '{station2}' with time {time} mins.")

    # vvvvvv THIS IS THE MISSING PIECE YOU NEEDED vvvvvv
    def dijkstra(self, start_station, end_station):
        """
        Finds the shortest path using Dijkstra's algorithm.
        """
        distances = {station: float('inf') for station in self.adjacency_list}
        distances[start_station] = 0
        
        previous_stations = {station: None for station in self.adjacency_list}
        
        priority_queue = [(0, start_station)]

        while priority_queue:
            current_time, current_station = heapq.heappop(priority_queue)

            if current_time > distances[current_station]:
                continue
            
            if current_station == end_station:
                break

            for neighbor, time in self.adjacency_list[current_station]:
                new_time = distances[current_station] + time

                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    previous_stations[neighbor] = current_station
                    heapq.heappush(priority_queue, (new_time, neighbor))
        
        path = []
        station = end_station
        while station is not None:
            path.insert(0, station)
            station = previous_stations[station]
            
        if distances[end_station] == float('inf'):
            return None, float('inf')

        return path, distances[end_station]
    # ^^^^^^ THE MISSING PIECE ENDS HERE ^^^^^^

if __name__ == "__main__":
    mumbai_metro = Graph()

    # Add stations
    stations = ["Churchgate", "Marine Lines", "Charni Road", "Grant Road", "Mumbai Central", "Mahalaxmi"]
    for station in stations:
        mumbai_metro.add_station(station)

    # Add routes
    mumbai_metro.add_route("Churchgate", "Marine Lines", 2)
    mumbai_metro.add_route("Marine Lines", "Charni Road", 3)
    mumbai_metro.add_route("Charni Road", "Grant Road", 4)
    mumbai_metro.add_route("Grant Road", "Mumbai Central", 2)
    mumbai_metro.add_route("Mumbai Central", "Mahalaxmi", 3)
    
    # Add a "shortcut" route to test Dijkstra's
    mumbai_metro.add_route("Marine Lines", "Grant Road", 8) 
    # The path through Charni Road should be faster (3+4=7)

    print("-" * 20)

    # Find and print the shortest path
    start = "Churchgate"
    end = "Mumbai Central"
    path, time = mumbai_metro.dijkstra(start, end)

    if path:
        print(f"Shortest path from '{start}' to '{end}':")
        print(f"Path: {' -> '.join(path)}")
        print(f"Total time: {time} minutes")
    else:
        print(f"No path found from '{start}' to '{end}'.")