class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visited = set()
        for crs, pre in prereqs:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True

            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
