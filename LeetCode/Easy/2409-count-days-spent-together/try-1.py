/*
 * Problem #2409: Count Days Spent Together
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 10/24/2026, 3:32:23 PM
 * Link: https://leetcode.com/problems/count-days-spent-together/
 */

class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        def to_days(date):
            month, day = map(int, date.split('-'))
            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return sum(days[:month - 1]) + day

        start = max(to_days(arriveAlice), to_days(arriveBob))
        end = min(to_days(leaveAlice), to_days(leaveBob))

        return max(0, end - start + 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
