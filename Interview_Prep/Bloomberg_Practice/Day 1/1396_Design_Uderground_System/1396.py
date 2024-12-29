class UndergroundSystem:

    def __init__(self):
        self.checkedIn = {}  # id -> (startStation, time)
        self.totalMap = {}  # (start, end) -> [totalTime, count]

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkedIn[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        start, time = self.checkedIn[id]
        route = (start, endStation)

        if route not in self.totalMap:
            self.totalMap[route] = [0, 0]
        self.totalMap[(start, endStation)][0] += t - time
        self.totalMap[(start, endStation)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total / count
