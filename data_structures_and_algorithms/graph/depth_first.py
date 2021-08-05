def depth_first(graph, source, path=[]):

    if source not in path:

        path.append(source)

        if source not in graph:
            return path

        for neighbor in graph[source]:

            path = depth_first(graph, neighbor, path)

    return path


