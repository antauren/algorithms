def get_component(graph: dict, start_vertex) -> set:
    '''
    :param graph: dict
    :param start_vertex: immutable types
    :return: set
    '''

    component = {start_vertex}
    queue = [start_vertex]

    while queue:
        current = queue.pop(0)

        for neighbor in graph[current]:
            if neighbor in component:
                continue
            component.add(neighbor)
            queue.append(neighbor)

    return component
