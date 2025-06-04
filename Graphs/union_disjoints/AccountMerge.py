from collections import defaultdict
from typing import List


class DisjointSet:

    def __init__(self, n):
        self.size = [1] * n
        self.parent = []
        for i in range(n):
            self.parent.append(i)

    def unionBySize(self, node1, node2):
        pu = self.findUltimateParent(node1)
        pv = self.findUltimateParent(node2)
        if pu == pv:
            return
        if self.size[pu] > self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv

    def findUltimateParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUltimateParent(self.parent[node])  # path compression
        return self.parent[node]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
            [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        """
        account_lookup = defaultdict(int)
        rows = len(accounts)

        ds = DisjointSet(rows)
        for i in range(rows):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail not in account_lookup:
                    account_lookup[mail] = i
                else:
                    ds.unionBySize(i, account_lookup[mail])

        temp = defaultdict(list)
        for key, val in account_lookup.items():
            ult_parent = ds.findUltimateParent(val)
            temp[ult_parent].append(key)

        # Step 3: Build result with names
        res = []
        for index, emails in temp.items():
            name = accounts[index][0]
            res.append([name] + sorted(emails))
        return res






if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]
    s = Solution()
    ans = s.accountsMerge(accounts)
    print(ans)












