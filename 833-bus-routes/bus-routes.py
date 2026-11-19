
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_bus=defaultdict(list)
        for i , stop in enumerate(routes):
            for s in stop:
                stop_to_bus[s].append(i)
        queue=deque([(source,0)])
        visited_stop=set([source])
        visited_bus=set()
        while queue:
            stop,bus=queue.popleft()
            for i in stop_to_bus[stop]:
                if i in visited_bus:
                    continue
                visited_bus.add(i)
                for j in routes[i]:
                    if j == target:
                        return bus+1
                    if j not in visited_stop:
                        visited_stop.add(j)
                        queue.append((j,bus+1))
        return -1
