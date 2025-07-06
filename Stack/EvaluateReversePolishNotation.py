import re
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        """
            ["4","13","5","/","+"]

        """
        # If there are any expressions other than the digits or +, /, -
        operator_stack = []
        for token in tokens:
            # inside your tokenizer/parse loop:
            if re.fullmatch(r'[+-]?\d+', token):
                # token is one or more digits, with an optional leading + or –
                operator_stack.append(int(token))
            else:
                evaluated_value = self.evaluate(token, operator_stack)
                if evaluated_value == float('inf'):
                    continue
                operator_stack.append(evaluated_value)

        return operator_stack[0]

    def evaluate(self, token, operator_stack):
        if len(operator_stack) < 2:
            return float('inf')

        second_value = operator_stack.pop()
        first_value = operator_stack.pop()
        if token == '+':
            return first_value + second_value
        elif token == '-':
            return first_value - second_value
        elif token == '*':
            return first_value * second_value
        elif token == '/':
            return int(first_value / second_value)
        else:
            return float('inf')


if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN(["4", "13", "-5", "/", "+"]))
