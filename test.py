# 小于n的最大数
# 考点：--
# 412 人用过
# 我用过 1 次
# 给定一个数 n，如 23121；给定一组数字 A 如 {2,4,9}，求由 A 中元素组成的、小于 n 的最大数，如小于 23121 的最大数为 22999。​​​
# 参考答案
# 大体思路是，从最高位向最低位构造目标数，用 A 中尽量大的元素（但要小于等于 n 的相应位数字）。一旦目标数中有一位数字小于 n 相应位的数字，剩余低位可用 A 中最大元素填充。​

# 注意： ​

# 1. 可能构造出等于 n 的数，需判断后重新构造；​
# 2. 若 A 中没有小于等于 n 最高位数字的元素，则可直接用 A 中最大元素填充低位；​
# 3. 有无解情形。​

# ## 一些边界情况：​

# n A 结果​
# 23333 {2,3} 3333​
# 23333 {3} 3333​
# 22222 {2} 2222​
# 22222 {2,3} 3333​
# 2 {2} 无解​

n = 23121
A = [2, 3, 1, 0]

ans = []
n_lst = list(map(int, list(str(n))))
n_len = len(n_lst)
A.sort()

for i in range(n_len):
    j = 0
    while j < len(A):
        if A[j] >= n_lst[i]:
            break
        j += 1
    if A[j] == n_lst[i]:
        ans.append(A[j])
    else:
        ans.append(A[j-1])
        k = i
        while k < n_len - 1:
            ans.append(A[-1])
            k += 1
        break
ans = int(''.join(list(map(str, ans))))
if ans == n:
    pass
print(ans)