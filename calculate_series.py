from stack import Stack
from sympy import *
from funcs import add, subtract, multiply, divide, floor_divide, modulus, exponent

operators = {'+': (1, add), '-': (1, subtract), '*': (2, multiply), '/': (2, divide),
             '//': (2, floor_divide), '%': (2, modulus), '**': (3, exponent)}
operands = '1234567890n'


def infix_to_postfix(infix):
    """
    Convert infix expression to a
    postfix expression.

    :param infix: expression to convert.
    :return: converted expression.
    """
    postfix = ''
    stack = Stack()
    infix = infix.split()
    for i in infix:
        if i in operands:
            postfix += i + ' '
        elif i == '(':
            stack.push(i)
        elif i in operators:
            lst = []
            while not stack.empty():
                lst.append(stack.pop())
            new_lst = []
            value = operators[i][0]
            for element in lst:
                if element != '(':
                    if operators[element][0] >= value:
                        postfix += element + ' '
                    else:
                        new_lst.append(element)
                else:
                    new_lst.append(element)
            for element in new_lst[::-1]:
                stack.push(element)
            stack.push(i)
        elif i == ')':
            item = stack.pop()
            while item != '(':
                postfix += item + ' '
                item = stack.pop()

    while not stack.empty():
        postfix += stack.pop() + ' '

    return postfix


def evaluate(infix, n):
    """

    """
    postfix = infix_to_postfix(infix)
    stack = Stack()
    postfix = postfix.split()
    for i in postfix:
        token = i
        if token == 'n':
            stack.push(n)
        elif token in operands:
            stack.push(token)
        else:
            x, y = [stack.pop(), stack.pop()][::-1]
            lst = []
            while not stack.empty():
                lst.append(stack.pop())
            stack.push(operators[token][1](int(x), int(y)))
            for x in lst[::-1]:
                stack.push(x)
    return stack.pop()


def series_partial_sum():
    """
    Returns partial sum of the series.

    :return: sum.
    """
    line = input()
    n = int(input())
    partial_sum = 0
    for i in range(1, n + 1):
        partial_sum += evaluate(line, i)
    print(partial_sum)
    return partial_sum


def check_limit(expression, to, param=None):
    """
    Return limit of the expression.
    With 'c' or 'd' parameters finds
    limits for Cauchy's and d'Alembert's
    rules respectively.

    :param expression:
    :param to:
    :param param:
    :return:
    """
    n = symbols('n')
    prepared_expression =
    if param == 'c':
        pass
    if param == 'd':
        pass
    return limit(prepared_expression, x, to)


def convergence(expression):
    # check needed condition
    if check_limit(expression, float('inf')) != 0:
        return False

    # check harmony rule
    if '1 / n ** ' in expression:
        alpha = expression[8:]
        if int(alpha) > 1:
            return True

    # check Cauchy rule
    if check_limit(expression, float('inf'), 'c') < 1:
        return True
    elif check_limit(expression, float('inf'), 'c') > 1:
        return False

    # check d'Alembert rule
    if check_limit(expression, float('inf'), 'd') < 1:
        return True
    elif check_limit(expression, float('inf'), 'd') > 1:
        return False

    # Cauchy = prepare_expression(expression, 'c')
    # Cauchy = expression ** (1/x)
    # if check_limit(Cauchy, float('inf')) < 1:
    #     return True
    # elif check_limit(Cauchy, float('inf')) > 1:
    #     return False

    # DAlembert = prepare_expression(expression, 'd')
    # DAlembert = abs(expression(n + 1) / expression)
    # if check_limit(Cauchy, float('inf')) < 1:
    #     return True
    # elif check_limit(Cauchy, float('inf')) > 1:
    #     return False

    return 'error'


# if __name__ == '__main__':
#     series_partial_sum()

x = symbols('x')
func = 1/x
# func /= x * 2
print(limit(func, x, float('inf')) == 0.5)
