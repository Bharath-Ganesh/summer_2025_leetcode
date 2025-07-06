# User function Template for python3

class Solution:


    def cutRodRecursion(self, price):
        # code here
        n = len(price)
        dp = {}
        def backttracking(index, remaining_length):
            # No more rod length left
            if index == 0:
                return remaining_length * price[0]

            key = index, remaining_length
            if key in dp:
                return dp[key]
            # pick or not pick
            # Here you have a rod length of N
            # Lets suppose you're at the index = 2, which means a rod of length 3 (index + 1)
            # You can take it or not take it
            #[1, 5, 8, 9]
            not_pick = backttracking(index - 1, remaining_length)
            pick = float('-inf')
            rod_length = index + 1
            if rod_length <= remaining_length:
                pick = price[index] + backttracking(index , remaining_length - rod_length)
            dp[key] = max(pick, not_pick)
            return dp[key]

        return backttracking(n - 1, n)

    def cutRod(self, price):
        # code here
        n = len(price)
        dp = [0] * (n + 1)

        for i in range(0, n + 1 ):
            for j in range(1, i + 1):
                dp[i] = max(price[j - 1] + dp[i - j], dp[i])
        return dp[n]


if __name__ == '__main__':
    print(Solution().cutRodRecursion([1, 5, 8, 9, 10, 17, 17, 20]))