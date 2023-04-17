import datetime
from random import randint
print('-=-' * 20)
print('\033[32m' 'ROBO DA BLAZE' '\033[m')
print('-=-' * 20)
seq = int(input('''qual foi a ultima sequencia de cores?
[1]vermelho, vermelho
[2]preto, preto
[3]vermelho, preto
[4]preto, vermelho
[5]apareceu branco
Digite aqui: '''))

data_e_hora_atuais = datetime.datetime.now()
datahora = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

lista = ['vermelho', 'preto', 'branco/preto', 'branco/vermelho']
esc = randint(0, 3)

if seq == 1:
    print('Com a sequencia de vermelho, vermelho as {} o proximo sera {}'.format(datahora, lista[esc]))
elif seq == 2:
    print('Com a sequencia de preto, preto as {} o proximo sera {}'.format(datahora, lista[esc]))
elif seq == 3:
    print('Com a sequencia de vermelho, preto as {} o proximo sera {}'.format(datahora, lista[esc]))
elif seq == 4:
    print('Com a sequencia de preto, vermelho as {} o proximo sera {}'.format(datahora, lista[esc]))
else:
    print('Como apareceu branco até {} o proximo sera {}'.format(datahora, lista[esc]))
