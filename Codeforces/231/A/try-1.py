/*
 * Problem : Team
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: Python 3
 * Date: 7/27/2026, 7:37:35 PM
 * Link: https://codeforces.com/contest/231/problem/A
 */

n = int(input())

count = 0

for _ in range(n):
    p, v, t = map(int, input().split())
    if p + v + t >= 2:
        count += 1

print(count)
