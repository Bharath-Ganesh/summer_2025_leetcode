from collections import Counter, defaultdict

from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        match_freq_count, left, n = 0, 0, len(s2)
        desired_freq = len(s1)
        look_up_s1 = Counter(s1)
        look_up_s2 = defaultdict(int)

        for right, ch in enumerate(s2):

            look_up_s2[ch] += 1

            if ch in look_up_s1 and look_up_s1[ch] >= look_up_s2[ch]:
                match_freq_count += 1

            if match_freq_count == desired_freq:
                return True

            if right + 1 >= len(s1):
                ch_to_be_removed = s2[left]
                if ch_to_be_removed in look_up_s1 and look_up_s1[ch_to_be_removed] >= look_up_s2[ch_to_be_removed]:
                    match_freq_count -= 1

                look_up_s2[ch_to_be_removed] -= 1
                freq = look_up_s2[ch_to_be_removed]
                if freq == 0:
                    del look_up_s2[ch_to_be_removed]
                left += 1

        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkInclusion(s1="ab", s2="eidboaoo"))

if __name__ == '__main__':
    sol = Solution()
    print(sol.checkInclusion(s1 = "ab", s2 = "eidboaoo"))