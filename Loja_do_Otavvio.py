"""
Autor : Douglas Nascimento (Shrek18.5)
Obs: Execício baseado no curso de ADS da UNINTER modulo EAD de 2022


"""
print('Bem vindo a loja do Otávio Machado Vimeiro')
produto = float(input('Insira o valor do produto: '))
qtd = int(input('Ok, e quantas unidades desse produto: '))

Psemdesconto  = produto * qtd

P5dedesconto = (produto * qtd * (5/100))

valorfinal5 = (Psemdesconto - P5dedesconto)

P10dedesconto = (produto * qtd * (10/100))

valorfinal10 = (Psemdesconto - P10dedesconto)

if(qtd < 9):
    print('Você está comprando {:.0f} unidade do nosso produto. \nEssa quantidade não há desconto, o valor total é {:.2f}!'.format(qtd, Psemdesconto))

elif(qtd >= 9 and qtd < 99):
    print('Você ganho 5% de desconto, o valor a ser pago é R$ {}'.format(valorfinal5))

elif(qtd >= 100 and qtd <999):
    print('Você ganho 10% de desconto, o valor a ser pago é R$ {}'.format(valorfinal10))
