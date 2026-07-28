/*
 * Problem : Next Round
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: Python 3
 * Date: 7/28/2026, 7:12:40 PM
 * Link: https://codeforces.com/contest/158/problem/A
 */

n, k = map(int, input().split())
scores = list(map(int, input().split()))

cutoff = scores[k - 1]

count = 0
for score in scores:
    if score >= cutoff and score > 0:
        count += 1

print(count)
