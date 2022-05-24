from typing import List
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row = 1
        last_row = 0

        for ch in s:
            width = widths[ord(ch) - 97]
            if last_row + width > 100:
                last_row = width
                row += 1
            else:
                last_row += width
        return [row, last_row]