import heapq

def dijkstra(graph, start):
    # 初始化距離表
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    # 優先隊列，用於選擇當前距離最小的節點
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # 如果取出的距離大於已知最短距離，則跳過
        if current_distance > distances[current_vertex]:
            continue

        # 檢查所有鄰居
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # 如果找到更短的路徑，更新距離表並加入優先隊列
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 示例圖結構 (用鄰接表表示)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 從節點 'A' 開始進行 Dijkstra 演算法
distances = dijkstra(graph, 'A')
print(distances)
