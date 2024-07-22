
def bfs(graph, start):
    """
    使用廣度優先搜索從起點開始遍歷圖。

    :param graph: 圖結構，用鄰接表表示，例如 {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], ...}
    :param start: 起始節點
    :return: 返回從起始節點可以訪問的所有節點
    """
    visited = set()  # 用於記錄已訪問的節點
    queue = [start]  # 用 list 作為 BFS 的隊列

    while queue:
        vertex = queue.pop(0)  # 從隊列左側取出節點
        if vertex not in visited:
            print(vertex)  # 處理當前節點，這裡用 print 打印出來
            visited.add(vertex)  # 標記為已訪問
            # 將所有未訪問的鄰居加入隊列
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# 示例圖結構 (用鄰接表表示)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 從節點 'A' 開始進行廣度優先搜索
bfs(graph, 'A')
