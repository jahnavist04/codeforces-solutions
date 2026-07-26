/*
 * Problem : Bit++
 * Difficulty: Easy
 * Submission: Try 2
 * status: Accepted
 * Language: Python 3
 * Date: 7/26/2026, 7:43:24 PM
 * Link: https://codeforces.com/contest/282/problem/A
 */

n = int(input())

x = 0

for _ in range(n):
    statement = input()
    if "++" in statement:
        x += 1
    else:
        x -= 1

print(x)
