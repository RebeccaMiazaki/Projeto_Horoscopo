#Projeto Horoscopo

#Apresentação
print(f'\n\t\t Horóscopo \t\t')

#Entrada
dia= int(input('Informe o dia do seu aniversário: '))
mes= int(input('Informe o mês do seu aniversário: '))

#Processamento e Saída
if mes ==12 and dia >=22 or mes== 1 and dia <=20:
        print('Capricórnio')

elif mes ==1 and dia >=21 or mes== 2 and dia <=19:
        print('Áquario')

elif mes ==2 and dia >=20 or mes== 3 and dia <=20:
        print('Peixes')

elif mes ==3 and dia >=21 or mes== 4 and dia <=20:
        print('Áries')

elif mes ==4 and dia >=21 or mes== 5 and dia <=20:
        print('Touro')

elif mes ==5 and dia >=21 or mes== 6 and dia <=20:
        print('Gêmeos')

elif mes ==6 and dia >=21 or mes== 7 and dia <=21:
        print('Cancêr')

elif mes ==7 and dia >=22 or mes== 8 and dia <=22:
        print('Leão')

elif mes ==8 and dia >=23 or mes== 9 and dia <=22:
        print('Virgem')

elif mes ==9 and dia >=23 or mes== 10 and dia <=22:
        print('Libra')

elif mes ==10 and dia >=23 or mes== 11 and dia <=21:
        print('Escorpião')

elif mes ==11 and dia >=22 or mes== 12 and dia <=21:
        print('Sagitário')

else:
    print('Mês inválido')