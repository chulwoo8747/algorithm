def bt():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, n + 1):
        if i not in ans:
            ans.append(i)
            bt()
            ans.pop()


ans = []
n, m = map(int, input().split())
bt()