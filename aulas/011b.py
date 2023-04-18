n1 = float(input('Digite a primeria nota:'))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 6:
    print('Voce passou de ano parabens, sua media foi de {:.1f}'.format(m))
else:
    print('Infelizmente voce reprovou, sua media foi de {:.1f}'.format(m))
