from typing import List


class Solution:
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        output = []
        visited, cycle = set(), set()

        # ? Build an adjacency list
        for crs, pre in prereqs:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
