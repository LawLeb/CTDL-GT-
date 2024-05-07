class Solution:
    def HauTo(self, bt):
        def precedence(op):
            if op == '+' or op == '-':
                return 1
            if op == '*' or op == '/':
                return 2
            return 0

        output = []
        operators = []

        i = 0
        while i < len(bt):
            if bt[i].isdigit():
                num = ''
                while i < len(bt) and (bt[i].isdigit() or bt[i] == '.'):
                    num += bt[i]
                    i += 1
                output.append(num)
                continue
            elif bt[i] == '(':
                operators.append('(')
            elif bt[i] == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()
            else:
                while operators and precedence(operators[-1]) >= precedence(bt[i]):
                    output.append(operators.pop())
                operators.append(bt[i])
            i += 1

        while operators:
            output.append(operators.pop())

        return ' '.join(output)

# Test
solution = Solution()
print(solution.HauTo('2 + 3 * 5'))  # Output: '2 3 5 * +'
