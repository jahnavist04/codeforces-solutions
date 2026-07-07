/*
 * Problem : Village Guilds
 * Difficulty: Medium
 * Submission: Try 1
 * status: Accepted
 * Language: Python 3
 * Date: 7/7/2026, 7:47:59 PM
 * Link: https://codeforces.com/contest/2238/problem/C
 */

import sys

sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def dfs(v, p):
    global ans, dp, depth, g

    ans[v] = 0
    dp[v] = depth[v]

    m1 = depth[v]
    m2 = depth[v]

    for u in g[v]:
        if u != p:
            depth[u] = depth[v] + 1
            dfs(u, v)

            dp[v] = max(dp[v], dp[u])
            ans[v] += ans[u]

            if dp[u] >= m1:
                m2 = m1
                m1 = dp[u]
            elif dp[u] >= m2:
                m2 = dp[u]

    ans[v] += m2 - depth[v] + 1


t = int(input())

for _ in range(t):
    n = int(input())

    g = [[] for _ in range(n)]
    depth = [0] * n
    dp = [0] * n
    ans = [0] * n

    if n > 1:
        parents = list(map(int, input().split()))
        for i, p in enumerate(parents, start=1):
            g[p - 1].append(i)

    dfs(0, -1)
    print(ans[0])
