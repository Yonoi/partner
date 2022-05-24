from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        records = defaultdict(str)
        modulo = 2 * (numRows - 1)
        for i, ch in enumerate(s):
            row_idx = i % modulo if (i // (numRows - 1)) % 2 == 0 else -i % modulo
            records[i % modulo] += ch
        
        return ''.join(records.values())