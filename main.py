from calculadora import soma

# print(soma(1, 2))
# print(soma(-10, 20))
# print(soma(1.5, 2.5))

try:
    print(soma('10', 15))
except AssertionError as e:
    print(f'Conta inválida: {e}')

print('Conta', soma(25, 25))
