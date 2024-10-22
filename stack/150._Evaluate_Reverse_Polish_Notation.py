class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                match token:
                    case '+':
                        stack.append(operand1 + operand2)
                    case '-':
                        stack.append(operand1 - operand2)
                    case '*':
                        stack.append(operand1 * operand2)
                    case '/':
                        stack.append(int(operand1 / operand2))

        return stack[-1]
