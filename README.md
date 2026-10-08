# Intelligent Route Planner Using Graph Algorithms

## 🚀 Project Overview

The Intelligent Route Planner Using Graph Algorithms is a Data Structures and Algorithms (DSA) project that simulates how modern navigation and route optimization systems work. The application models locations as graph nodes and roads as weighted edges, enabling users to find optimal routes between locations using efficient graph algorithms.

The project demonstrates real-world applications of Graph Theory, BFS, DFS, Dijkstra’s Algorithm, Priority Queues, and Path Reconstruction techniques commonly used in navigation systems such as Google Maps, Uber, Ola, logistics platforms, and delivery applications.

---

## 🎯 Problem Statement

Finding the optimal route between locations is a fundamental problem in transportation, logistics, ride-hailing, and navigation systems. Traditional manual route planning becomes inefficient as the number of locations and road connections increases.

This project solves the route optimization problem by representing a transportation network as a weighted graph and applying graph algorithms to compute the shortest and most efficient route between a source and destination.

---

## ✨ Features

* Graph Representation using Adjacency List
* Breadth First Search (BFS) Traversal
* Depth First Search (DFS) Traversal
* Dijkstra’s Shortest Path Algorithm
* Priority Queue (Min Heap) Optimization
* Route Reconstruction
* Route Summary Generation
* Execution Time Analysis
* Nodes Exploration Statistics
* Graph Visualization using NetworkX
* Report Generation and File Handling
* Interactive Command Line Interface (CLI)
* Modular and Scalable Project Structure

---

## 🏗️ System Workflow

Location Input
→ Graph Creation
→ Adjacency List Storage
→ BFS / DFS Traversal
→ Dijkstra Algorithm
→ Route Reconstruction
→ Distance Calculation
→ Route Summary Generation
→ Graph Visualization

---

## 🧠 DSA Concepts Used

### Graph

Locations are represented as nodes and roads are represented as weighted edges.

### Adjacency List

Efficient graph storage structure for sparse networks.

### Breadth First Search (BFS)

Traverses the graph level by level.

### Depth First Search (DFS)

Explores nodes deeply before backtracking.

### Dijkstra's Algorithm

Computes the shortest path between source and destination.

### Priority Queue (Min Heap)

Optimizes shortest path computation using Python's heapq module.

### Path Reconstruction

Rebuilds the complete shortest route after algorithm execution.

---

## ⚙️ Technologies Used

* Python
* NetworkX
* Matplotlib
* Heapq
* JSON
* Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
Intelligent-Route-Planner-Graph-Algorithms/
│
├── data/
│   └── city_graph.json
│
├── src/
│   ├── graph.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── dijkstra.py
│   ├── report.py
│   └── visualization.py
│
├── outputs/
│   ├── route_report.txt
│   └── graph_visualization.png
│
├── images/
│   ├── image1.png
│   ├── image2.png
│   ├── image3.png
│   ├── image4.png
│   ├── image5.png
│   ├── image6.png
│   └── image7.png
│
├── docs/
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Intelligent-Route-Planner-Graph-Algorithms.git
```

### Navigate to Project

```bash
cd Intelligent-Route-Planner-Graph-Algorithms
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or

```bash
pip install networkx matplotlib
```

---

## ▶️ Run Project

```bash
python main.py
```

---

## 📋 CLI Menu

```text
1. Display Graph
2. BFS Traversal
3. DFS Traversal
4. Find Shortest Route
5. Generate Route Report
6. Visualize Graph
7. Exit
```

---

## 📊 Sample Output

```text
==================================================
INTELLIGENT ROUTE PLANNER
==================================================

Shortest Route:
A -> C -> D -> E

Total Distance: 6 km

Nodes Explored: 5

Execution Time: 0.0821 ms
```

---

## 📈 Algorithm Complexity

### BFS

```text
Time Complexity: O(V + E)
Space Complexity: O(V)
```

### DFS

```text
Time Complexity: O(V + E)
Space Complexity: O(V)
```

### Dijkstra Algorithm

```text
Time Complexity: O((V + E) log V)
Space Complexity: O(V)
```

Where:

* V = Number of Vertices
* E = Number of Edges

---

## 🖼️ Project Screenshots

### Project Structure

![Project Structure](images/image1.png)

### Graph Dataset

![Graph Dataset](images/image2.png)

### BFS Traversal Output

![BFS Output](images/image3.png)

### DFS Traversal Output

![DFS Output](images/image4.png)

### Shortest Path Output

![Shortest Path](images/image5.png)

### Route Report

![Route Report](images/image6.png)

### Graph Visualization

![Graph Visualization](images/image7.png)

---

## 🌍 Real-World Applications

* Google Maps Navigation
* Uber Route Optimization
* Ola Ride Matching
* Swiggy Delivery Routing
* Zomato Delivery Planning
* Logistics and Supply Chain Networks
* Transportation Systems
* Smart City Navigation
* Emergency Route Planning
* Fleet Management Systems

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Graph Data Structures
* Graph Traversal Algorithms
* Shortest Path Algorithms
* Priority Queue Implementation
* Complexity Analysis
* Path Optimization Techniques
* File Handling
* Data Visualization
* Modular Software Design
* Real-World DSA Applications

---

## 💡 Future Enhancements

* A* Search Algorithm
* Traffic Simulation
* Toll Cost Optimization
* Multi-Criteria Route Selection
* Real Map Integration
* Web-Based Dashboard
* FastAPI Backend
* Interactive Route Visualization
* Live Route Updates

---

## 👨‍💻 Author

Developed as a Data Structures and Algorithms Project to demonstrate practical applications of Graph Theory, BFS, DFS, Dijkstra's Algorithm, Priority Queues, and Route Optimization techniques used in modern navigation and logistics systems.

If you found this project useful, consider giving it a ⭐ on GitHub.
