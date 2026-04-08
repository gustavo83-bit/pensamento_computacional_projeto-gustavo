print('qual a sua idade?')


idade = int(input())

if idade < 18:
    print('voce e menor de idade')

elif idade <= 65:
    print('voce e adulto')

else:
    print('voce e idoso de idade')

