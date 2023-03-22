print('Aumento salarial!')

sal = float(input('Digite o seu salário: R$'))
aum = sal + (sal * 15 / 100)
print('O salário de R${} aumentou para R${:.2f}.'.format(sal, aum))