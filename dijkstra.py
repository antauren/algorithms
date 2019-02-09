from collections import deque


def get_min_weight(weighted_graph, vertex_1, vertex_2):
    ''' Dijkstra's algorithm '''

    min_weight_dict = dict.fromkeys(weighted_graph.keys(), float('inf'))
    min_weight_dict[vertex_1] = 0
    queue = deque(vertex_1)

    while queue:
        current = queue.popleft()
        for neighbor in weighted_graph[current]:
            offering_min_weight = min_weight_dict[current] + weighted_graph[current][neighbor]

            if offering_min_weight >= min_weight_dict[neighbor]:
                continue
            min_weight_dict[neighbor] = offering_min_weight
            queue.append(neighbor)

    return min_weight_dict[vertex_2]
