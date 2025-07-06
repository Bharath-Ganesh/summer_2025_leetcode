class Solution:
    def simplifyPath(self, paths: str) -> str:
        """
        "../../../"
        [".", ".", "/"]
        "/home//foo/"
        ["/", "home", "/", "/", "foo", "/"]
        ["/", "home", "/", "foo", "/"]
        """
        stack = []
        idx = 0
        while idx < len(paths):
            path = paths[idx]
            if path.isalpha():
                temp = []
                while idx < len(paths) and paths[idx].isalpha():
                    temp.append(paths[idx])
                    idx += 1
                last_char = ""
                stack.append(''.join(temp))
                while stack and stack[-1] == '/':
                    last_char = stack.pop()
                if last_char == "/":
                    stack.append("/")
                idx -= 1
            elif path == "/":
                stack.append(path)
            elif path == ".":
                if not stack:
                    stack.append(path)
                elif stack and idx + 1 < len(paths) and paths[idx + 1] == ".":
                    stack.pop()
                    stack.pop()
                    stack.pop()
            idx += 1
        if stack  and stack[-1] == "/":
            stack.pop()
        return ''.join(list(stack))

if __name__ == '__main__':
    sol = Solution()
    print(sol.simplifyPath("/home/user/Documents/../Pictures"))