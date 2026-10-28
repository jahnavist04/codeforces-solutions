/*
 * Problem #2144: Minimum Cost of Buying Candies With Discount
 * Difficulty: Easy
 * Submission: Try 1
 * status: Accepted
 * Language: python
 * Date: 10/28/2026, 8:25:35 PM
 * Link: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
 */

class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        total = 0

        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total += cost[i]

        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
