class Solution:
    def GiaTri(self, bt):
        def precedence(op):
            if op == '+' or op == '-':
                return 1
            if op == '*' or op == '/':
                return 2
            return 0
        
        def apply_op(a, b, op):
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            if op == '/':
                return a // b

        values = []
        operators = []

        i = 0
        while i < len(bt):
            if bt[i].isdigit():
                val = 0
                while i < len(bt) and bt[i].isdigit():
                    val = val * 10 + int(bt[i])
                    i += 1
                values.append(val)
                i -= 1
            elif bt[i] == '(':
                operators.append(bt[i])
            elif bt[i] == ')':
                while operators and operators[-1] != '(':
                    op = operators.pop()
                    b = values.pop()
                    a = values.pop()
                    values.append(apply_op(a, b, op))
                operators.pop()
            else:
                while operators and precedence(operators[-1]) >= precedence(bt[i]):
                    op = operators.pop()
                    b = values.pop()
                    a = values.pop()
                    values.append(apply_op(a, b, op))
                operators.append(bt[i])
            i += 1

        while operators:
            op = operators.pop()
            b = values.pop()
            a = values.pop()
            values.append(apply_op(a, b, op))

        return values[-1]

# Kiểm tra kết quả
bt = "3 + 4 * 2 / (1 - 5)^2"
solution = Solution()
print("Giá trị của biểu thức", bt, "là:", solution.GiaTri(bt))
