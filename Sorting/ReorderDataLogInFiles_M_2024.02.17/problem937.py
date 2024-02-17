from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = [x for x in logs if x.split(" ")[1].isalpha()]
        letter_logs.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0:]))
        digi_logs = [x for x in logs if x.split(" ")[1].isdigit()]
        return letter_logs + digi_logs
