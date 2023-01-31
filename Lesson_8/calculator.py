def copy_expression(expression: list) -> list:
    origin_expression = expression.copy()
    return origin_expression


def list_expression(expression: str) -> list:
    expression = expression.replace(' ', ''). \
        replace('+', ' + '). \
        replace('*', ' * '). \
        replace('/', ' / ')
    if expression.startswith('-'):
        expression = expression.replace('-', ' - ')
        expression = ('-' + expression[3:]).split()
    else:
        expression = expression.replace('-', ' - ').split()
    return expression


class Calculator:
    operation = {
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
    }

    def calculate(self, expression: list, operator_1, operator_2):
        i = 0
        while operator_1 in expression or operator_2 in expression:
            if expression[i] in [operator_1, operator_2]:
                expression[i - 1] = self.operation.get(expression[i])(int(expression[i - 1]), int(expression[i + 1]))
                del expression[i]
                del expression[i]
            else:
                i += 1
        return expression