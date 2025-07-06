from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            a = length
            b = len(words[i])
            c = len(line)
            if a + b+ c > maxWidth:
                # Line complete
                extra_space = maxWidth - length
                spaces = extra_space // max(1, len(line) - 1)
                remainder = extra_space % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))
                line, length = [], 0  # Reset line and length
                continue

            line.append(words[i])
            length += len(words[i])
            i += 1

        # Handling last line (left-justified)
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        last_line += " " * trail_space
        res.append(last_line)

        return res

if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    sol = Solution()
    sol.fullJustify(words, maxWidth)