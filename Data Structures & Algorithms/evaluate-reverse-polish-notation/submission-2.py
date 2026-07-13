class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            try:
                n = int(t)
                stack.append(n)
            except ValueError:
                n2 = stack.pop()
                n1 = stack.pop()

                match t:
                    case '+':
                        stack.append(n1 + n2)
                        print(n1, '+', n2, '=', n1 + n2)
                    case '-':
                        stack.append(n1 - n2)
                        print(n1, '-', n2, '=', n1 - n2)
                    case '*':
                        stack.append(n1 * n2)
                        print(n1, '*', n2, '=', n1 * n2)
                    case '/':
                        stack.append(int(n1 / n2))
                        print(n1, '/', n2, '=', n1 / n2)
        
        return stack.pop()