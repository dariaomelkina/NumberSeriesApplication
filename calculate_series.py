from stack import Stack
from sympy import *
from funcs import add, subtract, multiply, divide, floor_divide, modulus, exponent
from sympy.parsing.sympy_parser import parse_expr

operators = {'+': (1, add), '-': (1, subtract), '*': (2, multiply), '/': (2, divide),
             '//': (2, floor_divide), '%': (2, modulus), '**': (3, exponent)}
operands = '1234567890n.'


def find_alpha(lst):
    """
    Return alpha part
    from the harmonic series.

    :param lst: list with alpha.
    :return: string alpha.
    """
    if '(' in lst:
        return ''.join(lst[1:-1])
    else:
        return ''.join(lst)


def partial(expression, to):
    """
    Return partial sum
    using sympy library.

    :param expression: series.
    :param to: number of iterations.
    :return: sum.
    """
    summ = 0
    n = symbols('n')
    expr = parse_expr(expression)
    for i in range(1, to + 1):
        summ += expr.subs(n, i)
    return summ


def prepare_expression(expression):
    """
    Prepares expression for converting into prefix.
    Adds needed spaces between operands and operators.

    :param expression: expression, that needs to be changed.
    :return: prepared expression.
    """
    lst = []
    element = ''

    for i in expression:
        if i == '(' or i == ')':
            lst.append(element)
            element = ' '
            lst.append(i)
        elif i in operands and (element == '' or element[-1] in operands):
            element += i
        elif i in operands and element[-1] not in operands:
            lst.append(element)
            element = i
        elif i in operators and element[-1] in operators:
            element += i
        elif i in operators and element[-1] not in operators:
            lst.append(element)
            element = i

    if element:
        lst.append(element)
    return ' '.join(lst)


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
    Returns value of the expression.

    :param infix: expression in the infix notation.
    :param n: variable n.
    :return: value of the expression.
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


def series_partial_sum(series, n):
    """
    Returns partial sum of the series.

    :return: sum.
    """
    lst = prepare_expression(series).split()
    check_lst = []
    for i in lst:
        if not (i in list(operators) or i in list(operands)):
            check_lst.append(i)
    if not check_lst:
        partial_sum = 0
        for i in range(1, n + 1):
            partial_sum += evaluate(series, i)
        return partial_sum
    else:
        return partial(series, n)


def check_limit(expression, to, param=None):
    """
    Return limit of the expression.
    With 'c' or 'd' parameters finds
    limits for Cauchy's and d'Alembert's
    rules respectively.

    :param expression: series.
    :param to: approached value.
    :param param: Cauchy/d'Alembert
    :return: limit.
    """
    n = symbols('n')
    prepared_expression = prepare_expression(expression)
    if param == 'c':
        cauchy = parse_expr(prepared_expression) ** (1 / n)
        return limit(cauchy, n, to)
    elif param == 'd':
        dalember_plus_one = prepared_expression.replace('n', '( n + 1 )')
        DAlembert = parse_expr(dalember_plus_one) / parse_expr(prepared_expression)
        return limit(DAlembert, n, to)
    else:
        return limit(parse_expr(prepared_expression), n, to)


def convergence(expression):
    """
    Return True if series
    are convergence.
    Returned string 'error'
    indicates, that these tests
    were not enough.

    :param expression: series.
    :return: bool/string.
    """
    # check harmonic series
    lst = prepare_expression(expression).split()
    if ['1', '/', 'n'] == lst:
        return False
    if ['1', '/', 'n', '**'] == lst[:4] and 'n' not in lst[4:]:
        alpha = find_alpha(lst[4:])
        if float(alpha) > 1:
            return True
        else:
            return False

    # check needed condition of limit
    if check_limit(expression, float('inf')) != 0:
        return False

    # check Cauchy test
    if check_limit(expression, float('inf'), 'c') < 1:
        return True
    elif check_limit(expression, float('inf'), 'c') > 1:
        return False

    # check d'Alembert test
    if check_limit(expression, float('inf'), 'd') < 1:
        return True
    elif check_limit(expression, float('inf'), 'd') > 1:
        return False

    return 'error'


print(convergence('1/n**5'))
print(convergence('n**2 /n'))
print(convergence('(n**2 + n -1)/4**n'))
print(convergence('((7*n + 1)/(6*n + 5))**(3*n + 2)'))
print(series_partial_sum('sin(n/10*pi)', 10))
