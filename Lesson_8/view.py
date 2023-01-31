def get_expression():
    expression = input('Введите арифметическое выражение, используя числа и знаки + - * /: ')
    return expression


def print_result(origin_expression, result):
    print(f'{" ".join(origin_expression)} = {result[0]}')