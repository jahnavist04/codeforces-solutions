/*
 * Problem : Way Too Long Words
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: Python 3
 * Date: 7/14/2026, 12:39:43 PM
 * Link: https://codeforces.com/contest/71/problem/A
 */

n = int(input())

for _ in range(n):
    word = input()

    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word) - 2) + word[-1])
