
import calculator
import view


def start():
    calc = calculator.Calculator()
    expression = view.get_expression()
    le = calculator.list_expression(expression)
    le_copy = calculator.copy_expression(le)
    while len(le) > 1:
        calc.calculate(le, '/', '*')
        calc.calculate(le, '-', '+')
    view.print_result(le_copy, le)