from collections import deque


def get_component(graph: dict, start_vertex) -> set:
    '''
    :param graph: dict
    :param start_vertex: immutable types
    :return: set
    '''

    component = {start_vertex}
    queue = deque(start_vertex)

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor in component:
                continue
            component.add(neighbor)
            queue.append(neighbor)

    return component
