"""
raise - lançando exceções
https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
"""

# print(123)
# raise ValueError('Deu erro')
# print(456)


# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         print('erro...')
#         raise


# print(divide(8, 0))


# def divide(n, d):
#     if d == 0:
#         raise ZeroDivisionError('Você está tentando dividir por zero.')
#     return n / d


# print(divide(8, 0))


def nao_aceita_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero.')
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)

    nao_aceita_zero(d)
    return n / d


print(divide(8, '0'))
