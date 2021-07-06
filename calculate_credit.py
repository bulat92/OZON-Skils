def calculate_credit(s, r, n):

    if (type(s) is not int) and (type(s) is not float):
        return f"В функцию передано не подходящее значение ({s}) это s"
    if (type(r) is not int) and (type(r) is not float):
        return f"В функцию передано не подходящее значение ({r}) это r"
    if (type(n) is not int) and (type(n) is not float):
        return f"В функцию передано не подходящее значение ({n}) это n"
    if s*n*r == 0:
        return f'В функцию передан 0!'

    r = r / 12
    result = int(s * (r * (1 + r) ** n) / ((1 + r) ** n - 1))
    return result


class Calculator():


    def sum(self, a, b):
        return a + b


    def mult(self, a, b):
        return a * b