def max_cyclic_sum(s):
    s = s * 2
    n = len(s) // 2
    ans = 0
    for i in range(n):
        seen = set()
        curr = 0
        for j in range(i, i + n):
            if s[j] in seen:
                break
            seen.add(s[j])
            curr += ord(s[j]) - 96
        ans = max(ans, curr)
    return ans

s = input().strip()
print(max_cyclic_sum(s))

