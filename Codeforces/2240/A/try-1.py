/*
 * Problem : Another Popcount Problem
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: Python 3
 * Date: 7/6/2026, 7:01:58 PM
 * Link: https://codeforces.com/contest/2240/problem/A
 */

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    ans = 0

    for i in range(31):
        cost = 1 << i
        take = min(n // cost, k)
        ans += take
        n -= take * cost

    print(ans)
