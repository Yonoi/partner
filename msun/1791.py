from collections import defaultdict
class Solution:
    def findCenter(self, edges: list) -> int:
        degree = defaultdict(int)
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        
        for key, values in degree.items():
            if values == len(edges):
                return key

if __name__ == '__main__':
    s = Solution()
    # edges = [[1,2],[2,3],[4,2]]
    edges = [[1,2],[5,1],[1,3],[1,4]]
    print(s.findCenter(edges))
