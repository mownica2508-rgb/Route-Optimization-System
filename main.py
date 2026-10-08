from src.graph import Graph
from src.bfs import bfs
from src.dfs import dfs
from src.dijkstra import dijkstra
from src.report import generate_report, save_report
from src.visualization import visualize_graph


graph = Graph()
graph.load_graph("data/city_graph.json")


while True:

    print("\n" + "=" * 50)
    print("INTELLIGENT ROUTE PLANNER")
    print("=" * 50)

    print("1. Display Graph")
    print("2. BFS Traversal")
    print("3. DFS Traversal")
    print("4. Find Shortest Route")
    print("5. Generate Route Report")
    print("6. Visualize Graph")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        graph.display_graph()

    elif choice == "2":

        start = input("Enter Starting Location: ")

        if start not in graph.graph:
            print("\nInvalid Location!")
            continue

        result = bfs(graph, start)

        print("\nBFS Traversal:")
        print(" -> ".join(result))

    elif choice == "3":

        start = input("Enter Starting Location: ")

        if start not in graph.graph:
            print("\nInvalid Location!")
            continue

        result = dfs(graph, start)

        print("\nDFS Traversal:")
        print(" -> ".join(result))

    elif choice == "4":

        source = input("Enter Source: ")
        destination = input("Enter Destination: ")

        path, distance = dijkstra(
            graph,
            source,
            destination
        )

        if path:
            print("\nShortest Route:")
            print(" -> ".join(path))
            print(f"\nTotal Distance: {distance} km")
        else:
            print("\nNo valid route found.")

    elif choice == "5":

        source = input("Enter Source: ")
        destination = input("Enter Destination: ")

        path, distance = dijkstra(
            graph,
            source,
            destination
        )

        if path:

            report = generate_report(
                source,
                destination,
                path,
                distance
            )

            print(report)

            save_report(report)

            print("\nReport Saved Successfully!")
            print("Saved to outputs/route_report.txt")

        else:
            print("\nNo valid route found.")

    elif choice == "6":

        source = input("Enter Source: ")
        destination = input("Enter Destination: ")

        path, distance = dijkstra(
            graph,
            source,
            destination
        )

        if path:

            visualize_graph(
                graph,
                path
            )

            print(
                "\nGraph visualization saved as "
                "outputs/graph_visualization.png"
            )

        else:
            print("\nNo valid route found.")

    elif choice == "7":

        print("\nThank You For Using Route Planner!")
        break

    else:

        print("\nInvalid Choice! Please try again.")