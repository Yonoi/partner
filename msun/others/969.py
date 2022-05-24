class Solution:
    def pancakeSort(self, arr: list) -> list:
        ans = []
        for n in range(len(arr), 1, -1):
            index = arr.index(max(arr[0:n]))

            if index == n - 1:
                continue
            m = index
            for i in range((m + 1) // 2):
                arr[i], arr[m - i] = arr[m - i], arr[i]
            
            for i in range(n // 2):
                arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

            ans.append(index + 1)
            ans.append(n)

        return ans


if __name__ == "__main__":
    s = Solution()
    arr = [3, 2, 4, 1]
    print(s.pancakeSort(arr))