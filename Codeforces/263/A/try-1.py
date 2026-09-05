/*
 * Problem : Beautiful Matrix
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: Python 3
 * Date: 9/5/2026, 7:47:48 PM
 * Link: https://codeforces.com/contest/263/problem/A
 */

row = col = 0

for i in range(1, 6):
    nums = list(map(int, input().split()))

    for j in range(1, 6):
        if nums[j - 1] == 1:
            row = i
            col = j

moves = abs(row - 3) + abs(col - 3)

print(moves)
