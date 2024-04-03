<img src="https://github.com/Dynamo-Dream/A_Star_ALgo/blob/main/visual.png" alt="Example Image" width="500" height="500">

## Summary of A* Search Algorithm

The A* search algorithm is a widely-used pathfinding algorithm in computer science and artificial intelligence. It is an extension of Dijkstra's algorithm with a heuristic added to improve efficiency. A* is particularly useful in scenarios where finding the shortest path from a starting point to a goal is required, such as in route planning or game AI.

At its core, A* search evaluates nodes in a graph based on two factors: the cost to reach the node from the start node (g-score) and an estimate of the cost to reach the goal from that node (h-score). The algorithm selects nodes to explore based on a combination of these scores, typically using a priority queue to prioritize nodes with lower total scores.

A* guarantees to find the shortest path if certain conditions are met, namely that the heuristic function used (h-score) must be admissible (never overestimates the true cost to reach the goal) and consistent (satisfies the triangle inequality).

## Visualization of A* Search in Pygame

In this GitHub repository, I've implemented the A* search algorithm and provided a visualization using the Pygame library. The implementation allows users to interactively see how the algorithm traverses through a grid from a start point to a goal point.

Here's a brief overview of the visualization:
- **Grid Representation**: The grid represents the environment in which the algorithm operates. Each cell can be either empty, representing traversable terrain, or blocked, representing obstacles that cannot be traversed.
- **Interactive Start and Goal Selection**: Users can select the starting and goal positions by clicking on the grid.
- **A* Algorithm Execution**: Upon selecting the start and goal positions, the A* algorithm is executed to find the shortest path between them. During execution, the algorithm visually highlights the explored nodes, the path found, and any obstacles encountered.
- **Real-time Visualization**: The visualization is updated in real-time as the algorithm progresses, allowing users to see the search process step by step.
- **Pygame Window**: The visualization is displayed in a Pygame window, providing a user-friendly interface for interaction.

This implementation not only serves as a demonstration of the A* search algorithm but also provides a valuable tool for understanding its behavior and performance in different scenarios. Users can experiment with different grid layouts, obstacle configurations, and heuristic functions to gain insights into how these factors affect the algorithm's efficiency and the resulting path.
#### The Motivation and Help was taken from Youtube Video A* Pathfinding Visualization of Channel Tech With Tim


