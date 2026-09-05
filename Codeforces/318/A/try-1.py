/*
 * Problem : Even Odds
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: Python 3
 * Date: 9/5/2026, 7:46:53 PM
 * Link: https://codeforces.com/contest/318/problem/A
 */

n, k = map(int, input().split())

odd_count = (n + 1) // 2

if k <= odd_count:
    answer = 2 * k - 1
else:
    answer = 2 * (k - odd_count)

print(answer)
