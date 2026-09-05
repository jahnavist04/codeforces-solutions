/*
 * Problem : Theatre Square
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: Python 3
 * Date: 8/6/2026, 7:41:07 PM
 * Link: https://codeforces.com/contest/1/problem/A
 */

n, m, a = map(int, input().split())

rows = (n + a - 1) // a
cols = (m + a - 1) // a

print(rows * cols)
