class Solution:
    def decodeString(self, s: str) -> str:
        curr = ""
        stack = []
        for word in s:
            if word == '[':
                if curr.isdigit():
                    stack.append(int(curr))
                else:
                    stack.append(curr)
                stack.append(word)
                curr = ""
            elif word == ']':
                new_word = []
                while stack and stack[-1] != '[':
                    new_word.append(stack.pop())
                new_word.reverse()
                if stack:
                    stack.pop()
                new_word = ''.join(new_word * stack.pop())
                stack.append(new_word)
                curr = ""
            elif word.isalpha():
                stack.append(word)
            else:
                curr += word
        return ''.join(list(stack))

if __name__ == '__main__':
    sol = Solution()
    ans = sol.decodeString("3[a]2[bc]")
    print(ans)