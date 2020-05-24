from stack import Stack


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def floor_divide(x, y):
    return x // y


def modulus(x, y):
    return x % y


def exponent(x, y):
    return x ** y


operators = {'+': (1, add), '-': (1, subtract), '*': (2, multiply), '/': (2, divide),
             '//': (2, floor_divide), '%': (2, modulus), '**': (3, exponent)}
operands = '1234567890n'


def infix_to_postfix(infix):
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


def series():
    line = input()
    n = int(input())
    summ = 0
    for i in range(1, n + 1):
        summ += evaluate(line, i)
    print(summ)
    return summ


if __name__ == '__main__':
    series()
